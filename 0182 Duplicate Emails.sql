-- MySQL
-- Runtime: 296 ms
-- Memory: 0 B
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1;
