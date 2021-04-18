--ignore their select * from airbnb_search_details;
SELECT
    neighbourhood,
    AVG(beds) AS "averageBeds"
FROM
    airbnb_search_details
GROUP BY
    neighbourhood
HAVING
    SUM(beds) >= 3
ORDER BY
    "averageBeds" DESC;
