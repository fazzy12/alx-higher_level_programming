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
    query = "SELECT * FROM `cities` as `c` INNER JOIN `states` as `s` ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id`"
    
    print(", ".join([ct[2] for ct in cursor.fetchall() if ct[4] == state_name]))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
