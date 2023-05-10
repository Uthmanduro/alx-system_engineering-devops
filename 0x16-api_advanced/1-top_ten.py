#!/usr/bin/python3
"""prints the titles of thf the first 10 hot posts listed """
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Badoo"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    datas = res.json().get("data")
    if not datas:
        print(None)
    for items in datas.get("data").get("children"):
        if items.get("data") and items.get("data").get("title"):
            print(items.get("data").get("title"))
    print(None)
