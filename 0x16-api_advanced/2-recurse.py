#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for
a given subreddit. If no results are found for the given subreddit,
the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """prints the titles of the first 10 hot posts listed for
    a given subreddit"""
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
            hot_list.extend([post['data']['title'] for post in posts])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None
