-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table states in the database hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT AUTOINCREMENT PRIMARY KEY,
	name VARCHAR(256) IS NOT NULL,
);
