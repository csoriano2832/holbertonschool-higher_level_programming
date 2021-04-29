#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)

    for index in range(len(names)):
        if names[index][:2] != "__":
            print("{:s}".format(names[index]))
