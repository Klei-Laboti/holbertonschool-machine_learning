#!/usr/bin/env python3
"""Prints the location of a specific GitHub user."""
import sys
import time
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset = int(response.headers["X-Ratelimit-Reset"])
        minutes = int((reset - time.time()) / 60)
        print("Reset in {} min".format(minutes))
    elif response.status_code == 200:
        print(response.json()["location"])
