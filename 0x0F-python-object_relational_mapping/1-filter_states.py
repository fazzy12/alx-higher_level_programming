#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()

    # Execute the query to select states starting with 'N' and sort by id
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch and display the results
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]

    # close the cursor and the database connection
    cursor.close()
    db.close()
