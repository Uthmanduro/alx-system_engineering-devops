#!/usr/bin/python3
"""prints the titles of thf the first 10 hot posts listed """
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "ew Badoo"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        datas = res.json().get("data").get("children")
        if datas:
            for items in datas:
                print(items.get("data").get("title"))
    else:
        print(None)
