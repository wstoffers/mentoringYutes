--ignore their select * from facebook_employees;
SELECT
    employees.location,
    AVG(survey.popularity) AS "averagePopularity"
FROM
    facebook_employees AS employees
JOIN facebook_hack_survey AS survey ON
    employees.id = survey.employee_id
GROUP BY
    employees.location;
