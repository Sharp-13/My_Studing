SELECT
first_name AS 'First Name',
last_name AS 'Last Name'
FROM employees;

select
DISTINCT department_id 
from employees e; 

select
*
from employees e 
order by first_name desc;

SELECT 
first_name as 'First Name',
last_name as 'Last Name',
salary,
salary*12/100 as PF
from employees e; 

select
max(salary) as 'Max Salary',
min(salary) as 'Min Salary'
from employees e; 

select
first_name as 'First Name',
last_name as 'Last Name',
round(salary/12, 2) as 'Monthly Salary'
from employees e; 

