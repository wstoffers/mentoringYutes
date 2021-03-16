--ignore their select * from employee;
SELECT
    first_name AS "firstName"
FROM
    employee
WHERE
    manager_id != 1;
