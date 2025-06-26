#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    safe_state = state_name.replace("'", "''")

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(safe_state)
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

