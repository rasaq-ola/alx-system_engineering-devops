#!/usr/bin/python3
"""
100-count.py
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:requests (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')
    
    for post in children:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title.split():
                word_count[word_lower] = word_count.get(word_lower, 0) + title.split().count(word_lower)
    
    if after is None:
        if not word_count:
            return
        
        sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
        return
    
    return count_words(subreddit, word_list, word_count, after)
