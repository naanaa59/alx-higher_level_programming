#!/usr/bin/python3
"""
    This lists all states from database hbtn_0e_0_usa
    This lists all states from database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    connection = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                                 password=sys.argv[2], database=sys.argv[3])
    cursor = connection.cursor()

    table = "states"
    query = f"SELECT * FROM {table} ORDER BY id"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
