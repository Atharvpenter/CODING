-- Distinct is used to remove duplicate rows. and also common elements.
-- Order is used to sort the result set using one or more columns.


use atharv;
show tables;
select * from student;
select student_fname,enrollment_date,year_of_exp,source_of_joining from student;
select distinct student_company from student;
select distinct source_of_joining from student limit 5;