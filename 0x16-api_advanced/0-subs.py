#!/usr/bin/python3
"""Queries API and returns number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subacribers"""

    header = {'User-Agent': 'Chrome/100.0.4896.88 Mobile Safari/537.36'}

    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    sub = requests.get(url, headers=header)

    if sub.status_code != 200:
        return (0)

    num = sub.json()["data"]["subscribers"]
    return (num)
