#!/usr/bin/python3
"""
    This script lists all cities from database hbtn_0e_4_usa
    This script lists all cities from database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                                 password=sys.argv[2], database=sys.argv[3])
    cursor = connection.cursor()

    table = "cities"
    query = "SELECT * FROM {}".format(table)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
