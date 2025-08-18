-- alter is used to add, modify tables.


select * from employee;
insert into employee(id,firstname, lastname, age, salary) values(7,'shreyash','dhole', 22, 100000);
insert into employee(id,firstname, lastname, age, salary) values(4,'sarvesh','penter', 23, 100000);
insert into employee(id,firstname, lastname, age, salary) values(5,'aditya','penter', 24, 100000);
insert into employee(id,firstname, lastname, age, salary) values(6,'shivam','more', 25, 100000);
select* from employee;
alter table employee add column jobTitle varchar(20) default 'Manager';
alter table employee add column workmode varchar(20) default 'hybrid';
select * from employee;