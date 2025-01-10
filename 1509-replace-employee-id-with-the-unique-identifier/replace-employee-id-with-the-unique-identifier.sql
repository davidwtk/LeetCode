# Write your MySQL query statement below
SELECT unique_id, name FROM EmployeeUNI eu RIGHT OUTER JOIN Employees e ON eu.id = e.id