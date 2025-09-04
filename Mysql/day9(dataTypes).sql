-- Data Types in MYSQl →
-- Numeric → INT, DECIMAL, FLOAT
-- String → CHAR, VARCHAR, TEXT, BLOB
-- Date/Time → DATE, DATETIME, TIMESTAMP, TIME, YEAR
-- Special → ENUM, SET, SPATIAL

use atharv;
show tables;
create table course(
course_id int not null,
course_name varchar(20),
course_duration decimal(3,1) not null,
course_fee int not null,
changed_at TIMESTAMP DEFAULT NOW()
);
insert into course(course_id,course_name,course_duration,course_fee) values(1 , 'devops', 7.5, 75000);
insert into course(course_id,course_name,course_duration,course_fee) values(2 , 'AIML', 11.3, 95000);
insert into course(course_id,course_name,course_duration,course_fee) values(3 , 'python', 6.5, 15000);
insert into course(course_id,course_name,course_duration,course_fee) values(4 , 'java', 8.3, 15000);
insert into course(course_id,course_name,course_duration,course_fee) values(5 , 'javaScript', 5.9, 18000);
show tables;
select * from course;