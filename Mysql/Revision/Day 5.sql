use revision;
# create a table in the database
create table don(
	id int primary key,
    name varchar(10),
    age int(2),
    address varchar(10)
);
insert into don(id,name,age,address) values(1,'ap',22,'pune');
insert into don(id,name,age,address) values(2,'ap1',22,'pune');
insert into don(id,name,age,address) values(3,'ap2',22,'pune');
insert into don(id,name,age,address) values(4,'ap3',22,'pune');
insert into don(id,name,age,address) values(5,'ap4',22,'pune');
select * from don;

# using auto_increment
create table inc(
	id int primary key auto_increment,
    name varchar(10) not null,
    age int(2)
);
insert into inc(name,age) values('ap',22);
insert into inc(name,age) values('ap1',22);
insert into inc(name,age) values('ap2',22);
insert into inc(name,age) values('ap3',22);
insert into inc(name,age) values('ap4',22);
select * from inc;

# using timestamp
create table local(
	lc_id int auto_increment,
    lc_name varchar(20) not null,
    lc_age int(2),
    lc_date timestamp,
    lc_address varchar(20),
    primary key(lc_id)
);
insert into local(lc_name,lc_age,lc_date,lc_address) values('ap',22,'2002-02-23','thane');
insert into local(lc_name,lc_age,lc_date,lc_address) values('ap1',22,'2002-02-23','thane');
insert into local(lc_name,lc_age,lc_date,lc_address) values('ap2',22,'2002-02-23','thane');
insert into local(lc_name,lc_age,lc_date,lc_address) values('ap3',22,'2002-02-23','thane');
insert into local(lc_name,lc_age,lc_date,lc_address) values('ap4',22,'2002-02-23','thane');
select * from local;

# joining two different tables
create table ppl(
	ppl_id int primary key auto_increment,
    ppl_name varchar(10),
    pp_field varchar(10)
);
insert into ppl(ppl_name,pp_field) values('aa','cricket');
insert into ppl(ppl_name,pp_field) values('aa1','cricket');
insert into ppl(ppl_name,pp_field) values('aa2','cricket');
insert into ppl(ppl_name,pp_field) values('aa3','cricket');
insert into ppl(ppl_name,pp_field) values('aa4','cricket');
select * from local,ppl;

# using aggregate functions
select max(lc_age) from local;
select min(lc_age) from local;
select sum(lc_age) from local;
select avg(lc_age) from local;

# using different conditions in database
# where
select * from local where lc_address = 'thane';
select * from ppl where pp_field = 'cricket';
select * from local where lc_age > 20;

# count
select count(*) from local;
select count(pp_field) from ppl;

# Using joins
create table player(
	py_id int primary key auto_increment,
    py_name varchar(10) not null
);
insert into player(py_name) values('ap');
insert into player(py_name) values('ap1');
insert into player(py_name) values('ap2');
insert into player(py_name) values('ap3');
insert into player(py_name) values('ap4');
create table team(
	tm_id int primary key auto_increment,
    tm_name varchar(10) not null
);
insert into team(tm_name) values('india');
insert into team(tm_name) values('australia');
insert into team(tm_name) values('eng');
insert into team(tm_name) values('wi');
insert into team(tm_name) values('sa');
select * from player,team;
select py_name,tm_name from player inner join team on py_id = tm_id;



