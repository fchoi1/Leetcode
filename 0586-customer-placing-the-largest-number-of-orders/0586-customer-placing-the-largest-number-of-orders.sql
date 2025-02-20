# Write your MySQL query statement below

with c as (select customer_number, COUNT(*) from Orders group by customer_number order by COUNT(*) DESC)

select c.customer_number from c limit 1