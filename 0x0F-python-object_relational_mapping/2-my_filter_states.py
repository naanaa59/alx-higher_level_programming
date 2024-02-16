#!/usr/bin/python3
"""
    This script takes in an argument and displays
    all values in the states tables
"""
import MySQLdb
import sys

if __name__ == "__main__":

    connection = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                                 password=sys.argv[2], database=sys.argv[3])
    cursor = connection.cursor()

    table = "states"
    column = sys.argv[4]
    query = "SELECT * FROM {} WHERE name = %s ORDER BY id".format(table)

    cursor.execute(query, (column,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
