-- Create force_name table in the database with id and non-null name field
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
);