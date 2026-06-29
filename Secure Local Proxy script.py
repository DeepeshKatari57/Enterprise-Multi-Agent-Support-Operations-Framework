import os
from pyngrok import ngrok

# Pull token from local machine environment variables instead of hardcoded raw values
NGROK_TOKEN = os.environ.get("NGROK_AUTHTOKEN")
if not NGROK_TOKEN:
    raise RuntimeError("❌ Network Alert: Environment variable 'NGROK_AUTHTOKEN' is missing.")

ngrok.set_auth_token(NGROK_TOKEN)

# Clean up any stale active sessions
tunnels = ngrok.get_tunnels()
for t in tunnels:
    ngrok.disconnect(t.public_url)

# Connect proxy securely to our Streamlit port
public_url = ngrok.connect(8501)
print(f"\n🌐 YOUR DASHBOARD URL IS:\n{public_url.public_url}\n")
