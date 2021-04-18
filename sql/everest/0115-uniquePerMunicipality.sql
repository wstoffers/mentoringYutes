--ignore their select * from los_angeles_restaurant_health_inspections;
SELECT
    facility_zip,
    COUNT(DISTINCT facility_id) AS facilities,
    COUNT(1) AS inspections
FROM
    los_angeles_restaurant_health_inspections
GROUP BY
    facility_zip
ORDER BY
    inspections DESC;
