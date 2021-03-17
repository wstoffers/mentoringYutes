--ignore their select * from ms_employee_salary;
SELECT
    id,
    first_name,
    last_name,
    department_id,
    MAX(salary) AS "currentSalary"
FROM ms_employee_salary
GROUP BY
    id,
    first_name,
    last_name,
    department_id
ORDER BY
    id ASC;
