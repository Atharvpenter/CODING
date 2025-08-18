create table empCRUD(
	id int primary key,
    fn varchar(20) not null,
    ln varchar(20) not null,
    age int unsigned,
    salary int unsigned,
    location varchar(30)
);
select * from empCRUD;
insert into empCRUD(id,fn,ln,age,salary,location) values(1,'atharv','penter',22,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(2,'prajwal','dighe',24,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(3,'rr','ame',35,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(4,'aa','bb',74,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(5,'dd','cc',33,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(6,'ee','tt',31,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(7,'rt','sr',50,100,'pune');
insert into empCRUD(id,fn,ln,age,salary,location) values(8,'tt','qq',40,100,'pune');
select * from empCRUD;

#view specific enteries we use specific operations like,
select * from empCRUD where age > 30;

--------------------------------
#sql_safe_updates---> used to prevent accidental loss while running statements.
set sql_safe_updates = 0;  --- #not started
set sql_safe_updates = 1;  ----#starte
select * from empCRUD;
