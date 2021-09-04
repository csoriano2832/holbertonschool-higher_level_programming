#!/usr/bin/python3
""" Gets the 10 newest commits in a repo """
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)

    commits = requests.get(url).json()

    for index in range(0, 10):
        print("{}: {}".format(commits[index].get("sha"),
                              commits[index].get("commit").get("author")
                              .get("name")))
# print(commits[index].get("sha"), end=": ")
# print(commits[index].get("commit").get("author").get("name"))