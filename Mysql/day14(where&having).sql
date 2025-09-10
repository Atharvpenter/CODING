use atharv;
-- Where -> filters groups before grouping.
-- Having -> filters groups after grouping.
select * from student;
select source_of_joining, count(*) as total from student group by source_of_joining having total>1 ;