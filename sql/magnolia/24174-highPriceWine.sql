--ignore their select * from winemag_p1;
WITH floor AS (
    SELECT
        variety,
        MIN(points) AS worst
    FROM
        winemag_p1
    GROUP BY
        variety
)
(SELECT
    wine.variety,
    MAX(wine.price) AS "highestPrice"
FROM 
    winemag_p1 AS wine
INNER JOIN
    floor
ON
    wine.variety = floor.variety
WHERE
    wine.country = 'US' AND
    floor.worst >= 90
GROUP BY
    wine.variety)
EXCEPT
(SELECT
    wine.variety,
    MAX(wine.price) AS "highestPrice"
FROM 
    winemag_p1 AS wine
INNER JOIN
    floor
ON
    wine.variety = floor.variety
WHERE
    wine.country IN ('Spain', 'Argentina', 'Portugal')  AND
    floor.worst >= 90
GROUP BY
    wine.variety);
