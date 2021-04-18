--ignore their select * from airbnb_search_details;
SELECT
    city,
    MIN(price) AS cheapest
FROM 
    airbnb_search_details
GROUP BY
    city;
