#!/usr/bin/python3
""" This module fetches a particular header """
import urllib.request
import sys


if __name__ == "__main__":
    """ Only executes as main """
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
