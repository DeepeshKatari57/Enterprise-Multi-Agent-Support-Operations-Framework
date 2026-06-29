Multi-Agent DevOps Dashboard 

```markdown
 🚀 Agentic DevOps Telemetry Core

An asynchronous, event-driven multi-agent framework designed to completely eliminate human triaging latency in production infrastructure monitoring loops. The system isolates raw, unstructured application error logs, validates them through strict data serialization contracts, and orchestrates an autonomous inter-agent handshake to output structured root-cause matrices and executable recovery playbooks.

 🧠 Multi-Agent Handshake Mechanics
Rather than relying on a single monolithic system prompt, this framework breaks operations down into an asymmetric multi-agent architecture:
* Agent 1 (Senior Systems Log Analyst):** Parses raw, un-indexed telemetry strings. Set to a deterministic temperature of `0.1` to extract timestamps, faulting modules, and structural summaries without hallucinations.
* Agent 2 (Senior SRE Engineer):** Consumes Agent 1's structured table directly. Set to a temperature of `0.2` to synthesize terminal commands, container rollback patterns, and tier-2 mitigation logic.

🏗️ Architecture & Component Topology
This framework enforces a strict decoupling of the interface layer from the core business logic:
* Asynchronous API Core (FastAPI Backend):** Listens for streaming JSON telemetry strings validated at runtime via Pydantic Data Transfer Objects (DTOs).
* Interactive UI (Streamlit Frontend):** A state-driven application interface that maps user inputs to background ports and handles runtime markdown compilation.
* Network Proxy Layer (Ngrok):** Securely exposes local application ports via production-grade TLS network tunnels.



🛠️ Tech Stack
* AI & Orchestration: Groq Cloud SDK (Llama 3.3 70B Versatile API Engine)
* Backend Core: FastAPI, Uvicorn, Pydantic (Type Enforcement)
* Frontend View: Streamlit (Dynamic Component Engine)
* Networking: Pyngrok Proxy Clients

📸 Dashboard Interface Display
> 💡 Tip: Take a screenshot of your active Streamlit web page showing the "Multi-Agent Consensus Achieved" block and place it in your repository root as `dashboard.png`!

![Agentic Dashboard Interface Workflow](dashboard.png)

## 🚀 Quick Start

### 1. Set Up Environment Keys
Export your cloud inference API key to your system environment variables to secure your credentials:
```bash
export GROQ_API_KEY="your_actual_groq_api_token_here"
export NGROK_AUTHTOKEN="your_actual_ngrok_token_here"
