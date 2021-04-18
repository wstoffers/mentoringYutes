--ignore their select * from yelp_reviews;
WITH ranked AS(
    SELECT
        business_name AS "businessName",
        review_text AS "reviewText",
        RANK() OVER(ordered) AS coolest
    FROM
        yelp_reviews
    WINDOW
        ordered AS (ORDER BY cool DESC)
)
SELECT
    "businessName",
    "reviewText"
FROM
    ranked
WHERE
    coolest = 1;
