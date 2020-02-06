#!/usr/bin/python3
"""
Module that get some information about the subscribers of anAPI.

"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers for a subreddit.

    Subreddit is passed as an argument.
    If the subreddit is not valid, 0 is returned.
    """
    # set variables
    request_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent':
               'chrome:number_of_subscribers_function:v1 (by /u/remyjuke)'}

    response = requests.get(request_url,
                            headers=headers,
                            allow_redirects=False)

    response_code = response.status_code
    if (response_code >= 300):
        return 0

    subscriber_count = response.json().get("data").get("subscribers")
    return subscriber_count


if __name__ == "__main__":
    number_of_subscribers("all")
    number_of_subscribers("fake_subreddit")
