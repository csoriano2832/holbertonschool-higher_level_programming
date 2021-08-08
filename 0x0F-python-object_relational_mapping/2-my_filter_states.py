#!/usr/bin/python3
''' This module lists all states where name matches with the argument '''
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv
    pattern = argv[4]

    # connect format (host, user, password, database)
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}'".format(pattern))
    data = cursor.fetchall()
    for row in data:
        print(row)

    db.close()
