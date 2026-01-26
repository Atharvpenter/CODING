# Creating Simple Database and Table
# Using Primary key
show databases;
use ap;
create table Student(
	id int primary key,
    Fname varchar(20) not null,
    Mname varchar(20),
    Lname varchar(20) not null,
    age int unsigned,
    address varchar(20) not null
);
insert into Student(id,Fname,Mname,Lname,age,address) values(1,'Atharv','Avinash','Penter',22,'Pune');
insert into Student(id,Fname,Mname,Lname,age,address) values(2,'Atharva','Ravindra','Kandekar',23,'Pune');
insert into Student(id,Fname,Mname,Lname,age,address) values(3,'Kunal','Anil','Sangle',23,'Pune');
insert into Student(id,Fname,Mname,Lname,age,address) values(4,'Akhil','Ashok','Berad',23,'Pune');
insert into Student(id,Fname,Mname,Lname,age,address) values(5,'Kshitij','Harishchandra','Gade',24,'Pune');
select * from Student;

#### Using Auto_increment 
create table auto_incre(
	id int primary key auto_increment,
    name varchar(20) not null,
    age int unsigned
);
insert into auto_incre(id,name,age) values(1,'ram',22);
insert into auto_incre(name,age) values('ram',22);
insert into auto_incre(id,name,age) values(3,'ram',22);
select * from auto_incre;

#### Adding columns in auto_incre
alter table auto_incre add address varchar(20) not null default'pune';
select * from auto_incre;

#### Using timestamp ----->
create table class(
	student_id int auto_increment,
    student_fname varchar(20) not null,
    student_mname varchar(20),
    student_lname varchar(20) not null,
    student_email varchar(20) not null,
    student_phone varchar(15) not null,
    student_alternate_phone int,
    enrollment_date timestamp not null,
    year_of_exp int not null,
    student_company varchar(10) not null,
    batch_date varchar(20) not null,
    source_of_joining varchar(20),
    location varchar(20) not null,
    primary key(student_id),
	unique key(student_email)
);
describe class;
insert into class 
(student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('virat', 'kohli','virat@gmail.com', '9292929292', 3, 'flipkart', '5-02-2021','linkedin', 'hyderabad',now());
insert into class 
(student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('kapil', 'dev','kapil@gmail.com', '9291292292', 15, 'microsoft', '5-02-2021','friend', 'pune',now());
insert into class 
(student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('brian', 'lara', 'brian@gmail.com', '9291297292', 18, 'tcs','5-02-2021', 'youtube', 'pune',now());
insert into class 
(student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('carl', 'hooper', 'carl@gmail.com', '9291297392', 20, 'wipro','19-02-2021', 'youtube', 'pune',now());
insert into class 
(student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('saurabh', 'ganguly', 'saurabh@gmail.com', '9291297492', 14,'wipro', '19-02-2021', 'google', 'chennai',now());
select * from class;

#### creating another table to match the upper table
create table course(
	course_id int auto_increment,
    course_name varchar(20) not null,
    course_duration int(20) not null,
    course_fee int (20) not null default'200000',
    primary key(course_id)
);
insert into course(course_name,course_duration)values('Data Science', 3);
insert into course(course_name,course_duration)values('Data Analysis', 6);
insert into course(course_name,course_duration)values('Big data', 4);
insert into course(course_name,course_duration)values('Machine learning', 3);
insert into course(course_name,course_duration)values('Full stack', 6);
--  Merging both tables --
select * from class,course;
set sql_safe_updates = 0;  -- when it is 0 table can be modified.


#---------------- Using Serveral Conditions in MySQL ------------------------------------------
# INNER JOINT , OUTER JOINT , RIGHT JOIN , LEFT JOIN , FULL JOIN 
# WHERE , IN , BETWEEN 
# GROUPBY :- COUNT , SUM , AVG , MIN , MAX , ORDER BY , DISTINCT
# ROW , RANK() , DENSE_RANK()

-- Using where, having condition
use ap;
select * from class,course;
select * from class where student_fname = 'virat';
select source_of_joining, count(*) as total from class group by source_of_joining having total>1;

-- Using Count() condition checks the total number of records in the table
select count(*) from class;  
-- Using Count() condition to check specific columns records
select count(student_company) from class;
select count(distinct location) from class; 

-- Using group by condition
select source_of_joining from class group by source_of_joining ;
-- count of student from different locations and name of location
select location, count(*) from class group by location;
-- count of student by location and source_of_joining... location and source_of_joining unique combination --- count
select location, source_of_joining, count(*) from class group by location,source_of_joining;
select student_company, location , count(*) from class group by student_company, location;

-- Using MIN,MAX,SUM,AVG conditions
select max(year_of_exp) from class;
select min(year_of_exp) from class;
select sum(year_of_exp) from class;
select avg(year_of_exp) from class;
select distinct student_company from class;

-- types of joins ->
-- 1. Inner join -> Returns only the rows that have matching values in both tables.
-- 2. Left join -> Returns all rows from the left table, plus the matching rows from the right table.
-- 3. Right join -> Returns all rows from the right table, plus the matching rows from the left table
-- 4. Full join -> Returns all rows from both tables.
-- Using join to combine two tables
select * from class,course;
select student_fname,student_mname,student_lname,student_email,student_phone,student_company,course_name,course_fee from class join course;
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class INNER JOIN course ON course_id = course_id;
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class left JOIN course ON course_id = course_id;
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class right JOIN course ON course_id = course_id;
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class full JOIN course ON course_id = course_id;

# ROW , RANK() , DENSE_RANK()
SELECT course_name,course_fee,RANK() OVER (ORDER BY course_fee DESC) AS course_rank FROM course;
SELECT course_name,course_fee,DENSE_RANK() OVER (ORDER BY course_fee DESC) AS course_dense_rank FROM course;