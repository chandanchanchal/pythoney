# 40-Hour Corporate Training Program
## Agentic AI, Enterprise Agent Development & LLMOps on AWS Bedrock

**Delivery mode:** Virtual (live, instructor-led)
**Batch size:** ~25 participants
**Duration:** 40 hours (recommended: 5 days x 8 hrs, or 8 sessions x 5 hrs across 2–3 weeks)
**Audience level:** Intermediate–Advanced (assumes participants have already built/deployed LLM solutions in production on Bedrock)

---

## 1. Program Design Philosophy

Since the audience already has production experience with Bedrock, this program is designed as an **advancement track**, not a "getting started" course. It spends minimal time on GenAI basics and prompt-engineering 101, and instead front-loads:

- Agentic architecture patterns (single-agent, multi-agent, orchestration)
- Hands-on build-out of enterprise-grade agents (not toy demos)
- Deep dive into Bedrock Agents, Knowledge Bases, Action Groups, Guardrails
- Advanced prompting techniques used for agentic reasoning, tool-use, and reliability — not basic prompt writing
- LLMOps: evaluation, observability, cost governance, CI/CD for agents, security

Every module pairs a **conceptual block** with a **hands-on lab** using a shared sandbox AWS account. Recommend closing with a **capstone project** (built into the LLMOps module) so participants leave with a working, deployable agent.

---

## 2. Hour Allocation Summary

| # | Module | Hours |
|---|--------|-------|
| 1 | Agentic AI Foundations | 6 |
| 2 | Advanced Prompt Engineering (for Agentic Systems) | 5 |
| 3 | Advanced Generative AI Development | 6 |
| 4 | Building Enterprise Agents (framework-based) | 8 |
| 5 | Amazon Bedrock Agents (deep dive) | 8 |
| 6 | LLMOps (Eval, Observability, Security, Deployment) | 7 |
| | **Total** | **40** |

---

## 3. Detailed Table of Contents

### Module 1 — Agentic AI Foundations (6 hrs)

**Learning objectives:** By the end, participants can distinguish agent architectures, explain the reasoning/acting loop, and select the right pattern for a given business problem.

| Time | Topic |
|------|-------|
| 0.5h | Landscape check: from RAG/chatbots to agents — why enterprises are moving to agentic systems |
| 1h | Core agent anatomy: LLM as reasoning engine, memory, tools, planner, orchestrator |
| 1h | Agent design patterns: ReAct, Plan-and-Execute, Reflexion, Tree-of-Thought for planning |
| 1h | Single-agent vs multi-agent systems; orchestrator-worker, hierarchical, and collaborative (swarm) patterns |
| 1h | Tool use & function calling fundamentals: schemas, structured outputs, error handling |
| 1h | **Lab:** Build a minimal ReAct agent from scratch (no framework) using an LLM API + 2 tools, to expose what frameworks abstract away |
| 0.5h | Discussion: where agentic AI fits (and doesn't) in enterprise workflows; failure modes (loops, hallucinated tool calls, cost runaway) |

---

### Module 2 — Advanced Prompt Engineering for Agentic Systems (5 hrs)

**Note:** Since teams already have Bedrock production experience, this skips prompting basics and focuses on prompting for reliability, reasoning, and multi-step tool use.

**Learning objectives:** Design prompts/system instructions that reduce agent hallucination, improve tool-selection accuracy, and control multi-step reasoning.

| Time | Topic |
|------|-------|
| 0.5h | Quick recap & gap-check (not a full re-teach) — chain-of-thought, few-shot, role prompting |
| 1h | Prompting for structured/tool-calling reliability: JSON schema adherence, function-call disambiguation, reducing tool hallucination |
| 1h | Prompting for multi-step reasoning: task decomposition prompts, self-consistency, reflection/self-critique loops |
| 1h | Context engineering: managing long context windows, context compression, dynamic context injection (RAG + memory + tool results) |
| 1h | Guardrail-aware prompting: prompt-injection resistance, jailbreak mitigation, output validation prompts |
| 0.5h | **Lab:** Refactor a fragile multi-tool agent prompt to improve tool-selection accuracy and reduce hallucinated calls (before/after eval) |

---

### Module 3 — Advanced Generative AI Development (6 hrs)

**Learning objectives:** Apply advanced RAG, fine-tuning/customization, and multi-modal techniques within enterprise architecture constraints.

| Time | Topic |
|------|-------|
| 1h | Beyond basic RAG: hybrid search, re-ranking, query rewriting/expansion, parent-child chunking |
| 1h | Advanced RAG architectures: GraphRAG, agentic RAG (retrieval as a tool call, not a pipeline step) |
| 1h | Model customization: fine-tuning vs. RAG vs. prompting decision framework; Bedrock fine-tuning & model distillation options |
| 1h | Multi-modal generative AI: document/image understanding, multi-modal agents (Bedrock multi-modal models) |
| 1h | Structured generation & output control: constrained decoding, JSON mode, schema-validated generation |
| 1h | **Lab:** Build an agentic-RAG pipeline with re-ranking and query rewriting over an enterprise-style document set |

---

### Module 4 — Building Enterprise Agents (8 hrs)

**Learning objectives:** Design and build a production-grade agent using an orchestration framework, with proper state management, tool integration, and multi-agent collaboration.

| Time | Topic |
|------|-------|
| 1h | Enterprise agent architecture: reference architecture (ingress, orchestrator, tools/APIs, memory store, guardrails, logging) |
| 1h | Framework overview & comparison: LangGraph, CrewAI, AutoGen/AG2, and Bedrock-native options — when to use which |
| 1.5h | **Lab:** Build a stateful agent graph with conditional routing, retries, and human-in-the-loop checkpoints (LangGraph) |
| 1h | Multi-agent orchestration: supervisor/worker pattern, task delegation, shared memory, inter-agent communication |
| 1.5h | **Lab:** Build a 3-agent collaborative workflow (e.g., research agent → analysis agent → report agent) with handoffs |
| 1h | Integrating enterprise systems: connecting agents to internal APIs, databases, ticketing/CRM systems; auth patterns (OAuth, IAM roles, secrets management) |
| 1h | Error handling, retries, circuit breakers, and cost/latency controls in agent loops |

---

### Module 5 — Amazon Bedrock Agents (Deep Dive) (8 hrs)

**Learning objectives:** Configure, deploy, and operate Bedrock Agents end-to-end including Knowledge Bases, Action Groups, multi-agent collaboration, and Guardrails — since teams already run Bedrock in production, this goes deep rather than introductory.

| Time | Topic |
|------|-------|
| 0.5h | Bedrock Agents architecture recap (fast-paced, assumes familiarity) |
| 1h | Action Groups deep dive: OpenAPI schema design, Lambda function integration, parameter handling, return-of-control pattern |
| 1h | Knowledge Bases for Bedrock: data sources, chunking strategies, vector store options (OpenSearch Serverless, Aurora, Pinecone), metadata filtering |
| 1h | **Lab:** Build a Bedrock Agent with a custom Action Group (Lambda-backed) and an attached Knowledge Base |
| 1h | Multi-agent collaboration in Bedrock (supervisor agents + collaborator agents), agent aliases & versioning |
| 1h | Bedrock Guardrails: content filters, denied topics, PII redaction, contextual grounding checks, integrating guardrails into agent flows |
| 1.5h | **Lab:** Extend the agent into a supervisor + 2 collaborator-agent system with guardrails applied |
| 1h | Bedrock Agent deployment patterns: aliases, throttling/quota management, VPC/private networking, cross-account access patterns |

---

### Module 6 — LLMOps (7 hrs)

**Learning objectives:** Establish evaluation, observability, security, and CI/CD practices to run agentic systems reliably at enterprise scale; complete a capstone deployment.

| Time | Topic |
|------|-------|
| 1h | LLMOps vs. traditional MLOps: what's different for agentic systems (non-determinism, tool chains, cost variability) |
| 1h | Evaluation frameworks: offline eval (task success rate, tool-call accuracy, groundedness/faithfulness), LLM-as-judge design, regression test suites for prompts/agents |
| 1h | Observability & tracing: instrumenting agent traces (tool calls, latency, token usage), using Langfuse/LangSmith or CloudWatch + X-Ray, building agent "flight recorders" |
| 1h | Cost & performance governance: token/cost monitoring, caching strategies, model routing (cheap model for tools, strong model for reasoning), rate limiting |
| 1h | Security & compliance: prompt-injection defenses, data residency, audit logging, IAM least-privilege for agent tool access, PII handling |
| 1h | CI/CD for agents: prompt/version control, automated eval gates before deploy, blue/green or canary rollout for agent updates |
| 1h | **Capstone:** Teams take an agent built earlier in the week, add eval + observability + a guardrail, and present a short deployment readiness review |

---

## 4. Requirements

### 4.1 Participant Prerequisites
- Hands-on Python proficiency (participants should be comfortable writing/debugging Python scripts)
- Working familiarity with Amazon Bedrock (model invocation, basic prompting) — **assumed, not taught**
- Basic understanding of REST APIs / JSON
- Git fundamentals (branching, commits) for the LLMOps module
- Recommended pre-read: AWS Bedrock Agents documentation overview (sent 1 week prior)

### 4.2 Technical/Environment Requirements
- **AWS Sandbox accounts** for each participant (or pooled team accounts) with:
  - Bedrock model access enabled (text + multi-modal models used in labs)
  - Bedrock Agents, Knowledge Bases, Guardrails enabled
  - OpenSearch Serverless (or equivalent vector store) provisioned
  - Lambda, IAM role creation permissions, S3 buckets for data sources
  - Budget alerts/quotas configured to cap lab spend
- Python 3.10+, `boto3`, `langgraph`/`langchain`, Jupyter or VS Code set up in advance (setup guide to be shared pre-course)
- A shared Git repository (GitHub/GitLab/CodeCommit) for lab code and the capstone
- Optional but recommended: Langfuse or LangSmith trial account for the observability module
- Stable video conferencing platform with breakout room support (batch of 25 → suggest 5 breakout groups of 5 for labs)

### 4.3 Logistics Recommendations
- Run labs in **breakout groups of 4–5** with one lab document per group; trainer/TA rotates through rooms
- Assign **1 teaching assistant per 12–15 participants** for lab support given the hands-on density of Modules 4–6
- Send **environment setup instructions 3–5 business days before Day 1** — sandbox provisioning is the #1 cause of lost lab time in virtual corporate trainings
- Record all sessions; share lab notebooks/code after each module
- Consider spacing delivery as **5 consecutive days** for momentum, or **2 sessions/week over 4 weeks** if participants need to interleave with regular work — the latter works better for retention but requires re-establishing environment state each session
- Build in a **20-minute buffer per session** for AWS console latency/quota issues, which are common in live Bedrock labs

### 4.4 Trainer-side Recommendations
- Pre-build one "golden path" reference agent for each lab so debugging in live sessions is fast
- Prepare fallback pre-recorded demo clips in case of AWS service throttling during the live session (Bedrock quotas can be tight for shared sandbox accounts with 25 concurrent users)
- Provide a **capstone rubric** in advance so participants know what "deployment-ready" looks like going into Module 6
- Share a **post-training resource pack**: architecture reference diagrams, prompt libraries, eval templates, and a Bedrock quota/cost checklist

---

## 5. Suggested Assessment / Certification Criteria
- Lab completion across Modules 4–6 (agent build, Bedrock deployment, capstone)
- Capstone presentation: working agent + eval report + at least one guardrail + one observability trace
- Optional written quiz on architecture decision-making (RAG vs. fine-tune vs. agent; framework selection; guardrail design)
