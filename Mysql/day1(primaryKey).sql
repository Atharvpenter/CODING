#what is primary key --> primary key is an column which uniquely identifies each rows in the table.
create table employee(
id int primary key,
firstname varchar(20) not null,
lastname varchar(20) not null,
age int unsigned, 
salary int unsigned,
location varchar(20) not null default 'pune'
);
select * from employee;
insert into employee(id,firstname, lastname, age, salary) values(3,'atharv','penter', 22, 100000);
describe employee;
select * from employee;