#!/usr/bin/python3
"""Number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in a subreddit"""

    header = {'User-Agent':  'Chrome/100.0.4896.88'}
    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        sub = response.json()["data"]["subscribers"]
    else:
        sub = 0
    return sub
