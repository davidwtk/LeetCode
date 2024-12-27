# Write your MySQL query statement below
SELECT D.Name as "Department", E.Name as "Employee", salary as "Salary"
FROM Employee E JOIN Department D 
ON E.DepartmentId = D.Id 
WHERE (DepartmentId,Salary) IN
(
    SELECT DepartmentId, MAX(Salary) 
    FROM Employee 
    GROUP BY DepartmentId
)