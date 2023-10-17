--  creates the MySQL server user user_0d_1.
--  user_0d_1 will have all privileges on your MySQL server.
--  The user_0d_1 password will be set to user_0d_1_pwd.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;