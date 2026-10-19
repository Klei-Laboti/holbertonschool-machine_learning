#!/usr/bin/env python3
"""Returns the list of ships that can hold a given number of passengers."""
import requests


def availableShips(passengerCount):
    """Return ship names holding at least passengerCount passengers."""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url is not None:
        response = requests.get(url)
        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "")
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])

        url = data["next"]

    return ships
