#!/usr/bin/python3
'''
This module takes in the name of a state as an argument and
lists all cities of that state
'''
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv
    state = argv[4]

    # connect format (host, user, password, database)
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities\
            WHERE state_id = (SELECT id from states\
            WHERE name = %(state)s)\
            ORDER BY cities.id", {'state': state})
    data = cursor.fetchall()
    cities = list()
    for row in data:
        cities.append(row[0])

    print(', '.join(cities))
    db.close()
