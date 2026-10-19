#!/usr/bin/env python3
"""Returns the home planets of all sentient species."""
import requests


def sentientPlanets():
    """Return names of home planets of all sentient species."""
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    while url is not None:
        response = requests.get(url)
        data = response.json()

        for species in data["results"]:
            classification = species["classification"]
            designation = species["designation"]
            if classification == "sentient" or designation == "sentient":
                home = species["homeworld"]
                if home is not None:
                    planet = requests.get(home).json()
                    planets.append(planet["name"])

        url = data["next"]

    return planets
