#!/usr/bin/python3
""" This script fetches a url """
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
