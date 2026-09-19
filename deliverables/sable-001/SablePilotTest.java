package io.agentscope.extensions.model.openai;

import com.sun.net.httpserver.HttpServer;
import io.agentscope.core.ReActAgent;
import io.agentscope.core.agent.RuntimeContext;
import io.agentscope.core.message.Msg;
import io.agentscope.core.message.MsgRole;
import io.agentscope.core.model.ExecutionConfig;
import io.agentscope.core.model.GenerateOptions;
import io.agentscope.core.model.transport.JdkHttpTransport;
import io.agentscope.core.state.AgentState;
import io.agentscope.core.state.JsonFileAgentStateStore;
import io.agentscope.core.util.JsonUtils;
import io.agentscope.extensions.model.openai.formatter.OpenAIChatFormatter;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/** Independent real-HTTP probe; no production provider or real credential is used. */
public class SablePilotTest {
    static final String REVISION = "51d10ecfddadc45fb2173ff161e40e7bcf48d0be";
    static final String MARKER = "SABLE_LOCAL_CONTROL_OK";
    static final String USER = "synthetic-user";
    static final String SESSION = "synthetic-session";

    static void json(Path path, Object value) throws Exception {
        Files.writeString(path, JsonUtils.getJsonCodec().toPrettyJson(value), StandardCharsets.UTF_8);
    }

    /** Invoked in a NEW JVM, using the real framework state-store deserializer. */
    public static void main(String[] args) throws Exception {
        var store = new JsonFileAgentStateStore(Path.of(args[0]));
        var state = store.get(USER, SESSION, "agent_state", AgentState.class);
        List<String> assistants = new ArrayList<>();
        if (state.isPresent()) {
            for (Msg msg : state.get().getContext()) {
                if (msg.getRole() == MsgRole.ASSISTANT) assistants.add(msg.getTextContent());
            }
        }
        json(Path.of(args[1]), Map.of("reader_pid", ProcessHandle.current().pid(),
            "state_present", state.isPresent(), "assistant_texts", assistants,
            "assistant_count", assistants.size(), "observed_at", Instant.now().toString()));
    }

    @SuppressWarnings("unchecked")
    Map<String, Object> probe(Path root, String scenario) throws Exception {
        Path dir = root.resolve(scenario);
        Files.createDirectories(dir);
        Path stateDir = dir.resolve("state");
        assertFalse(Files.exists(stateDir), "Each run requires a fresh output directory");
        var store = new JsonFileAgentStateStore(stateDir);
        AtomicInteger requests = new AtomicInteger();
        List<Map<String, Object>> httpTrace = new ArrayList<>();
        HttpServer server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            int n = requests.incrementAndGet();
            String request = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            int status = scenario.equals("retry-control") && n == 1 ? 429 : 200;
            String body = status == 429 ? "{\"error\":{\"message\":\"synthetic rate limit\",\"type\":\"rate_limit_exceeded\"}}"
                : scenario.equals("done-only") ? "data: [DONE]\n\n"
                : "data: {\"id\":\"local-control\",\"object\":\"chat.completion.chunk\",\"choices\":[{\"index\":0,\"delta\":{\"role\":\"assistant\",\"content\":\"" + MARKER + "\"},\"finish_reason\":null}]}\n\n"
                + "data: {\"id\":\"local-control\",\"object\":\"chat.completion.chunk\",\"choices\":[{\"index\":0,\"delta\":{},\"finish_reason\":\"stop\"}]}\n\ndata: [DONE]\n\n";
            synchronized (httpTrace) {
                httpTrace.add(Map.of("request_number", n, "method", exchange.getRequestMethod(),
                    "path", exchange.getRequestURI().toString(), "request_body", request,
                    "response_status", status, "response_body", body, "at", Instant.now().toString()));
            }
            exchange.getResponseHeaders().set("Content-Type", status == 200 ? "text/event-stream" : "application/json");
            byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var stream = exchange.getResponseBody()) { stream.write(bytes); }
        });
        server.start();
        AtomicReference<String> terminal = new AtomicReference<>("NOT_OBSERVED");
        List<String> delivered = new ArrayList<>();
        String error = "";
        var transport = JdkHttpTransport.builder().build();
        try {
            var model = OpenAIChatModel.builder().apiKey("local-dummy-not-a-credential")
                .modelName("synthetic-model").stream(true)
                .baseUrl("http://127.0.0.1:" + server.getAddress().getPort())
                .formatter(new OpenAIChatFormatter()).httpTransport(transport).build();
            var options = GenerateOptions.builder().stream(true).executionConfig(
                ExecutionConfig.builder().maxAttempts(3).initialBackoff(Duration.ofMillis(20))
                    .maxBackoff(Duration.ofMillis(50)).build()).build();
            var agent = ReActAgent.builder().name("local-verifier").sysPrompt("Return the supplied harmless marker.")
                .model(model).generateOptions(options).stateStore(store).build();
            agent.call("Return " + MARKER,
                    RuntimeContext.builder().userId(USER).sessionId(SESSION).build())
                .doOnNext(msg -> delivered.add(msg.getTextContent()))
                .doOnSuccess(msg -> terminal.set("onComplete"))
                .doOnError(ex -> terminal.set("onError"))
                .block(Duration.ofSeconds(30));
        } catch (Throwable ex) {
            error = ex.getClass().getName() + ": " + ex.getMessage();
        } finally {
            server.stop(0);
            transport.close();
        }
        json(dir.resolve("http-trace.json"), httpTrace);
        String cp = System.getProperty("surefire.test.class.path", System.getProperty("java.class.path"));
        Path argsFile = dir.resolve("reader.args");
        // Java argument files avoid Windows command-line length limits. Not part of public evidence.
        Files.writeString(argsFile, "-Xms16m\n-Xmx128m\n-cp\n" + quoted(cp) + "\n" + getClass().getName() + "\n"
            + quoted(stateDir.toAbsolutePath().toString()) + "\n"
            + quoted(dir.resolve("fresh-read.json").toAbsolutePath().toString()) + "\n");
        var child = new ProcessBuilder(Path.of(System.getProperty("java.home"), "bin", "java").toString(),
                "@" + argsFile.toAbsolutePath()).redirectErrorStream(true)
                .redirectOutput(dir.resolve("reader.log").toFile()).start();
        boolean childFinished = child.waitFor(30, TimeUnit.SECONDS);
        if (!childFinished) child.destroyForcibly();
        assertTrue(childFinished, "Fresh-reader timeout");
        assertEquals(0, child.exitValue(), "Fresh-reader failed; inspect reader.log");
        var fresh = JsonUtils.getJsonCodec().fromJson(Files.readString(dir.resolve("fresh-read.json")), Map.class);
        assertNotEquals(ProcessHandle.current().pid(), ((Number) fresh.get("reader_pid")).longValue());
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("scenario", scenario);
        result.put("runtime_source_revision", REVISION);
        result.put("java_version", System.getProperty("java.version"));
        result.put("configured_max_attempts", 3);
        result.put("http_request_count", requests.get());
        result.put("http_retries_observed", Math.max(0, requests.get() - 1));
        result.put("terminal_signal", terminal.get());
        result.put("delivered_assistant_texts", delivered);
        result.put("call_exception", error);
        result.put("parent_pid", ProcessHandle.current().pid());
        result.put("fresh_process_read", fresh);
        result.put("observed_at", Instant.now().toString());
        json(dir.resolve("result.json"), result);
        return result;
    }

    static String quoted(String text) { return "\"" + text.replace("\\", "\\\\").replace("\"", "\\\"") + "\""; }

    @Test
    @SuppressWarnings("unchecked")
    void independentHttpAndPersistenceExperiment() throws Exception {
        Path root = Path.of(System.getProperty("sable.output"));
        Files.createDirectories(root);
        var normal = probe(root, "normal-control");
        var retry = probe(root, "retry-control");
        var empty = probe(root, "done-only");
        boolean controls = validControl(normal, 1) && validControl(retry, 2);
        boolean zero = "onComplete".equals(empty.get("terminal_signal"))
            && "".equals(empty.get("call_exception")) && ((Number)empty.get("http_request_count")).intValue() == 1
            && ((List<?>)empty.get("delivered_assistant_texts")).isEmpty()
            && ((Number)((Map<?,?>)empty.get("fresh_process_read")).get("assistant_count")).intValue() == 0;
        boolean incomplete = !controls || "NOT_OBSERVED".equals(empty.get("terminal_signal"));
        json(root.resolve("summary.json"), Map.of("classification", incomplete ? "EVIDENCE GAP" : zero ? "VERIFIED" : "NOT VERIFIED",
            "controls_passed", controls, "revision", REVISION, "cases", List.of(normal, retry, empty),
            "boundary", "Local DONE-only HTTP 200 through actual JDK transport and ReActAgent.call; no production-frequency or provider-prevalence claim. No fallback model configured."));
        assertTrue(controls, "Positive content/persistence and retry controls must pass before classification");
    }

    static boolean validControl(Map<String, Object> x, int count) {
        var fresh = (Map<?,?>)x.get("fresh_process_read");
        return "onComplete".equals(x.get("terminal_signal")) && "".equals(x.get("call_exception"))
            && ((Number)x.get("http_request_count")).intValue() == count
            && ((List<?>)x.get("delivered_assistant_texts")).equals(List.of(MARKER))
            && ((List<?>)fresh.get("assistant_texts")).equals(List.of(MARKER));
    }
}
