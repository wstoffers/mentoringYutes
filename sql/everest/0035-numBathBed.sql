--ignore their select * from airbnb_search_details;
SELECT
    city,
    property_type,
    AVG(bathrooms) AS "averageBaths",
    AVG(bedrooms) AS "averageBedrooms"
FROM 
    airbnb_search_details
GROUP BY
    city,
    property_type;
