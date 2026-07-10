-- Select the title of the show and the corresponding genre ID
SELECT tv_shows.title, tv_show_genres.genre_id
  -- Use an INNER JOIN to connect the shows to their linked genres
-- This naturally filters out any shows that have no genres assigned
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
