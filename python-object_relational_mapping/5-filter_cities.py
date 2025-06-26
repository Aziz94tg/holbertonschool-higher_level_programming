#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def filter_cities():
    """
    Lists all cities of a given state from the database
    Takes 4 arguments: mysql username, mysql password, database name and state name
    Results are sorted in ascending order by cities.id
    Safe from MySQL injection by using parameterized queries
    Uses only one execute() call
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
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
    
    # Execute SQL query using JOIN to get cities for the specified state
    # Using parameterized query to prevent SQL injection
    query = """SELECT cities.name FROM cities 
               INNER JOIN states ON cities.state_id = states.id 
               WHERE states.name = %s 
               ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Extract city names and join them with commas
    city_names = [row[0] for row in results]
    print(", ".join(city_names))
    
    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
