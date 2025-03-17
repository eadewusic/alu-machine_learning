#!/usr/bin/env python3
"""
Module that retrieves the list of home planets
for all sentient species using SWAPI
"""

import requests


def sentientPlanets():
    """
    Returns a list of names of home planets of all sentient species

    Returns:
        List of planet names (list of str)
    """
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []  # Use a list to maintain order

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()
        for species in data.get('results', []):
            # If species has a language and homeworld, consider them sentient
            if species.get('language'):
                homeworld_url = species.get('homeworld')

                if homeworld_url:
                    hw_response = requests.get(homeworld_url)
                    if hw_response.status_code == 200:
                        homeworld_data = hw_response.json()
                        planet_name = homeworld_data.get('name')
                        if planet_name not in planets:
                            planets.append(planet_name)
                else:
                    if 'unknown' not in planets:
                        planets.append('unknown')

        # Move to next page if available
        url = data.get('next')

    return planets
