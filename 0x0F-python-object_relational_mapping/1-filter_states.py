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
    results = cursor.fetchall()
    if row == "N":
        for row in results:
            print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
