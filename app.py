import streamlit as st
import requests

st.set_page_config(page_title="Agentic DevOps Telemetry Core", page_icon="🚀", layout="wide")
st.title("🚀 Agentic DevOps Telemetry Core")
st.subheader("Autonomous Multi-Agent Log Parsing & Incident Remediation Dashboard")
st.markdown("---")

col_input, col_output = st.columns([1, 1])

with col_input:
    st.markdown("### 📥 Live Telemetry Ingestion Inflow")
    sample_logs = (
        "2026-06-27T14:32:01.482Z [CRITICAL] [AUTH_MODULE] DB_CONNECTION_TIMEOUT: Outbound pool exhausted on host 10.192.4.55:5432. Active connections: 100/100.\n"
        "2026-06-27T14:32:05.119Z [ERROR] [API_GATEWAY] HTTP_504: Gateway Timeout serving request /v1/user/profile - Upstream container unresponsive.\n"
        "2026-06-27T14:32:10.881Z [WARN] [RESOURCE_MONITOR] CPU utilization at 94.8% on container instance azure-compute-node-04a."
    )
    log_input = st.text_area("Production Log Stream Payload", value=sample_logs, height=250)
    trigger_btn = st.button("⚡ Trigger Agentic Runbook Pipeline", use_container_width=True)

with col_output:
    st.markdown("### 🎯 Live Operational Execution Reports")
    if trigger_btn:
        if not log_input.strip():
            st.warning("⚠️ Please provide a valid log payload.")
        else:
            with st.spinner("🤖 Inter-Agent Handshake Active..."):
                try:
                    response = requests.post("http://127.0.0.1:8000/api/v1/remediate", json={"logs": log_input})
                    if response.status_code == 200:
                        data = response.json()
                        st.success("✅ Multi-Agent Consensus Achieved!")
                        with st.expander("📊 Agent 1: Log Analyst Structured Metrics", expanded=True):
                            st.markdown(data["structured_metrics"])
                        with st.expander("🛠️ Agent 2: Tier-2 Recovery Playbook", expanded=True):
                            st.markdown(data["remediation_playbook"])
                    else:
                        st.error(f"❌ Backend Error ({response.status_code})")
                except Exception as e:
                    st.error(f"❌ Connection Error: {str(e)}")
    else:
        st.info("💡 Awaiting telemetry payload submission.")
