--ignore their select * from airbnb_reviews;
SELECT
    guests.gender,
    AVG(reviews.review_score) AS "averageReviewScore"
FROM airbnb_reviews AS reviews
JOIN airbnb_guests AS guests ON
    reviews.from_user = guests.guest_id
WHERE
    from_type = 'guest'
GROUP BY
    guests.gender
ORDER BY
    "averageReviewScore" DESC
LIMIT 1;

SELECT
    guests.gender,
    AVG(reviews.review_score) AS "averageReviewScore"
FROM
    airbnb_reviews AS reviews,
    airbnb_guests AS guests
WHERE
    reviews.from_user = guests.guest_id AND
    from_type = 'guest'
GROUP BY
    guests.gender
ORDER BY
    "averageReviewScore" DESC
LIMIT 1;
