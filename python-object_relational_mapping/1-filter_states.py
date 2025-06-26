#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states():
    """
    Lists all states with a name starting with N from the database
    Takes 3 arguments: mysql username, mysql password and database name
    Results are sorted in ascending order by states.id
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute SQL query to select states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Print results
    for row in results:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
