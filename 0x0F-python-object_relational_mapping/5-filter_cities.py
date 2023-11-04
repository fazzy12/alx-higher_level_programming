#!/usr/bin/python3
"""script that takes the name of a state as an argument
and lists all cities of that state from the hbtn_0e_4_usa"""

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
    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities JOIN\
        states ON cities.state_id = states.id\
            WHERE states.name=%s ORDER BY cities.id"
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    result = cursor.fetchone()
    if result:
        print(result[0])

    # Close the cursor and the database connection
    cursor.close()
    db.close()
