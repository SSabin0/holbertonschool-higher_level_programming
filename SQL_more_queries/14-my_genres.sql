-- Select the genre name
SELECT tv_genres.name
-- Start with the genres table and join the bridge and show tables
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filter specifically for the title 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Sort the list alphabetically
ORDER BY tv_genres.name ASC;
