#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Construct the SQL query and execute it
    query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(query)

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
