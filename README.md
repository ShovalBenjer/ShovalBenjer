### Shoval Benjer, AI Engineer (Tel Aviv)

I build production LLM agents and the automation around them: eval-gated support
and CRM agents, an internal MCP layer over the business systems, call and content
QC pipelines. Most of my public work is security and tooling for the agent
ecosystem, since that is the part everyone is shipping fast and checking last.

**Now**, at i-sdd (Be Z Online): support, marketing, and sales-ops automations on
Azure AI Foundry. Took one multilingual support agent's answer-quality pass rate
from 24% to 64% under an eval gate, and built the internal MCP server the agents
and analysts run through.

**Public projects**

- [mcp-guard](https://github.com/ShovalBenjer/mcp-guard) — adversarial fuzzer for MCP servers. 65 findings against Anthropic's reference servers, published as a [leaderboard](https://github.com/ShovalBenjer/mcp-guard/blob/main/LEADERBOARD.md).
- [sqltok](https://github.com/ShovalBenjer/sqltok) — schema token-budget manager for Text-to-SQL. Keeps 97% of gold tables at 2,000 tokens on BIRD.
- [agenteval-bench](https://github.com/ShovalBenjer/agenteval-bench) — pytest-style eval suites for agents, with CI gating on regressions.
- [protobuf-fuzz-guard](https://github.com/ShovalBenjer/protobuf-fuzz-guard) — CVE-pattern scanning and fuzz harnesses for .proto services (Python, C++, Go).
- [altius](https://github.com/ShovalBenjer/altius-financial-analysis) — PE risk and forecasting (de-smoothing, Chronos, AutoGluon). [Live dashboard](https://lookerstudio.google.com/reporting/7b2515d4-9975-484f-a77f-1402f9e6d9b4).

**Stack**: Python, TypeScript, SQL · Azure (Foundry, Functions), AWS · MCP, A2A,
RAG, LangGraph · PyTorch, LightGBM, QLoRA · Docker, Kubernetes, Bicep.

A lot of the work is agentic security across the whole stack: code, DevOps
pipeline, deployed infra, PII in transcripts, and agent-token guardrails. Open to
research collabs and MSc discussions.

Reach me: [LinkedIn](https://www.linkedin.com/in/shoval-benjer) · shovalb9@gmail.com
