# CoinGecko 脚本可靠性申请（已发送）

[原任务](https://laborx.com/jobs/enhance-coingecko-bot-reliability-96610)，买方 Morty Sheko。原截止日为 2025-09-24，需求是否仍存在未确认。用户统一授权自动发申请后，发送一次明确以核实旧需求为前提的申请；预算 300 美元等值、审阅代码并确认范围及托管后 5 天、一次修改。平台 My Jobs 已显示完整申请、Budget $300、Deadline 5 days 和 Chat。无买方接受或收入。

## 完整申请

Hi Morty, is this Python reliability task still available? I see the original deadline has passed and would confirm the need before starting.

For the described existing script, I propose USD 300 equivalent and 5 days after we review the code, agree acceptance criteria and fund LaborX escrow. The scope would cover configurable request pacing for your actual CoinGecko plan, bounded retries with exponential backoff and jitter, Retry-After handling, timeouts, and clear logging for connection/JSON errors. Output formatting would remain unchanged, with atomic output writes to preserve the last valid file when a run fails. Incomplete runs would be flagged rather than presented as fresh complete data.

Delivery: a patch to the existing Python code, regression tests using mocked 429/timeouts/malformed responses plus an output-format fixture, and a short run guide; one revision within the agreed scope. New data sources, deployment or paid API upgrades are outside this proposal. Please share the redacted script, dependencies, API plan, error examples and expected .txt output. Please do not send API keys or other secrets.

I use AI-assisted development and tests, and do not claim an existing client portfolio. My reproducible synthetic Python sample is here: https://github.com/WeiliangHuang-UM-connect/codex-pro-100-dollar-experiment/tree/main/examples/csv-orders

Would USDC on Base through LaborX escrow work, or another mutually supported stablecoin/network? This proposal remains subject to your confirmation that the task is open and our agreement on the reviewed scope.
