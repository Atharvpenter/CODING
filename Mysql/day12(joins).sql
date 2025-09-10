-- joins ->
-- It is used to join two tables
-- types of joins ->
-- 1. Inner join -> Returns only the rows that have matching values in both tables.
-- 2. Left join -> Returns all rows from the left table, plus the matching rows from the right table.
-- 3. Right join -> Returns all rows from the right table, plus the matching rows from the left table
-- 4. Full join -> Returns all rows from both tables.

use atharv;
select * from student;
select * from course;
select student_fname, student_mname, student_lname, student_phone, student_email, course_id, course_name, course_fee from student join course;
