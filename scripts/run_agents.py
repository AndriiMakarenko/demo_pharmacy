import asyncio
import random
from agents.agent import Agent

async def main():
    num_agents = random.randint(2, 5)
    agents = [
        Agent(f"agent_{i}", token_bank=random.randint(200, 1000))
        for i in range(num_agents)
    ]
    await asyncio.gather(*(agent.run() for agent in agents))

if __name__ == "__main__":
    asyncio.run(main())
