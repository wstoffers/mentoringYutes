--ignore their select * from los_angeles_restaurant_health_inspections;
SELECT
    grade,
    avg(score)
FROM
    los_angeles_restaurant_health_inspections
GROUP BY
    grade;
