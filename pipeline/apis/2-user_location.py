#!/usr/bin/env python3
"""
Fetches and prints the location of a GitHub user
Handles rate limits and non-existing users
"""

import requests
import sys
import time
from datetime import datetime


def get_user_location(url):
    """
    Fetches the location of the user from the GitHub API URL provided

    Args:
        url (str): The GitHub API URL for the user

    Returns:
        str: The location of the user, or appropriate message if
             the user is not found or if rate limits are exceeded
    """
    response = requests.get(url)

    # Check if user was found
    if response.status_code == 404:
        return "Not found"

    # Check for rate limit
    if response.status_code == 403:
        reset_timestamp = int(response.headers.get('X-RateLimit-Reset'))
        current_time = int(time.time())
        reset_in_seconds = reset_timestamp - current_time
        reset_in_minutes = reset_in_seconds // 60  # Convert seconds to minutes
        return f"Reset in {reset_in_minutes} min"

    # Check if the user exists and extract location
    if response.status_code == 200:
        user_data = response.json()
        print(user_data)  # Debugging: Print the response JSON to check its structure
        location = user_data.get('location', 'No location available')
        return location

    return "Error: Unable to fetch data"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the GitHub user API URL")
    else:
        url = sys.argv[1]
        location = get_user_location(url)
        print(location)
