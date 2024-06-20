#!/usr/bin/python3
"""
0-subs.py
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:requests (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    data = response.json().get('data', {})
    return data.get('subscribers', 0)
