#!/usr/bin/python3
"""Recursion to query the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a liat of titles of all articles for a subreddit"""
    header = {'User-Agent':  'Chrome/100.0.4896.88'}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
            "after": after,
            "count": count,
            "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
