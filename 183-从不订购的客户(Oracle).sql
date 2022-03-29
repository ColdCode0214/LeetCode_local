/* Write your PL/SQL query statement below */
select c.name as customers
from customers c
where c.id not in(
    select o.customerid
    from orders o
);