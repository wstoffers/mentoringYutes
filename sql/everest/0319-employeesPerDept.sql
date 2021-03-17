--ignore their select * from employee;
SELECT
    department,
    COUNT(1) AS "numEmployees"
FROM
    employee
GROUP BY
    department
ORDER BY
    "numEmployees" DESC;
