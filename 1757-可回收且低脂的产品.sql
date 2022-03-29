/* Write your PL/SQL query statement below */
select P.product_id
from Products P
where P.low_fats='Y' and P.recyclable='Y';