import copy
import random
import unittest

from dijkstra import dijkstra, shortest_path


class ShortestPathTests(unittest.TestCase):
    def test_sink_nodes_zero_edges_and_input_unchanged(self):
        graph = {"A": {"B": 8, "C": 0}, "C": {"B": 2}, "X": {}}
        before = copy.deepcopy(graph)
        distances, previous = dijkstra(graph, "A")
        self.assertEqual(distances["B"], 2)
        self.assertEqual(shortest_path(previous, "A", "B"), ["A", "C", "B"])
        self.assertIsNone(shortest_path(previous, "A", "X"))
        self.assertEqual(graph, before)

    def test_invalid_weights(self):
        for value in (-1, float("nan")):
            with self.assertRaises(ValueError):
                dijkstra({"A": {"B": value}}, "A")

    def test_malformed_predecessor_chain_terminates(self):
        self.assertIsNone(shortest_path({"A": None, "B": "C", "C": "B"}, "A", "B"))
        self.assertIsNone(shortest_path({"A": None}, "A", "missing"))
        self.assertEqual(shortest_path({"A": None}, "A", "A"), ["A"])

    def test_against_independent_floyd_warshall(self):
        rng = random.Random(100)
        for _ in range(30):
            nodes = list("ABCDEF")
            graph = {a: {b: rng.randrange(10) for b in nodes
                         if b != a and rng.random() < 0.35} for a in nodes}
            expected = {(a, b): (0 if a == b else graph[a].get(b, float("inf")))
                        for a in nodes for b in nodes}
            for via in nodes:
                for a in nodes:
                    for b in nodes:
                        expected[a, b] = min(expected[a, b], expected[a, via] + expected[via, b])
            for start in nodes:
                distances, previous = dijkstra(graph, start)
                for end in nodes:
                    self.assertEqual(distances[end], expected[start, end])
                    path = shortest_path(previous, start, end)
                    if expected[start, end] == float("inf"):
                        self.assertIsNone(path)
                    else:
                        self.assertEqual(sum(graph[a][b] for a, b in zip(path, path[1:])), distances[end])


if __name__ == "__main__":
    unittest.main()
