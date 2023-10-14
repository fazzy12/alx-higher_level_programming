!["Logo Title Text 1"](rtcwz.jpg)

# SQL Introduction Project

## Overview

This repository contains SQL scripts for a project focused on SQL introduction and database management. The tasks cover foundational concepts in SQL, and each script addresses specific operations on a MySQL database.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Task Descriptions](#task-descriptions)
- [Author](#author)
- [License](#license)

## Prerequisites

To execute the SQL scripts, you need:

- MySQL 8.0 installed
- Ubuntu 20.04 LTS operating system

### Installing MySQL on Ubuntu

1. Update the package list:

   ```bash
   sudo apt update
   ```

2. Install MySQL Server:

   ```bash
   sudo apt install mysql-server
   ```

3. Check the installed version:

   ```bash
   mysql --version
   ```

### Connecting to MySQL Server

- Connect via terminal:

  ```bash
  sudo mysql
  ```

- Connect via a MySQL client or use "container-on-demand" as specified in the tasks.

Make sure to follow the installation instructions for MySQL provided in the tasks.

## Project Structure

- **`0x0D-SQL_introduction/`**: Main project directory.
  - **`0-list_databases.sql`**: Script to list all databases.
  - **`1-create_database_if_missing.sql`**: Script to create a database if it doesn't exist.
  - **`2-remove_database.sql`**: Script to delete a database if it exists.
  - **`3-list_tables.sql`**: Script to list all tables in a specified database.
  - **`4-first_table.sql`**: Script to create a table named `first_table`.
  - **`5-full_table.sql`**: Script to print the full description of the `first_table`.
  - **`6-list_values.sql`**: Script to list all rows of `first_table`.
  - **`7-insert_value.sql`**: Script to insert a new row in `first_table`.
  - **`8-count_89.sql`**: Script to display the number of records with `id = 89` in `first_table`.
  - **`9-full_creation.sql`**: Script to create a table named `second_table` and add multiple rows.
  - **`10-top_score.sql`**: Script to list all records of `second_table` ordered by score.
  - **`11-best_score.sql`**: Script to list records with a score >= 10 in `second_table`.
  - **`12-no_cheating.sql`**: Script to update the score of Bob to 10 in `second_table`.
  - **`13-change_class.sql`**: Script to remove records with a score <= 5 in `second_table`.
  - **`14-average.sql`**: Script to compute the score average of all records in `second_table`.
  - **`15-groups.sql`**: Script to list the number of records with the same score in `second_table`.
  - **`16-no_link.sql`**: Script to list all records of `second_table` without rows without a name value.
  - **`100-move_to_utf8.sql`**: Script to convert the database and tables to UTF8.
  - **`101-avg_temperatures.sql`**: Script to display the average temperature by city.
  - **`102-top_city.sql`**: Script to display the top 3 cities' temperatures during July and August.
  - **`103-max_state.sql`**: Script to display the max temperature of each state.

## How to Use

1. Clone the repository:

   ```
   git clone [https://github.com/fazzy12/alx-higher_level_programming/0x0D-SQL_introduction]
   ```

2. Navigate to the project directory:

   ```
   cd 0x0D-SQL_introduction
   ```

3. Execute the SQL scripts using the provided commands.

## Task Descriptions

1. **List Databases (`0-list_databases.sql`):**

   - Lists all databases on the MySQL server.

2. **Create Database If Missing (`1-create_database_if_missing.sql`):**

   - Creates the `hbtn_0c_0` database if it doesn't exist.

3. **Delete Database (`2-remove_database.sql`):**

   - Deletes the `hbtn_0c_0` database if it exists.

4. **List Tables (`3-list_tables.sql`):**

   - Lists all tables in a specified database.

5. **First Table (`4-first_table.sql`):**

   - Creates a table named `first_table` with specified columns.

6. **Full Table Description (`5-full_table.sql`):**

   - Prints the full description of `first_table`.

7. **List All Rows (`6-list_values.sql`):**

   - Lists all rows of `first_table`.

8. **Insert New Row (`7-insert_value.sql`):**

   - Inserts a new row in `first_table`.

9. **Count Records (`8-count_89.sql`):**

   - Displays the number of records with `id = 89` in `first_table`.

10. **Full Creation (`9-full_creation.sql`):**

    - Creates a table named `second_table` and adds multiple rows.

11. **Top Scores (`10-top_score.sql`):**

    - Lists all records of `second_table` ordered by score.

12. **Best Scores (`11-best_score.sql`):**

    - Lists records with a score >= 10 in `second_table`.

13. **No Cheating (`12-no_cheating.sql`):**

    - Updates the score of Bob to 10 in `second_table`.

14. **Remove Low Scores (`13-change_class.sql`):**

    - Removes records with a score <= 5 in `second_table`.

15. **Average Score (`14-average.sql`):**

    - Computes the score average of all records in `second_table`.

16. **Number by Score (`15-groups.sql`):**

    - Lists the number of records with the same score in `second_table`.

17. **No Link (`16-no_link.sql`):**

    - Lists all records of `second_table` without rows without a name value.

18. **Convert to UTF8 (`100-move_to_utf8.sql`):**

    - Converts the database and tables to UTF8.

19. **Average Temperatures (`101-avg_temperatures.sql`):**

    - Displays the average temperature by city.

20. **Top City Temperatures (`102-top_city.sql`):**

    - Displays the top 3 cities' temperatures during July and August.

21. **Max State Temperatures (`103-max_state.sql`):**
    - Displays the max temperature of each state.

## Author

- [Ifeanyi Kalu](http://github.com/fazzy12)

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
