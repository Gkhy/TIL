-- SQLite
SELECT last_name,COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name,AVG(age),COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name,age
FROM users
WHERE last_name='곽';

SELECT *
FROM users
LIMIT 5;

SELECT last_name,COUNT(last_name)
FROM users
WHERE COUNT(last_name)>100
GROUP BY last_name;

SELECT last_name,COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name)>100;
