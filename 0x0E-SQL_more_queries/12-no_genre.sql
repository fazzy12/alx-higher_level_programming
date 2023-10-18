-- This query uses a LEFT JOIN to retrieve information about
-- TV shows and their associated genre IDs. 
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
        LEFT JOIN tv_show_genres 
        ON tv_shows.id = tv_show_genres.tv_show_id
            WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
