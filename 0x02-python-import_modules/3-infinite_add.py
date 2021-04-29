#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    total = 0

    if argc == 0:
        print(total)
    else:
        for index in range(1, (argc + 1)):
            total += int(argv[index])
        print(total)
