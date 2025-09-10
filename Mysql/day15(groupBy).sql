use atharv;
CREATE TABLE employee_over (
firstname varchar(20),
lastname varchar(20),
age int,
salary int,
location varchar(20)
);


INSERT INTO employee_over VALUES ('Lionel', 'Messi', 37, 120000, 'Miami');
INSERT INTO employee_over VALUES ('Cristiano', 'Ronaldo', 40, 150000, 'Riyadh');
INSERT INTO employee_over VALUES ('Neymar', 'Jr', 33, 110000, 'Riyadh');
INSERT INTO employee_over VALUES ('Kylian', 'Mbappe', 26, 95000, 'Madrid');
INSERT INTO employee_over VALUES ('Erling', 'Haaland', 25, 90000, 'Manchester');
INSERT INTO employee_over VALUES ('Luka', 'Modric', 39, 85000, 'Madrid');
INSERT INTO employee_over VALUES ('Robert', 'Lewandowski', 37, 92000, 'Barcelona');
INSERT INTO employee_over VALUES ('Kevin', 'DeBruyne', 34, 88000, 'Manchester');
INSERT INTO employee_over VALUES ('Mohamed', 'Salah', 33, 87000, 'Liverpool');
INSERT INTO employee_over VALUES ('Virgil', 'vanDijk', 34, 86000, 'Liverpool');

select * from employee_over;
select location, count(location), avg(salary) from employee_over group by location;