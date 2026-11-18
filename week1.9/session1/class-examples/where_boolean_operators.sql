.headers on
.mode column

SELECT name, price FROM menu_items WHERE is_vegetarian = 1 AND price < 15;

SELECT name FROM restaurants WHERE cuisine = 'Thai' OR cuisine = 'Indian';

SELECT name FROM restaurants WHERE cuisine = 'Thai' OR cuisine = 'Indian' AND hygiene_rating = 5;

SELECT name FROM restaurants WHERE (cuisine = 'Thai' OR cuisine = 'Indian') AND hygiene_rating = 5;