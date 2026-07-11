-- Select the title and the genre name
SELECT tv_shows.title, tv_genres.name
-- Start with all shows
FROM tv_shows
-- Left join the bridge table to keep all shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Left join the genres table to get the names
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Sort by title then genre name as requested
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
