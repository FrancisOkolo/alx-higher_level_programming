-- Task 8
-- searching for data using nested queries
SELECT id, name 
FROM cities
WHERE state_id =
	(SELECT id FROM states WHERE name = 'California')
GROUP BY id
ORDER BY id;
