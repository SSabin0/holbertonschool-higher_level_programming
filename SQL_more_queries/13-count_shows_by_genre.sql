-- Select genre name and count the occurrences of linked shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
-- Use INNER JOIN to automatically exclude genres with 0 shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group the results by genre name to prepare for the count
GROUP BY genre
-- Sort by the calculated count in descending order
ORDER BY number_of_shows DESC;
