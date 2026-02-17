# creating a new database
show databases;
create database revision;
use revision;

# creating new table using primary key in database
create table Student(
	id int primary key,
	fname varchar(10) not null,
    mname varchar(10),
    lname varchar(10) not null,
    age int,
    address varchar(20) default "pune",
    email varchar(20) not null,
    phone varchar(15) not null
);
insert into Student(id,fname,mname,lname,age,address,email,phone) values(1,"atharv","avinash","penter",22,"pune","atharv@gmail.com",7083534353);
insert into Student(id,fname,mname,lname,age,address,email,phone) values(2,"atharva","ravi","kandekar",23,"pune","atharva@gmail.com",7083534353);
insert into Student(id,fname,mname,lname,age,address,email,phone) values(3,"kunal","anil","sangle",23,"pune","kunal@gmail.com",7083534353);
insert into Student(id,fname,mname,lname,age,address,email,phone) values(4,"akhil","ashok","berad",23,"pune","akhil@gmail.com",7083534353);
insert into Student(id,fname,mname,lname,age,address,email,phone) values(5,"kshitij","hari","gade",24,"pune","kshitij@gmail.com",7083534353);
select * from Student;

# using auto_increment to create a table in the database
create table auto_increment(
	id int auto_increment primary key,
    name varchar(10) not null,
    blood varchar(5)
);
insert into auto_increment(id,name,blood) values(1,"atharv","A+");
insert into auto_increment(name,blood) values("akhil","A+");
insert into auto_increment(name,blood) values("kunal","B+");
insert into auto_increment(name,blood) values("atharva","AB+");
insert into auto_increment(name,blood) values("kshitij","C");
select * from auto_increment;

# using timestamp to create a table in the database
create table class(
	student_id int auto_increment,
    student_fname varchar(20) not null,
    student_mname varchar(20),
    student_lname varchar(20) not null,
    student_email varchar(20) not null,
    student_phone varchar(15) not null,
    enrollment_date timestamp not null,
    year_of_exp int not null,
    student_company varchar(10) not null,
    batch_date varchar(20) not null,
    source_of_joining varchar(20),
    location varchar(20) not null,
    primary key(student_id),
	unique key(student_email)
);
insert into class (student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('virat', 'kohli','virat@gmail.com', '9292929292', 3, 'flipkart', '5-02-2021','linkedin', 'hyderabad',now());
insert into class (student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('ms', 'dhoni','msd@gmail.com', '9292929292', 9, 'apple', '5-02-2021','linkedin', 'hyderabad',now());
insert into class (student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('suresh', 'raine','suresh@gmail.com', '9292929292', 3, 'flipkart', '5-02-2021','linkedin', 'hyderabad',now());
insert into class (student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('rohit', 'sharma','rohit@gmail.com', '9292929292', 3, 'flipkart', '5-02-2021','linkedin', 'hyderabad',now());
insert into class (student_fname, student_lname, student_email,student_phone, year_of_exp, student_company, batch_date,source_of_joining, 
location,enrollment_date) 
values('ravindra', 'jadeja','ravi@gmail.com', '9292929292', 3, 'flipkart', '5-02-2021','linkedin', 'hyderabad',now());
select * from class;

# creating new table to join the class table
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
select * from class,course;
set sql_safe_updates = 0;

# applying different conditions in mysql
# using where condition
select * from class where student_fname = 'virat';
select * from course where course_name = 'Data Science';
select * from class where year_of_exp > 5;
select * from class where student_company = 'apple';

# using count condition
use revision;
select count(*) from class;
select count(*) from course;
select count(student_company) from class;
select count(distinct location) from class;

# using group by condition
select source_of_joining from class group by source_of_joining;
-- count of student from different locations and name of location
select location, count(*) from class group by location;
-- count of student by location and source_of_joining... location and source_of_joining unique combination --- count
select location, source_of_joining, count(*) from class group by location, source_of_joining;

# Using MIN,MAX,SUM,AVG conditions
-- MAX
select max(year_of_exp) from class;
-- MIN
select min(year_of_exp) from class;
-- SUM
select sum(year_of_exp) from class;
-- AVG
select avg(year_of_exp) from class;

# types of joins ->
-- 1. Inner join -> Returns only the rows that have matching values in both tables.
-- 2. Left join -> Returns all rows from the left table, plus the matching rows from the right table.
-- 3. Right join -> Returns all rows from the right table, plus the matching rows from the left table
-- 4. Full join -> Returns all rows from both tables.
# Using join to combine two tables
-- inner join
select * from student, course;
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class INNER JOIN course ON student_id = course_id;
-- left join
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class left JOIN course ON student_id = course_id;
-- right join
select student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee from class right join course on student_id = course_id;
-- full join 
SELECT student_id,student_fname,student_lname,student_email,student_phone,student_company,course_name,course_fee FROM class full JOIN course ON student_id = course_id;

# ROW , RANK() , DENSE_RANK()
SELECT course_name,course_fee,RANK() OVER (ORDER BY course_fee DESC) AS course_rank FROM course;
SELECT course_name,course_fee,DENSE_RANK() OVER (ORDER BY course_fee DESC) AS course_dense_rank FROM course;