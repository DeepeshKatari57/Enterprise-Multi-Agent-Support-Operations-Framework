import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq

app = FastAPI(title="Agentic DevOps Telemetry Core")

# Secure Token Hydration Layer: Pulls key from local environment configuration safely
GROQ_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_KEY:
    raise RuntimeError("❌ SRE Alert: Environment variable 'GROQ_API_KEY' is missing or unauthenticated.")

client = Groq(api_key=GROQ_KEY)

class LogPayload(BaseModel):
    logs: str

class AutomatedIncidentReport(BaseModel):
    status: str = "success"
    structured_metrics: str
    remediation_playbook: str

@app.post("/api/v1/remediate", response_model=AutomatedIncidentReport)
async def process_telemetry_pipeline(payload: LogPayload):
    try:
        # Agent 1: Log Analyst
        response_analyst = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a Senior Systems Log Analyst. Provide a clean markdown table summarizing the timestamp, failing module, and root cause."},
                {"role": "user", "content": f"Analyze these logs:\n{payload.logs}"}
            ],
            temperature=0.1
        )
        parsed_table = response_analyst.choices[0].message.content

        # Agent 2: DevOps Responder
        response_responder = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a Senior DevOps Engineer. Write an explicit incident response playbook with terminal commands based on the summary table."},
                {"role": "user", "content": f"Review this table and write a playbook:\n{parsed_table}"}
            ],
            temperature=0.2
        )
        playbook = response_responder.choices[0].message.content

        return AutomatedIncidentReport(structured_metrics=parsed_table, remediation_playbook=playbook)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
