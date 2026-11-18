.headers on
.mode column


-- Some examples of WHEREs

SELECT name FROM restaurants WHERE cuisine = 'Italian';

SELECT name, price from menu_items WHERE price < 8;

SELECT name FROM customers WHERE email LIKE '%@leeds.ac.uk';

SELECT name FROM restaurants WHERE postcode LIKE 'LS6%';