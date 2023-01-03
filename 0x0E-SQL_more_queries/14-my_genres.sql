-- Task 14
-- query to get some data by multiple jonins

SELECT tv_genres.name AS 'name'
FROM tv_genres
JOIN tv_show_genres
	ON tv.genres.id = tv_show_genres.genre_id
JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
