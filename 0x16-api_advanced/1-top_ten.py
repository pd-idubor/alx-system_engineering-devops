#!/usr/bin/python3
"""Queries API and prints titles of hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""

    header = {'User-Agent': 'Chrome/100.0.4896.88 Mobile Safari/537.36'}

    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    sub = requests.get(url, headers=header)

    if sub.status_code != 200:
        print("None")

    limit = 10
    data = sub.json()["data"]["children"]
    for hot in data:
        if limit < 1:
            break
        print(hot["data"]["title"])
        limit -= 1
