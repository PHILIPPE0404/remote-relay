import asyncio
import json
import websockets

SERVER = "wss://TON-SERVICE.onrender.com"

async def main():
    code = input("Code de session : ").strip()
    url = f"{SERVER}/ws/client/{code}"

    print("Connexion au serveur...")

    async with websockets.connect(url) as ws:
        print("Connecte.")

        async def receive():
            async for message in ws:
                print("\n[RECU]", json.loads(message))

        async def send():
            while True:
                text = await asyncio.to_thread(input, "> ")
                await ws.send(json.dumps({"text": text}))

        await asyncio.gather(receive(), send())

if __name__ == "__main__":
    asyncio.run(main())
