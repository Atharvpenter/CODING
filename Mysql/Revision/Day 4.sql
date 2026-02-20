use revision;
# creating simple table using primary key
create table pora(
	id int primary key,
    name varchar(10) not null,
    phone varchar(14) not null
);
insert into pora(id,name,phone) values(1,'atharv','7083534353');
insert into pora(id,name,phone) values(2,'akhil','7083534353');
insert into pora(id,name,phone) values(3,'atharva','7083534353');
insert into pora(id,name,phone) values(4,'kunal','7083534353');
insert into pora(id,name,phone) values(5,'kshitij','7083534353');
select * from pora;

# using auto_increment to avoid giving id's separately
create table auto(
	id int primary key auto_increment,
    name varchar(10)
);
insert into auto(name) values('atharv');
insert into auto(name) values('atharva');
insert into auto(name) values('kunal');
insert into auto(name) values('akhil');
insert into auto(name) values('kshitij');
select * from auto;

# using timestamp
create table classroom(
	student_id int auto_increment,
    student_name varchar(10) not null,
    student_age int(10),
    student_address varchar(10) default 'Pune',
    student_phone varchar(12) not null,
    student_email varchar(20),
    primary key(student_id),
    unique key(student_email)
);
insert into classroom(student_name,student_age,student_address,student_phone,student_email) values('atharv',22,'pune','7083534353','ap@gmail.com');
insert into classroom(student_name,student_age,student_address,student_phone,student_email) values('atharva',22,'pune','7083534353','ak@gmail.com');
insert into classroom(student_name,student_age,student_address,student_phone,student_email) values('kunal',22,'pune','7083534353','ks@gmail.com');
insert into classroom(student_name,student_age,student_address,student_phone,student_email) values('akhil',22,'pune','7083534353','ab@gmail.com');
insert into classroom(student_name,student_age,student_address,student_phone,student_email) values('kshitij',22,'pune','7083534353','kg@gmail.com');
select * from classroom;

# joining two different tables
create table sub(
	sub_id int auto_increment,
    sub_name varchar(10) not null,
    sub_duration varchar(10),
    primary key(sub_id)
);
insert into sub(sub_name,sub_duration) values('ds','7 months');
insert into sub(sub_name,sub_duration) values('da','7 months');
insert into sub(sub_name,sub_duration) values('dsa','7 months');
insert into sub(sub_name,sub_duration) values('wd','7 months');
insert into sub(sub_name,sub_duration) values('sd','7 months');
select * from classroom,sub;

# using aggregate functions
select max(student_age) from classroom;
select min(student_age) from classroom;
select sum(student_age) from classroom;
select avg(student_age) from classroom;

# using joins
create table emp(
	emp_id int primary key auto_increment,
    emp_name varchar(10)
);
insert into emp(emp_name) values('atharv');
insert into emp(emp_name) values('atharva');
insert into emp(emp_name) values('kunal');
insert into emp(emp_name) values('akhil');
insert into emp(emp_name) values('kshitij');

create table department(
	dept_id int primary key auto_increment,
    dept_name varchar(10)
);
insert into department(dept_name) values('HR');
insert into department(dept_name) values('SALES');
insert into department(dept_name) values('TECHNICAL');
insert into department(dept_name) values('NTECH');
insert into department(dept_name) values('MARKETING');
select * from emp,department;

# using inner join
select emp_name,dept_name from emp inner join department on emp_id = dept_id;
# using left join
select emp_name,dept_name from emp left join department on emp_id = dept_id;
# using right join
select emp_name,dept_name from emp right join department on emp_id = dept_id;

# using different conditions 
# where
select * from classroom where student_age > 20;
# count
select count(student_email) from classroom;


