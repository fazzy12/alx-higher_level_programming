--These queries will alter the character set and collation of the specified database, table, and field, respectively
USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;