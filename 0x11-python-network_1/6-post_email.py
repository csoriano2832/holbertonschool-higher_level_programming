#!/usr/bin/python3
""" Sends a POST request to the passed URL with email as parameter """
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(url, data={'email': email})
    print(r.text)
