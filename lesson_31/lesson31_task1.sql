select 
e.first_name,
e.last_name,
e.department_id,
d.depart_name
from employees e 
left join departments d 
on e.department_id = d.department_id;

SELECT 
e.first_name,
e.last_name,
d.depart_name,
l.city,
l.state_province
from employees e 
left join departments d 
on e.department_id = d.department_id
left join locations l 
on d.location_id = l.location_id;

select 
e.first_name,
e.last_name,
e.department_id,
d.depart_name
from employees e 
join departments d 
on e.department_id = d.department_id 
where (e.department_id = 80 or e.department_id = 40);

select 
department_id,
depart_name 
from departments d; 

SELECT 
e.first_name as 'Employee',
emp.first_name as 'Manager'
from employees e 
left join employees emp
on e.manager_id = emp.employee_id;

select 
j.job_title,
(e.first_name || ' ' || e.last_name) as 'Full name',
(j.max_salary - e.salary) as 'Salary difference'
from jobs j 
join employees e 
on j.job_id = e.job_id;

SELECT 
j.job_title,
avg(e.salary)
from jobs j 
join employees e 
on j.job_id = e.job_id
group by j.job_title;

SELECT 
(e.first_name || ' ' || e.last_name) as 'Full name',
e.salary
from employees e 
join departments d 
on e.department_id = d.department_id
left join locations l 
on d.location_id = l.location_id
where l.city = 'London'; 

SELECT 
d.depart_name,
count(e.employee_id)
from departments d  
join employees e 
on d.department_id = e.department_id
group by d.depart_name ;


