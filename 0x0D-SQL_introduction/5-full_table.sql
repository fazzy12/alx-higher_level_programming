-- Execute: mysql -uhbtn_0c_0 -p hbtn_0c_0 < 0x0D-SQL_introduction/5-full_table.sql
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';