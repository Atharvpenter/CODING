-- Logical Operators 
-- AND,NOT,NOR,XNOR(&,!)

use atharv;
select * from course;
select * from student;
select student_fname, batch_date,source_of_joining, location, student_company, year_of_exp from student where location = 'america';
select student_fname, batch_date,source_of_joining, location, student_company, year_of_exp from student where location != 'america';
select student_fname from student where student_fname regexp '^r';