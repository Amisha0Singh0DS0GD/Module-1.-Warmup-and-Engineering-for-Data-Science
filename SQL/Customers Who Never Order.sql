# Write your MySQL query statement below
WITH t AS (SELECT name,o.id
FROM Customers c
LEFT JOIN Orders o
ON c.id=o.customerId)
SELECT name AS Customers
FROM t
WHERE id IS NULL