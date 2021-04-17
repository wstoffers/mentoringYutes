--ignore their select * from employee;
SELECT
    first_name
FROM employee
WHERE
    department = 'Sales' AND
    target > 150
ORDER BY
    first_name DESC;
