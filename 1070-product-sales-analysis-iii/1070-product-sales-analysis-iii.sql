# Write your MySQL query statement below
# Below Approah exceeds the time limit and only 5/10 test cases pass
/*
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
WHERE s.year=(
    SELECT MIN(s2.year)
    FROM Sales s2
    WHERE s2.product_id=s.product_id
);
*/
SELECT product_id, year AS first_year, quantity, price
FROM (
    SELECT 
       product_id, 
       year, 
       quantity, 
       price,
       DENSE_RANK() OVER(
          PARTITION BY product_id
          ORDER BY YEAR
        ) AS rnk
    FROM Sales
) s
WHERE rnk=1;