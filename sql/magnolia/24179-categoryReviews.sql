--ignore their select * from yelp_business;
WITH separated AS (
    SELECT
        UNNEST(STRING_TO_ARRAY(categories,';')) AS categories,
        review_count
    FROM 
        yelp_business
)
SELECT
    categories,
    SUM(review_count) AS "reviewCount"
FROM
    separated
GROUP BY
    categories
ORDER BY
    "reviewCount" DESC;
