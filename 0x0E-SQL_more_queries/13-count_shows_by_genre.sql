-- Task 13
-- Query to import database and use the count function on a table join
SELECT tv_genres.name AS 'genre', tv_show_genres.genre_id AS 'number_of_shows'
FROM tv_genres
JOIN tv_show_genres
	ON tv.genres.id = tv_show_genre.genre_id
WHERE tv_genre.name IS NOT NULL
GROUP BY COUNT(tv_show.genre.id)
ORDER BY tv_show.genre.id DESC;
