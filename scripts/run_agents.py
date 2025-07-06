import asyncio
import random
from agents.agent import Agent

async def run():
    # num_agents = random.randint(2, 5)
    num_agents = 1
    agents = [
        Agent(f"agent_{i}", token_bank=random.randint(200, 1000))
        for i in range(num_agents)
    ]
    await asyncio.gather(*(agent.run() for agent in agents))

def main():
    asyncio.run(run())
