#!/usr/bin/python3
'''
This module lists all states where name matches with the argument
Safe from MySQL injections
'''
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv
    pattern = argv[4]

    # connect format (host, user, password, database)
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %(pattern)s\
            ORDER BY id", {'pattern': pattern})
    data = cursor.fetchall()
    for row in data:
        print(row)

    db.close()
