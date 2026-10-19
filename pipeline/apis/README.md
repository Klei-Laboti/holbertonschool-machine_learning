# Data Collection - APIs

Scripts that collect and transform data from external APIs using the
Python `requests` package: handling HTTP GET requests, pagination,
rate limits, and JSON resources.

## Requirements
- Ubuntu 20.04 LTS, Python 3.9
- `requests` package
- pycodestyle 2.11.1
- All files start with `#!/usr/bin/env python3` and are executable

## Tasks
| File | Description |
|------|-------------|
| `0-passengers.py` | `availableShips(passengerCount)` — Swapi ships that can hold a given number of passengers |
| `1-sentience.py` | `sentientPlanets()` — home planets of all sentient species (Swapi) |
| `2-user_location.py` | Prints a GitHub user's location, handling 404 and rate-limit (403) |

## Author
Kleant Laboti
