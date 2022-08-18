-- SQLite
1.
SELECT smoking, COUNT(*)
FROM healthcare
GROUP BY smoking;

2.
SELECT is_drinking, COUNT(*)
FROM healthcare
GROUP BY is_drinking;

3.
SELECT is_drinking, COUNT(*)
FROM healthcare
WHERE blood_pressure>=200 AND blood_pressure != '' AND is_drinking != ''
GROUP BY is_drinking;

4. 
SELECT sido, COUNT(*)
FROM healthcare
GROUP BY sido
HAVING COUNT(*) >= 50000;

5.
SELECT height, COUNT(*)
FROM healthcare
GROUP BY height
ORDER BY COUNT(*)
DESC LIMIT 5;

6. 
SELECT weight, height, COUNT(*)
FROM healthcare
GROUP BY height, weight

7. 
SELECT is_drinking, AVG(waist), COUNT(*)
FROM healthcare
GROUP BY is_drinking

8. 
SELECT gender, AVG(va_left), AVG(va_right)
FROM healthcare
GROUP BY gender

9.
SELECT age, AVG(height), AVG(weight)
FROM healthcare
GROUP BY age

10.
SELECT 
