import asyncio
import random
import httpx

from pharmacy.core.config import Config

API_URL = f"http://localhost:{Config().port}"
AUTH_HEADER = {"Authorization": "Bearer secret-token"}

class Agent:
    def __init__(self, agent_id: str, token_bank: int):
        self.agent_id = agent_id
        self.token_bank = token_bank

    async def run(self):
        while True:
            await asyncio.sleep(1)
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(f"{API_URL}/next_task", headers=AUTH_HEADER)
                    if response.status_code == 204:
                        await asyncio.sleep(30)
                        continue
                    task = response.json()
                    task_id = task["id"]
                    token_cost = task["tokens"]
                    if self.token_bank < token_cost:
                        outcome = "failed"
                    else:
                        await asyncio.sleep(random.randint(3, 5))
                        outcome = random.choice(["completed", "failed"])
                        if outcome == "completed":
                            self.token_bank -= token_cost
                    await client.post(f"{API_URL}/update_task/{task_id}", json={"status": outcome}, headers=AUTH_HEADER)
            except Exception as e:
                print(f"Agent {self.agent_id} error: {e}")
