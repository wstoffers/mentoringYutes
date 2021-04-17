--ignore their select * from employee;
SELECT
    department,
    first_name,
    salary,
    AVG(salary) OVER
        (PARTITION BY
             department) AS "avgDeptSalary"
FROM employee;

