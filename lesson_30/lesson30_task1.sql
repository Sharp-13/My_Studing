attach database 'C:\Users\Serhii\Downloads\d1093fe7-995d-44c9-8728-673af8914cf8.db' as simpledb;
create table simpledb.cities
(
postcode integer,
name text,
population integer
);

alter table cities 
rename to ukrainian_cities;

alter table ukrainian_cities 
add column squere real;

insert into ukrainian_cities 
values(01001, 'Kyiv', 2884000, 839.2);

INSERT into ukrainian_cities 
values(65000, 'Odesa', 1010537, 16.42);

INSERT INTO ukrainian_cities 
values(39600, 'Kremenchuk', 215271, 96);

INSERT INTO ukrainian_cities 
values(308000, 'Bilgorod', 333931, 153.1);

update ukrainian_cities 
set squere = 162.42
where name = 'Odesa';

SELECT *
from ukrainian_cities uc 

delete from ukrainian_cities 
where name = 'Bilgorod';

SELECT *
from ukrainian_cities uc; 


