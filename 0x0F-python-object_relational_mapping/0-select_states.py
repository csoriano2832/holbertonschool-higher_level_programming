#!/usr/bin/python
''' This module lists all states from a database '''
import sys
import MySQLdb


if __name__ == "__main__":
    # Save argument list to variable
    argv = sys.argv

    # Open database connection
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    # Fetch and print all rows
    data = cursor.fetchall()
    for row in data:
        print(row)

    # Disconnect from server
    db.close()
