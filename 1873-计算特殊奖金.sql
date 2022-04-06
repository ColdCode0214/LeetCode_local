/* Write your PL/SQL query statement below */
select e.employee_id,
    (case
    when mod(e.employee_id, 2)=1 and
        e.name not like 'M%' 
    then salary
    else 0
    end) bonus
from Employees e
order by e.employee_id;