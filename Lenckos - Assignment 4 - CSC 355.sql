/*
Michael Lenckos
CSC 355 Section 501
Assignment 4
Febuary 6th, 2020
*/

-- 1. Display the number of employees who make at least $90,000, and the average salary among those employees.

select count(salary), avg(salary)
from employee
where salary>90000;

--select avg(salary)
--from employee
--where salary>90000;

-- 2 For each department, give the department number and name and the largest salary of an employee in that department. Order the rows by the department number.

select dname, dnumber, max(salary)
from department
inner join employee
on dnumber = employee.dno
group by dname, dnumber
order by dnumber;


/* 3. List the last names and salaries of all male employees in the Development department,
ordered from the employee with the lowest salary to the employee with the highest
salary. 
*/

select employee.last, salary, gender
from EMPLOYEE
where gender = 'M'
and employee.dno  = 2 -- might want to do better way
order by salary asc;

-- 4. Display the smallest salary paid to an employee working on the Automation project.

select min(salary) 
from employee 
where employee.eid in 
    (select assignment.employeeid
    from assignment
    inner join project
    on assignment.projectno = project.pnumber
    where assignment.projectno = 11);

/*5. List, in alphabetical order, the names of all projects that Ahmed Salman works on, and
the number of hours he works on each project.*/
select assignment.projectno, assignment.hours, project.pname
from assignment
inner join project
on project.pnumber = assignment.projectno
where assignment.employeeid = 9879877 -- might want better way 
order by project.pname;

/* 6. List the IDs of all employees who are assigned to three or more projects, along with
the number of projects each of them is assigned to. */
select employeeid, count(employeeid) as "Projects assigned to"
from assignment
having count(employeeid) > 2
group by employeeid;

/*7. Give the ID and full name of every employee who has a son, along with the
employee’s son’s first name and age. Order the output by the son’s age, from youngest to
oldest. */
select distinct employee.eid, employee.first, employee.last, dependent.first, dependent.age
from employee
inner join dependent
on employee.eid = dependent.employeeid
where employee.eid in (
    select employeeid
    from dependent
    where relationship = 'Son')
and dependent.relationship = 'Son'
order by dependent.age asc;

/*8. For each project located in Pittsburgh, display the project number, project name, and
the total number of hours that employees have been assigned to that project. List the
projects from the one with the most total hours assigned to it to the one with the fewest. */
select sum(hours), projectno
from assignment
where projectno in 
    (select pnumber
    from project
    where plocation = 'Pittsburgh')
group by projectno
order by sum(hours) desc;