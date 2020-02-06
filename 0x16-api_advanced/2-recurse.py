#!/usr/bin/python3
"""
Module that get some results of an API using recursion.
"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """Find hot subreddit article titles using recursion"""
    payload = {}

    baseURL = "https://www.reddit.com/r/"
    url = baseURL + subreddit + "/hot/.json?limit=100"

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '214 at Holberton'
    }
    result = requests.get(url, headers=headers, params=params)
    title = []
    if result.status_code == 200:
        result = result.json()
        children = result.get('data').get('children')
        nChildren = len(children)
        for i in range(nChildren):
            if children[i].get('data').get('title'):
                title.append(children[i].get('data').get('title'))
                hot_list.append(title)
            else:
                return
        after = result.get('data').get('after')
        if after is None:
            return hot_list
        else:
            payload = {"after": after}
            recurse(subreddit, hot_list, payload)
            return hot_list
    else:
        return None
