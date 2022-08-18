-- SQLite
SELECT * FROM users LIMIT 1;
SELECT last_name||first_name name,
age,
country as sido,
phone,
balance
FROM users
LIMIT 5;
SELECT LENGTH(first_name),first_name
FROM users LIMIT 5;

SELECT first_name,REPLACE(phone,'-','') phone
FROM users
LIMIT 5;

SELECT MOD(5,2)
FROM users
LIMIT 1;

SELECT CEIL(3.14),FLOOR(3.14),ROUND(3.14)
FROM users
LIMIT 1;

SELECT SQRT(9)
FROM users
LIMIT 1;

SELECT POWER(9,2)
FROM users
LIMIT 1;