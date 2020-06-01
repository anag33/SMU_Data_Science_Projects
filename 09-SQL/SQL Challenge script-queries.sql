--1. List the following details of each employee: employee number, last name, first name, sex, and salary.

select 
	e.emp_no,
	e."last_Name",
	e."first_Name",
	e.sex,
	s.salary
from 
	"Employees" e 
	join "Salaries" s on s.emp_no = e.emp_no 
order by
	e.emp_no asc 
limit 10


--2. List first name, last name, and hire date for employees who were hired in 1986.

select 
	e.emp_no,
	e."last_Name",
	e."first_Name",
	e.hire_date 
from 
	"Employees" e 

where
	extract(year from hire_date) = 1986
order by
	e.hire_date asc 
limit 10


--3. List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name.

select 
	dm.dept_manager_id,
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e."last_Name",
	e."first_Name"
from 
	"Dept_manager" dm 
	join "Departments" d on dm.dept_no = d.dept_no 
	join "Employees" e on dm.emp_no = e.emp_no 
order by
	d.dept_no asc 
limit 10


--4. List the department of each employee with the following information: employee number, last name, first name, and department name.

select 
	de.dept_emp_id,
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e."last_Name",
	e."first_Name"
from 
	"Dept_emp" de 
	join "Departments" d on de.dept_no = d.dept_no 
	join "Employees" e on de.emp_no = e.emp_no 
order by
	d.dept_no asc, emp_no asc
limit 10

--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

select 
	e.emp_no,
	e."last_Name",
	e."first_Name",
	e.sex 
from 
	"Employees" e
where
	"first_Name" = 'Hercules'
	and "last_Name" like 'B%'
order by
	emp_no asc
limit 10


--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

select 
	de.dept_emp_id,
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e."last_Name",
	e."first_Name"
from 
	"Dept_emp" de 
	join "Departments" d on de.dept_no = d.dept_no 
	join "Employees" e on de.emp_no = e.emp_no 
where
	d.dept_name = 'Sales'
order by
	d.dept_no asc, emp_no asc
limit 10

--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select 
	de.dept_emp_id,
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e."last_Name",
	e."first_Name"
from 
	"Dept_emp" de 
	join "Departments" d on de.dept_no = d.dept_no 
	join "Employees" e on de.emp_no = e.emp_no 
where
	d.dept_name = 'Sales' or d.dept_name = 'Development'
order by
	d.dept_no asc, emp_no asc
limit 10

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select 
	e."last_Name",
	count(e."last_Name")
from 
	"Employees" e
group by
	e."last_Name" 
order by
	count(e."last_Name") desc
limit 10