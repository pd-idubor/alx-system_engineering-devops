#!/usr/bin/python3
"""Recursive function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list for all the hot articles for the given subreddit"""

    header = {'User-Agent': 'Chrome/100.0.4896.88 Mobile Safari/537.36'}
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    params = {
            "after": after,
            "count": count,
            }
    sub = requests.get(url, headers=header, params=params,
                       allow_redirects=False)

    if sub.status_code != 200:
        return (None)

    else:
        data = sub.json()["data"]
        after = data["after"]
        count += data["dist"]

        for hot in data["children"]:
            hot_list.append(hot["data"]["title"])

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return (hot_list)
