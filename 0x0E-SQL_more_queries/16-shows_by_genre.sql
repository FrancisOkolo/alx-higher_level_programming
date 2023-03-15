-- Task 16
-- Query to show all tv shows and their genres
-- Where a show doesn't have a genre the value should be NULL

SELECT tv_shows.title AS 'title', tv_genres.name AS 'name'
FROM tv_shows
LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
