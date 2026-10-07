import secrets
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
sessions = {}

def generate_code():
    return f"{secrets.randbelow(1_000_000):06d}"

@app.get("/")
def home():
    return {"status": "online", "service": "remote-relay"}

@app.post("/session")
def create_session():
    code = generate_code()
    while code in sessions:
        code = generate_code()
    sessions[code] = {"client": None, "operator": None}
    return {"code": code}

@app.websocket("/ws/{role}/{code}")
async def websocket_endpoint(websocket: WebSocket, role: str, code: str):
    if role not in ("client", "operator") or code not in sessions:
        await websocket.close(code=1008)
        return

    session = sessions[code]
    if session[role] is not None:
        await websocket.close(code=1008)
        return

    await websocket.accept()
    session[role] = websocket

    try:
        other_role = "operator" if role == "client" else "client"
        other = session[other_role]

        if other:
            await other.send_json({"type": "connected", "role": role})

        while True:
            message = await websocket.receive_json()
            other = session[other_role]
            if other:
                await other.send_json({
                    "type": "message",
                    "from": role,
                    "data": message
                })
    except WebSocketDisconnect:
        pass
    finally:
        if session.get(role) is websocket:
            session[role] = None

        other_role = "operator" if role == "client" else "client"
        other = session.get(other_role)
        if other:
            try:
                await other.send_json({"type": "disconnected", "role": role})
            except Exception:
                pass
