#!/usr/bin/env python3
"""
Script that prints the location of a GitHub user
passed as the first argument
"""

import requests
from sys import argv
from time import time

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        exit(1)

    try:
        url = argv[1]
        results = requests.get(url)

        # Handle 403 (Rate limit exceeded)
        if results.status_code == 403:
            reset = results.headers.get('X-RateLimit-Reset')
            wait_time = int(reset) - time()
            minutes = round(wait_time / 60)
            print('Reset in {} min'.format(minutes))

        # Handle 404 (User not found)
        elif results.status_code == 404:
            print('Not found')

        # Handle 200 (Success)
        else:
            results = results.json()
            location = results.get('location')
            if location:
                print(location)
            else:
                print('Not found')

    except Exception as err:
        print('Not found')
