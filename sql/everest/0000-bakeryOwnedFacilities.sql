--ignore their select * from los_angeles_restaurant_health_inspections;
SELECT
    DISTINCT owner_name,
    pe_description
FROM
    los_angeles_restaurant_health_inspections
WHERE
    owner_name LIKE '%BAKERY%' AND
    pe_description LIKE '%LOW RISK%';
