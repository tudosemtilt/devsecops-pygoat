# quake-log-report-cloudwalk
 Log parser and reporter for Cloudwalk software engineering evaluation.

## Setup

1. [Download](https://www.python.org/downloads/) and install `Python 3.12` or higher.
2. Install `poetry` by running `pip install poetry` on your CLI
3. Install this project dependencies by running `poetry install` on your CLI

## Modules

- `filehandler`: Reads raw content from `.log` file
- `logparser`: Extracts the relevant informations from raw log
- `gamesreporter`: Builds and generates report from games parsed log info

## Report Format

```jsonc
{
  "game_1": {               // Game identifier
    "total_kills": 0,       // Total number of kills during game
    "players": [],          // All players connected during game
    "kills": {},            // Counter of kills per player
    "killing_methods": {}   // Counter of killing methods (e.g.: "MOD_ROCKET_SPLASH" )
  },
}
```
- Kill counting also includes the zero ones, since a player may have score `0` if it gets one kill, but it is killed once by the `<world>`
- For readability, only the observed killing methods are listed per game.

## How to Run

- On this project's root, run `poetry run py main.py` on your CLI
- The `report.json` file will be generated on this project's root as well
- Execution log `main.log` will also be generated

## How to Test

- On this project's root, run `poetry run pytest` on your CLI
- For a `html` coverage report, run `poetry run pytest --cov=modules test/ --cov-report html`. The report will be generated on `htmlcov` folder
- For a `CLI` coverage report, just run `poetry run pytest --cov=modules test/`

**Have fun! :)**
