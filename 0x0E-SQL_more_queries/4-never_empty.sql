-- Create a table named id_not_null. This table should have:
-- An id column that cannot be null and must have a default value of 1
-- A name column that can be null
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);