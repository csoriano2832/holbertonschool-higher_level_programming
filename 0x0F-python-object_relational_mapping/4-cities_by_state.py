#!/usr/bin/python3
''' This module lists all cities from a database '''
import sys
import MySQLdb


if __name__ == "__main__":
    argv = sys.argv

    # connect format (host, user, password, database)
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM states INNER JOIN cities\
            ON states.id = cities.state_id\
            ORDER BY id")
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
