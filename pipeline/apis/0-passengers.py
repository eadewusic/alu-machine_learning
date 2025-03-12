#!/usr/bin/env python3
"""
Module that retrieves ships from the SWAPI API that
can hold a given number of passengers
"""

import requests


def availableShips(passengerCount):
    """
    Returns a list of starship names that can hold
    at least passengerCount passengers

    Args:
        passengerCount (int): The minimum number of
        passengers the starship must accommodate

    Returns:
        List of starship names (list of str)
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break  # Failed to fetch data, exit loop

        data = response.json()

        for ship in data.get('results', []):
            passengers = ship.get('passengers', '0').replace(',', '')

            # Ignore if it's 'unknown' or 'n/a'
            if passengers.lower() in ['unknown', 'n/a']:
                continue

            try:
                passenger_num = int(passengers)
            except ValueError:
                continue  # Skip if passengers value can't be converted to int

            if passenger_num >= passengerCount:
                ships.append(ship['name'])

        # Move to the next page (if available)
        url = data.get('next')

    return ships
