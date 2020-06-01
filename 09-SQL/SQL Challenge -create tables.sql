CREATE TABLE "Departments" (
    "dept_no" varchar(20)   NOT NULL,
    "dept_name" varchar(50)  NULL,
    "last_updated" timestamp null default current_timestamp,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "Titles" (
    "title_id" varchar(20)   NOT NULL,
    "title" varchar(50)   NULL,
    "last_updated" timestamp null default current_timestamp,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "title_id"
     )
);

CREATE TABLE "Employees" (
    "emp_no" Int   NOT NULL,
    "emp_title_id" varchar(10)  NULL,
    "birth_date" date   NULL,
    "first_Name" varchar(50) NULL,
    "last_Name" varchar(50)  NULL,
    "sex" varchar(1) NULL,
    "hire_date" date NULL,
     "last_updated" timestamp null default current_timestamp,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "Dept_emp" (
    "dept_emp_id" serial not null,
    "emp_no" int NULL,
    "dept_no" varchar(20) NULL,
   "last_updated" timestamp null default current_timestamp,
   CONSTRAINT "pk_Dept_emp" PRIMARY KEY (
        "dept_emp_id"
   )   
);

CREATE TABLE "Dept_manager" (
    "dept_manager_id" serial  NOT NULL,
    "dept_no" varchar(20) NULL,
    "emp_no" int NULL,
     "last_updated" timestamp null default current_timestamp,
    CONSTRAINT "pk_Dept_manager" PRIMARY KEY (
        "dept_manager_id"
     )
);
 
CREATE TABLE "Salaries" (
    "salary_id" serial  NOT NULL,
    "emp_no" int  NULL,
    "salary" int  NULL,
    "last_updated" timestamp null default current_timestamp,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "salary_id"
     )
);

ALTER TABLE "Employees" ADD CONSTRAINT "fk_Employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "Titles" ("title_id");

ALTER TABLE "Dept_emp" ADD CONSTRAINT "fk_Dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Dept_emp" ADD CONSTRAINT "fk_Dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

ALTER TABLE "Dept_manager" ADD CONSTRAINT "fk_Dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_no");

ALTER TABLE "Dept_manager" ADD CONSTRAINT "fk_Dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employees" ("emp_no");
