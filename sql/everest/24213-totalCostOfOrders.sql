--select * from customers;
SELECT
    customers.id,
    customers.first_name,
    SUM(orders.order_cost) AS "totalOrderCost"
FROM customers
JOIN orders ON
    customers.id = orders.cust_id
GROUP BY
    customers.id,
    customers.first_name
ORDER BY
    customers.first_name;
