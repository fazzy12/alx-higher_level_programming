-- This SQL query retrieves information about TV shows and their associated genres.
-- It uses a LEFT JOIN to include all shows from the 'tv_shows' table, even if they
-- don't have a corresponding entry in the 'tv_show_genres' table. If a show has no
-- genre, the 'tv_show_id' in the 'tv_show_genres' table will be NULL for that record.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;