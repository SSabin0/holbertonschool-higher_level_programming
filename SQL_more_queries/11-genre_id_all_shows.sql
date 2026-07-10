-- List all shows, including those without a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- LEFT JOIN ensures all records from tv_shows are kept
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Sort by title then genre_id as requested
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
