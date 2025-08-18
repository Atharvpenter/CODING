#what is auto increment used for in mysql ---> it increases value of a column
show databases;
use atharv;
show tables;
create table empAutoIncrement(
id int primary key auto_increment,
fn varchar(20) not null,
ln varchar(20) not null,
age int unsigned,
salary int unsigned,
location varchar(30) not null
);
select * from empAutoIncrement;
insert into empAutoIncrement(id,fn,ln,age,salary,location) values(1,'atharv','penter',22,100,'pune');
insert into empAutoIncrement(fn,ln,age,salary,location) values('ram','sham',22,10000,'pune');
insert into empAutoIncrement(fn,ln,age,salary,location) values('Ms','Dhoni',29,100000,'sangamner');
select * from empAutoIncrement;

#CRUD Operations ---> Create,read,update,delete.

