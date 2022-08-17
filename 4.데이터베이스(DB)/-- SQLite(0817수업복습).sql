-- SQLite
SELECT * FROM users;

Q.users 테이블에서 
age가 30이상, 성이 '김'인 사람의 
나이와 이름만 조회하려면?
SELECT age, first_name FROM users WHERE age>=30 and last_name="김";

SELECT COUNT(*) FROM users;

SELECT AVG(age) FROM users WHERE age>=30;

SELECT first_name, MAX(balance) FROM users;

SELECT AVG(balance) FROM users WHERE age>=30;

SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE age>=20 and age<30;

SELECT * FROM users WHERE phone LIKE '02-%';

SELECT * FROM users WHERE first_name LIKE '%준';

SELECT * FROM users WHERE phone LIKE '%-5114-%';

SELECT * FROM users ORDER BY age ASC LIMIT 10;

SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

