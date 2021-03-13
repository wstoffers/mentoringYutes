--ignore their select * from db_employee;
SELECT
    MAX(CASE WHEN
            dept.department = 'marketing'
        THEN
            employees.salary
        END) -
    MAX(CASE WHEN
            dept.department = 'engineering'
        THEN
            employees.salary
        END) AS "salaryDifference"
FROM db_employee AS employees
JOIN db_dept AS dept ON
    employees.department_id = dept.id;
