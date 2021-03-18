--ignore their select * from google_adwords_earnings;
SELECT
    business_type,
    SUM(adwords_earnings) as "totalEarnings"
FROM google_adwords_earnings
GROUP BY
    business_type;
