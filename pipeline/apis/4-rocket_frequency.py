#!/usr/bin/env python3
"""
Script that fetches the SpaceX launch data and
displays the number of launches per rocket
"""

import requests
from collections import defaultdict

if __name__ == '__main__':
    url = "https://api.spacexdata.com/v4/launches"

    try:
        # Fetch all launches from the API
        response = requests.get(url)
        response.raise_for_status()

        # Get launch data
        launches = response.json()

        # Create a dictionary to count launches per rocket
        rocket_launch_counts = defaultdict(int)

        # Count launches for each rocket
        for launch in launches:
            rocket_name = launch.get('rocket')
            if rocket_name:
                rocket_launch_counts[rocket_name] += 1

        # Sort rockets by the number of launches (descending) and
        # alphabetically by name
        sorted_rockets = sorted(
            rocket_launch_counts.items(), key=lambda x: (-x[1], x[0]))

        # Print the results in the required format
        for rocket, count in sorted_rockets:
            print(f"{rocket}: {count}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
