#!/usr/bin/python3
""" This script fetches a url """
import requests


if __name__ == "__main__":
    """ Only executes as main """
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
