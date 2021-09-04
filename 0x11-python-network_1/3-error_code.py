#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response """
from urllib.error import HTTPError
import urllib.request
import sys


if __name__ == "__main__":
    """ Only executes as main """

    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        print(html.decode('utf-8'))
