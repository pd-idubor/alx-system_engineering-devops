#!/usr/bin/python3
"""Count of words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, insts={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Chrome/100.0.4896.88"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if insts.get(word) is None:
                    insts[word] = times
                else:
                    insts[word] += times

    if after is None:
        if len(insts) == 0:
            print("")
            return
        insts = sorted(insts.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in insts]
    else:
        count_words(subreddit, word_list, insts, after, count)
