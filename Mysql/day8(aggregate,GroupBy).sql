show databases;
use atharv;
show tables;
select * from student;
-- Aggregate function is used to perform calculations.

select student_fname,batch_date,source_of_joining,location from student;
select count(*) from student;
select count(student_company) from student;
select count(distinct location) from student;

-- GroupBY
select source_of_joining, count(*) from student group by source_of_joining;
-- count of student from different locations and name of location
select location, count(*) from student group by location;

-- count of student by location and source_of_joining... location and source_of_joining unique combination --- count
select location,source_of_joining,count(*) from student group by location, source_of_joining;

-- MAX 
select max(year_of_exp) from student;

-- MIN
select min(year_of_exp) from student;

-- SUM
select sum(year_of_exp) from student;

-- AVG
select avg(year_of_exp) from student;

