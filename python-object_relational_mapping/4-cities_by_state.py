#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
along with their corresponding state names.

Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=db_name
    )
    cursor = db.cursor()

    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

