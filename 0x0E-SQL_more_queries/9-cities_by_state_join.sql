-- Task 9
-- Query to join two tables
SELECT cities.id, cities.name, states.name
FROM states
JOIN cities
	ON states.id = cities.state_id
ORDER BY cities.id;
