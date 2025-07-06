import asyncio
import random
import string
import httpx

from pharmacy.core import config

API_URL = f"http://localhost:{config.port}"
AUTH_HEADER = {"Authorization": "Bearer secret-token"}

def generate_payload():
    length = random.randint(100, 200)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

async def create_task():
    task_data = {
        "type": random.choice(["TYPE_A", "TYPE_B", "TYPE_C"]),
        "payload": generate_payload(),
        "tokens": random.randint(10, 50)
    }
    async with httpx.AsyncClient() as client:
        try:
            await client.post(f"{API_URL}/new_task", json=task_data, headers=AUTH_HEADER)
        except Exception as e:
            print(f"Error creating task: {e}")

async def main():
    while True:
        await create_task()
        await asyncio.sleep(random.randint(30, 60))

if __name__ == "__main__":
    asyncio.run(main())
