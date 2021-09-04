#!/usr/bin/python3
""" Sends a POST request to a URL with a letter as parameter """
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json = r.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
