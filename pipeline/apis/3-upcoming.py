#!/usr/bin/env python3
"""
Script that fetches and displays the next
upcoming SpaceX launch with specific details
"""

import requests
from datetime import datetime

if __name__ == '__main__':
    url = "https://api.spacexdata.com/v4/launches/upcoming"

    try:
        # Fetch upcoming launches from the API
        response = requests.get(url)
        response.raise_for_status()

        # Get launch data
        launches = response.json()

        # Sort launches by the 'date_unix' timestamp and pick the soonest
        launches.sort(key=lambda launch: launch['date_unix'])

        # Get the soonest upcoming launch
        upcoming_launch = launches[0]

        # Extract the necessary details
        name = upcoming_launch.get('name')
        date_utc = upcoming_launch.get('date_utc')
        rocket_id = upcoming_launch.get('rocket')
        launchpad = upcoming_launch.get('launchpad')

        # Fetch rocket details using the rocket ID
        rocket_response = requests.get(
            f"https://api.spacexdata.com/v4/rockets/{rocket_id}")
        rocket_response.raise_for_status()
        rocket_data = rocket_response.json()
        rocket_name = rocket_data.get('name')

        # Fetch launchpad details using the launchpad ID
        launchpad_response = requests.get(
            f"https://api.spacexdata.com/v4/launchpads/{launchpad}")
        launchpad_response.raise_for_status()
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get('name')
        launchpad_locality = launchpad_data.get('locality')

        # Convert UTC date to local time
        date_utc_obj = datetime.strptime(date_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
        local_time = date_utc_obj.strftime("%Y-%m-%dT%H:%M:%S%z")

        # Display the information in the required format
        print(f"{name} ({local_time}) {
              rocket_name} - {launchpad_name} ({launchpad_locality})")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
