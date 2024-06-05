#!/usr/bin/python3
"""
Recursive function to count occurrences of
specified words in hot articles of a subreddit.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count occurrences of specified
    words in hot articles of a subreddit"""
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (compatible; my-reddit-bot/1.0; '
            '+https://www.example.com/bot)'
        )
    }
    params = {
        'limit': 100,
        'after': after
    }

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        counts[word.lower()] = counts.get(
                                word.lower(), 0) + title.count(word.lower())
            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, counts)
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
        elif response.status_code == 404:
            return
    except requests.RequestException:
        return
