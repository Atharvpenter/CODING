use revision;
create table aar(
	id int primary key,
    name varchar(20),
    age int(2)
);
insert into aar(id,name,age) values(1,'a',22);
insert into aar(id,name,age) values(2,'a',22);
insert into aar(id,name,age) values(3,'a',22);
insert into aar(id,name,age) values(4,'a',22);
insert into aar(id,name,age) values(5,'a',22);
select * from aar;

create table at(
	id int primary key auto_increment,
    name varchar(20),
    age int(2)
);
insert into at(name,age) values('a',22);
insert into at(name,age) values('a',22);
insert into at(name,age) values('a',22);
insert into at(name,age) values('a',22);
insert into at(name,age) values('a',22);
select * from at;

create table ep(
	id int primary key auto_increment,
    name varchar(20),
    date timestamp,
    age int(2)
);
insert into ep(name,date,age) values('a','2025-08-02',22);
insert into ep(name,date,age) values('a','2025-08-02',22);
insert into ep(name,date,age) values('a','2025-08-02',22);
insert into ep(name,date,age) values('a','2025-08-02',22);
insert into ep(name,date,age) values('a','2025-08-02',22);
select * from ep;

select max(age) from ep;
select min(age) from ep;
select avg(age) from ep;
select sum(age) from ep;

select * from ep where age >10;
select count(age) from ep;

create table j(
	j_id int primary key auto_increment,
    j_name varchar(20),
    j_age int(2)
); 
create table e(
	e_id int primary key auto_increment,
    e_name varchar(20),
    e_age int(2)
);
insert into j(j_name,j_age) values('a',22);
insert into j(j_name,j_age) values('d',23);
insert into j(j_name,j_age) values('c',24);
insert into e(e_name,e_age) values('a',22);
insert into e(e_name,e_age) values('b',23);
insert into e(e_name,e_age) values('c',24);
select * from j,e;
select j_name,j_age,e_name,e_age from j right join e on j_id = e_id;
select j_name,j_age,e_name,e_age from j left join e on j_id = e_id;
select j_name,j_age,e_name,e_age from j full join e on j_id = e_id;
