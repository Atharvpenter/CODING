use revision;
create table tom(
	id int primary key,
    name varchar(10),
    age int(2)
);
insert into tom(id,name,age) values(1,'a',22);
insert into tom(id,name,age) values(2,'a',22);
insert into tom(id,name,age) values(3,'a',22);
insert into tom(id,name,age) values(4,'a',22);
insert into tom(id,name,age) values(5,'a',22);
select * from tom;

# using auto_increment
create table tt(
	id int primary key auto_increment,
    name varchar(20),
    age int(2)
);
insert into tt(name,age) values('a',22);
insert into tt(name,age) values('a',22);
insert into tt(name,age) values('a',22);
insert into tt(name,age) values('a',22);
insert into tt(name,age) values('a',22);
select * from tt;

# using timestamp
create table ap(
	id int primary key auto_increment,
    name varchar(20),
    age int(20),
    date timestamp
);
insert into ap(name,age,timestamp) values('aa',22,'2025-07-22');
insert into ap(name,age,timestamp) values('aa',22,'2026-02-02');
insert into ap(name,age,timestamp) values('aa',22,'2026-02-02');
insert into ap(name,age,timestamp) values('aa',22,'2026-02-02');
insert into ap(name,age,timestamp) values('aa',22,'2026-02-02');

# joining two tables
create table kn(
	id int primary key auto_increment,
    name varchar(20),
    age int(2)
);
insert into kn(name,age) values('a',22);
insert into kn(name,age) values('a',22);
insert into kn(name,age) values('a',22);
insert into kn(name,age) values('a',22);
insert into kn(name,age) values('a',22);
select * from kn;

create table nl(
	nl_id int primary key auto_increment,
    nl_name varchar(20),
    nl_age int(2)
);
insert into nl(nl_name,nl_age) values('a',22);
insert into nl(nl_name,nl_age) values('a',22);
insert into nl(nl_name,nl_age) values('a',22);
insert into nl(nl_name,nl_age) values('a',22);
insert into nl(nl_name,nl_age) values('a',22);
select * from kn,nl;

# aggregate function
select max(nl_age) from nl;
select min(nl_age) from nl;
select avg(nl_age) from nl;

# joins
