-- MySQL
-- runtime: 163 ms
-- Memory: 0 B
SELECT *
FROM cinema
WHERE id % 2 = 1 and description != "boring"
ORDER BY rating DESC;
