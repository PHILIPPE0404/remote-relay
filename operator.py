import asyncio
import json
import requests
import websockets

SERVER_HTTP = "https://TON-SERVICE.onrender.com"
SERVER_WS = "wss://TON-SERVICE.onrender.com"

def create_session():
    response = requests.post(f"{SERVER_HTTP}/session", timeout=15)
    response.raise_for_status()
    return response.json()["code"]

async def main():
    code = create_session()

    print()
    print("=" * 40)
    print("SESSION CREEE")
    print("=" * 40)
    print(f"Code : {code}")
    print("=" * 40)
    print()

    url = f"{SERVER_WS}/ws/operator/{code}"

    async with websockets.connect(url) as ws:
        print("En attente du client...")

        async def receive():
            async for message in ws:
                print("\n[CLIENT]", json.loads(message))

        async def send():
            while True:
                text = await asyncio.to_thread(input, "> ")
                await ws.send(json.dumps({"text": text}))

        await asyncio.gather(receive(), send())

if __name__ == "__main__":
    asyncio.run(main())
