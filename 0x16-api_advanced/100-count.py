#!/usr/bin/python3
""" Module that get some subreddit count using recursion """
import requests


def count_words(subreddit, word_list, hot_list_titles=[], after='null'):
    """ returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/hot.json"
    credentials = {'User-Agent': "linux:1:v1.0 (by /u/svelezg_r)"}
    parameters = {"limit": "100", "after": after}
    response = requests.get(url,
                            headers=credentials,
                            params=parameters,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    hot_list_of_dicts = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    """""to print the after string, which acts as a "pointer"
    to the next response uncomment the following line"""
    # print(after)
    hot_list_titles.extend([reddit.get("data").get("title") for
                            reddit in hot_list_of_dicts])
    """to print the length of the hot_list_titles uncomment
    the following line"""
    # print(len(hot_list_titles))

    # after = None
    if after is None:
        to_print_dict = {}
        for word in word_list:
            count = 0
            for title in hot_list_titles:
                split_title = title.split()
                count = count + split_title.count(word)
            if count != 0:
                to_print_dict[word] = count
        for key, value in sorted(to_print_dict.items(),
                                 key=lambda x: (x[1], x[0]),
                                 reverse=True):
            print("{}: {}".format(key, value))

    else:
        return count_words(subreddit, word_list,
                           hot_list_titles, after)
