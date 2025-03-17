#!/usr/bin/env python3
"""
Script that prints the location of a GitHub user
passed as the first argument
"""

import sys
import requests
from datetime import datetime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)

        # Handle 403 (Rate limit exceeded)
        if response.status_code == 403:
            # Get the reset timestamp from headers
            reset_timestamp = response.headers.get('X-RateLimit-Reset')

            if reset_timestamp:
                # Convert timestamp to int
                reset_timestamp = int(reset_timestamp)

                # Get current time
                now_timestamp = int(datetime.now().timestamp())

                # Calculate the minutes remaining until reset
                minutes_remaining = (reset_timestamp - now_timestamp) // 60

                print(f"Reset in {minutes_remaining} min")
            else:
                print("Rate limit exceeded. No reset info found")

        # Handle 404 (User not found)
        elif response.status_code == 404:
            print("Not found")

        # Handle 200 (Success)
        elif response.status_code == 200:
            user_data = response.json()
            location = user_data.get('location')

            if location:
                print(location)
            else:
                print("No location found")

        # Other cases
        else:
            print(
                f"Error: Received unexpected status code {
                    response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
