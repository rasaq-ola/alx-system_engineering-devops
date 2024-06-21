#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:requests (by /u/yourusername)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get('data', {})
    except ValueError:
        print(None)
        return

    children = data.get('children', [])

    if not children:
        print(None)
        return

    for post in children[:10]:
        print(post.get('data', {}).get('title', ''))
