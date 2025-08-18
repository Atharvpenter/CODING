use atharv;
create table student_demo(s_id int not null auto_increment, fname varchar(10),lname varchar(20),course varchar(20));
drop table student_demo;
create table student_demo (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50),
    course VARCHAR(50)
);
select * from student_demo;
insert into student_demo(student_name,course) values('Atharv Penter','Data Science');
insert into student_demo(student_name,course) values('Rohit Sharma', 'Full Stack'),
('Virat Kohli', 'Data Science'),
('MS Dhoni', 'AI & ML'),
('Shikhar Dhawan', 'Python'),
('Kapil Dev', 'Power BI'),
('Brian Lara', 'Excel'),
('Carl Hooper', 'Java'),
('Saurabh Ganguly', 'Cypress'),
('HL Rahul', 'Postman'),
('Rishabh Pant', 'Playwright');
select * from student_demo;
set sql_safe_updates = 0;  -- when it is 0 table can be modified.
set sql_safe_updates = 1;  -- when it is 1 table can not be updated.
delete from student_demo where student_name like 'Ro%';
select * from student_demo;
delete from student_demo where student_name like 'ri';
truncate table student_demo;   -- delete all columns and rows but it keeps sturcture.
select * from student_demo;