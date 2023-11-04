#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Construct the SQL query with placeholders and execute it safely
    query = "SELECT * FROM states WHERE name=%s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
