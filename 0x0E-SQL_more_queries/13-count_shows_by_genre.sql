-- Task 13
-- Query to import database and use the count function on a table join

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres
JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name IS NOT NULL
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
