-- Select the title of the show
SELECT tv_shows.title
-- Start with shows and link them to the bridge
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Link the bridge to the genres table
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filter only for Comedy
WHERE tv_genres.name = 'Comedy'
-- Sort the results alphabetically
ORDER BY tv_shows.title ASC;
