-- MySQL
-- Runtime: 316 ms
-- Memory: 0 B
SELECT name, population, area
FROM world
WHERE area > 3000000 OR population > 25000000;
