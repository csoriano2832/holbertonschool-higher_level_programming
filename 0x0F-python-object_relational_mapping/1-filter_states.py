#!/usr/bin/python3
''' This module lists all states with a name starting with N '''
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv

    # connect format (host, user, password, database)
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
            ORDER BY id")
    data = cursor.fetchall()
    for row in data:
        print(row)

    db.close()
