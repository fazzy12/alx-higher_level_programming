-- This query selects the title from the tv_shows table and genre_id 
-- from the tv_show_genres table. It then uses the JOIN clause to combine
-- rows from both tables based on the id in tv_shows matching the show_id 
-- in tv_show_genres. The results are sorted in ascending order by title and genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
