--ignore their select * from customers;
SELECT
    customers.first_name AS "firstName",
    customers.last_name AS "lastName",
    customers.city,
    orders.order_details AS details
FROM
    customers
LEFT JOIN orders ON
    customers.id = orders.cust_id
ORDER BY
    "firstName" ASC,
    details ASC;
