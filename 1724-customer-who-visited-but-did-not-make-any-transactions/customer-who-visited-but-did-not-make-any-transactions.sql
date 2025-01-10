# Write your MySQL query statement below
SELECT customer_id, COUNT(v.visit_id) "count_no_trans"
FROM Visits v LEFT JOIN Transactions t USING (visit_id)
WHERE transaction_id is NULL
GROUP BY customer_id