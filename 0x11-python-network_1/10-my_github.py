#!/usr/bin/python3
""" Uses the GitHub API to display my id """
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=(user, password))

    print(r.json().get('id'))
