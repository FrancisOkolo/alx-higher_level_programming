-- Task 15
-- Query to determine number of ocuurence of records
SELECT score, COUNT(score) AS 'number'
FROM second_table
ORDER BY 'number' DESC;
