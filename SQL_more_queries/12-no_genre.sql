-- Select title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
-- Join tables, keeping all shows from the left
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Filter for shows without a linked genre
WHERE tv_show_genres.genre_id IS NULL
-- Sort the results
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
