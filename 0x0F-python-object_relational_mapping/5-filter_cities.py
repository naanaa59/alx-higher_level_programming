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
    state_name = sys.argv[4]
    query = "SELECT cities.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s"

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    cities = [row[0] for row in rows]
    print(', '.join(cities))

    cursor.close()
    connection.close()
