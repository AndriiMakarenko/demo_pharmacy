# demo_pharmacy

## Installation

Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.  
Then run:

```bash
poetry install
```

## Running the system

Start the API server:

```bash
poetry run python -m pharmacy.main
```

In separate terminals:

Start the agents (spawns 2–5 workers):

```bash
poetry run run-agents
```

Start the task creator:

```bash
poetry run run-task-creator
```

## If I had more time

- Wrap the simulation scripts and the application in a docker-compose file  
- Add unit tests for the application  
- Ensure that the previously existing agents are wiped from the system upon launch of the new simulation (with a separate endpoint for that)
- Add logging to the application