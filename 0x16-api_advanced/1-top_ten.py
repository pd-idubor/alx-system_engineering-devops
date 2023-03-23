#!/usr/bin/python3
"""Top Ten Titles"""
import requests


def top_ten(subreddit):
    """Prints the title of the ten posts of a subreddit"""

    header = {'User-Agent':  'Chrome/100.0.4896.88'}
    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    param = {
        "limit": 10
    }
    response = requests.get(url, headers=header, params=param,
                            allow_redirects=False)
    if response.status_code == 200:
        h_list = response.json()["data"]["children"]
        for hot in h_list:
            print(hot["data"]["title"])
    else:
        print("None")
