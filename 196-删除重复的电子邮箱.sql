/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 */
delete 
from person
where id in(
    select id
    from(
        select id, 
            row_number() over(partition by email order by id) rn 
        from person
    )t1
    where rn>1
) ;

