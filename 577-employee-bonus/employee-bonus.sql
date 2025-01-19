# Write your MySQL query statement below
SELECT name, bonus
FROM Employee e LEFT JOIN bonus b
ON e.empId = b.empId
WHERE IFNULL(bonus, 0) < 1000