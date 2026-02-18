use revision;
create table name(
	id int primary key auto_increment,
    fname varchar(10) not null,
    mname varchar(10),
    lname varchar(10) not null,
    age int,
    address varchar(20) not null
);
insert into name(fname,mname,lname,age,address) values ("atharv","avinash","penter",22,"pune");
insert into name(fname,mname,lname,age,address) values ("aa","avinash","e",22,"pune");
insert into name(fname,mname,lname,age,address) values ("cc","avinash","r",22,"pune");
insert into name(fname,mname,lname,age,address) values ("ss","avinash","t",22,"pune");
insert into name(fname,mname,lname,age,address) values ("dd","avinash","i",22,"pune");
select * from name;

# using timestamp in table
create table room(
	id int primary key auto_increment,
    name varchar(10) not null,
    age int,
    phone varchar(15) not null,
    company varchar(10) not null
);
insert into room(name,age,phone,company) values ("atharv",22,"7083534353","apple");
insert into room(name,age,phone,company) values ("e",22,"7083534353","apple");
insert into room(name,age,phone,company) values ("r",22,"7083534353","apple");
insert into room(name,age,phone,company) values ("t",22,"7083534353","apple");
insert into room(name,age,phone,company) values ("y",22,"7083534353","apple");
select * from room;

# concatination
create table courses(
	id int primary key auto_increment,
    name varchar(10) not null,
    duration int
);
insert into courses(name,duration) values ("DS",3);
insert into courses(name,duration) values ("DA",3);
insert into courses(name,duration) values ("DSA",3);
insert into courses(name,duration) values ("FD",3);
insert into courses(name,duration) values ("DEV",3);
select * from room,courses;

# aggregate functions
# sum,min,max,avg
select max(age) from room;
select min(age) from room;
select avg(age) from room;
select sum(age) from room;

# using joins
select * from room,courses;
select name,age,name,duration from room inner join courses on name = name;