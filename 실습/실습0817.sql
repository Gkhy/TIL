-- SQLite
SELECT count(*) FROM users WHERE age>=30;
SELECT first_name FROM users WHERE age>=30;
SELECT first_name FROM users WHERE age>=30 LIMIT 3;
SELECT age, first_name FROM users WHERE age>=30 and last_name='김';
SELECT count(*) FROM users WHERE age>=30;
SELECT MIN(age) FROM users;
SELECT MIN(age) FROM users WHERE last_name ='이';
SELECT MIN(age),first_name,balance FROM users WHERE last_name ='이';
SELECT AVG(age) FROM users WHERE age>=30;
SELECT MAX(balance),first_name FROM users;

SELECT COUNT(*) FROM users WHERE phone LIKE '02_%';
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

select first_name from users order by age ASC LIMIT 10;
SElect *FROM users order by age, last_name limit 10;
SELECT last_name,first_name,balance FROM users order by balance desc limit 10;
select last_name,first_name,balance fRom users ORDER BY balance DESC,last_name ASC LIMIT 10;