#!/usr/bin/python3
""" function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0 """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (compatible; my-reddit-bot/1.0; '
            '+https://www.example.com/bot)'
        )
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
