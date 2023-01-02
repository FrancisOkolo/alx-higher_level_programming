-- Task 7
-- Query to create a database with a table of special field.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	FOREIGN KEY(state_id) REFERENCES states(id) ON DELETE CASCADE,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL
	);


