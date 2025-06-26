#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1], sys.argv[2],\
            sys.argv[3], sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()

    # Safe SQL query using parameterized input (no SQL injection)
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    # Format output as comma-separated list
    print(", ".join([city[0] for city in results]))

    cursor.close()
    db.close()
