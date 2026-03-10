use revision;
#create simple table in the database
create table r(
	id int primary key,
    name varchar(10),
    age int(2)
);
insert into r(id,name,age) values(1,'a',22);
insert into r(id,name,age) values(2,'a',22);
insert into r(id,name,age) values(3,'a',22);
insert into r(id,name,age) values(4,'a',22);
insert into r(id,name,age) values(5,'a',22);
select * from r;

# use auto_increment
create table a(
	id int primary key auto_increment,
    name varchar(10),
    age int(2)
);
insert into a(name,age) values('a',22);
insert into a(name,age) values('a',22);
insert into a(name,age) values('a',22);
insert into a(name,age) values('a',22);
insert into a(name,age) values('a',22);
select * from a;

# using timestamp
create table map(
	m_id int primary key auto_increment,
    m_name varchar(10),
    m_age int(2),
    m_date timestamp
);
insert into map(m_name,m_age,m_date) values('a',22,'2025-07-22');
insert into map(m_name,m_age,m_date) values('a',27,'2025-07-22');
insert into map(m_name,m_age,m_date) values('a',29,'2025-07-22');
insert into map(m_name,m_age,m_date) values('a',21,'2025-07-22');
insert into map(m_name,m_age,m_date) values('a',22,'2025-07-22');
select * from map;

# Joining  two tables
create table wap(
	w_id int primary key auto_increment,
    w_name varchar(10),
    w_course varchar (20)
);
insert into wap(w_name,w_course) values ('a','data science');
insert into wap(w_name,w_course) values ('a','data analyst');
insert into wap(w_name,w_course) values ('a','data engineer');
insert into wap(w_name,w_course) values ('a','data collection');
insert into wap(w_name,w_course) values ('a','data visualization');
select * from map,wap;

# aggregate function
select max(m_age) from map;
select min(m_age) from map;
select avg(m_age) from map;

# joins
select m_name,m_age,m_date,w_name,w_course from map right join wap on m_id = w_id;

