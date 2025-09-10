use atharv;
show tables;
select * from employee_over;
select row_number() over (order by salary desc) as rownum , firstname, lastname, salary  from employee_over;
select * from (select firstname, lastname, salary , row_number() over (order by salary desc) as rownum from employee_over) as temptable 
where rownum=1;
select rank() over (order by location desc) as ranknum , firstname, lastname, salary , location from employee_over;
select dense_rank() over (order by salary desc) as dranknum , firstname, lastname, salary , location from employee_over;