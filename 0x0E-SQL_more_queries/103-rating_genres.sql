-- Task 20
-- Query that uses multiple tables with Group by clause

SELECT tv_genres.name AS 'name', SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_genres
JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings
	ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY name
ORDER BY rating DESC;
