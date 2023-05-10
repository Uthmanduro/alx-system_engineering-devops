#!/usr/bin/python3
"""runs the function printing the number of subscriber for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    data = res.json().get('data')
    if not data:
        return 0
    return (data.get('subscribers'))
