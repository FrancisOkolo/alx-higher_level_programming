-- Task 6
-- Query to create database and a table in it.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
