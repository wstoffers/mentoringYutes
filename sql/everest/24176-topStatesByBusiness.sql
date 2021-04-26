--ignore their select * from yelp_business;
SELECT
    state,
    COUNT(1) AS "fiveStars"
FROM yelp_business
WHERE
    stars = 5
GROUP BY
    state
ORDER BY
    "fiveStars" DESC,
    state ASC
LIMIT 5;
