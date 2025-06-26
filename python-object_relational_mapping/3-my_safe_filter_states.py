#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This version is safe from MySQL injections!
"""

import MySQLdb
import sys


def safe_filter_states():
    """
    Displays all values in the states table where name matches the argument
    Takes 4 arguments: mysql username, mysql password, database name and state name
    Results are sorted in ascending order by states.id
    Safe from MySQL injection by using parameterized queries
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    
    cursor = db.cursor()
    
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
