--ignore their select * from employee;
SELECT
    first_name AS name,
    bonus
FROM
    employee
WHERE
    bonus < 150;
