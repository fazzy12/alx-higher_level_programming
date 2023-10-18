-- This SQL query retrieves information about TV shows and their associated genres.
-- It uses a LEFT JOIN to include all shows from the 'tv_shows' table, even if they
-- don't have a corresponding entry in the 'tv_show_genres' table. If a show has no
-- genre, the 'tv_show_id' in the 'tv_show_genres' table will be NULL for that record.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
