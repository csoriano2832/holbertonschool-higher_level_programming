#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
        print("{:d}: {:s}".format(argc, argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for index in range(1, (argc + 1)):
            print("{:d}: {:s}".format(index, argv[index]))
