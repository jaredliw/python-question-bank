-- MySQL
-- Runtime: 577 ms
-- Memory: 0 B
SELECT Name AS "Customers"
FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE CustomerId IS null;
