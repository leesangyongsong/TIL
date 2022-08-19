# 📚 0819 데이터베이스(DB)

## 📌 CASE
```SQL
1. CASE
  - CASE문은 특정 상황에서 데이터를 변환하여 활용할 수 있음
  - ELSE를 생략하는 경우 NULL값이 지정됨

  CASE
    WHEN 조건식 THEN 식
    WHEN 조건식 THEN 식
    ELSE 식
  END

  Q. gender가 1인 경우는 남자를,
     gender가 2인 경우에는 여자를 출력하시오.
  A.
    SELECT
      id,
      CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
      END
    FROM healthcare
    LIMIT 3;

  Q. 나이에 따라
      청소년(~18), 청년(~30), 중장년(~64)로 출력하시오.
  A. 
    SELECT
      last_name,
      age
      CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 30 THEN '청년'
        WHEN age <= 64 THEN '중장년'
      END
    FROM users
    LIMIT 15;

2. 서브쿼리
  -- 서브쿼리란?
  - 서브쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것
  - 실제 테이블에 없는 기준을 이용한 검색이 가능함
  - 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 
    모두 사용할 수 있음
  - 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음

  -- 서브쿼리의 종류
  1) 단일행 서브쿼리
    - 서브쿼리의 결과가 0 또는 1개인 경우
    - 단일행 비교 연산자와 함께 사용 (=, <, <=, >=, >, <>)

  2) 다중행 서브쿼리
    - 서브쿼리 결과가 2개 이상인 경우
    - 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)

  3) 다중컬럼 서브쿼리

  -- 단일행 서브쿼리 - WHERE에서의 활용
  Q. users에서 가장 나이가 적은 사람의 수는?
  A. 
    -- 1
    SELECT COUNT(*) 
    FROM users 
    GROUP BY age 
    ORDER BY age 
    LIMIT 1;

    -- 2
    SELECT COUNT(*)
    FROM users
    WHERE age = (SELECT MIN(age) FROM users);

  Q. users에서 평균 계좌 잔고가 높은 사람의 수는?
  A.
    SELECT COUNT(*) 
    FROM users
    WHERE balance > (SELECT AVG(balance) FROM users);

  Q. users에서 유은정과 같은 지역에 사는 사람의 수는?
  A. 
    -- 1
    SELECT 
      country,
      last_name,
      first_name
    FROM users
    WHERE last_name = '유' AND first_name= "은정"

    -- 2
    SELECT
      COUNT(*)
    FROM users
    WHERE country = (
      SELECT country
      FROM users
      WHERE last_name = '유' AND first_name = '은정');

  -- 단일행 서브쿼리 - SELECT에서의 활용
  Q. 전체 인원과 평균 연봉, 평균 나이를 출력하세요.
  A.
    -- 1
    SELECT 
      COUNT(*), 
      AVG(balance), 
      AVG(age)
    FROM users;

    -- 2
    SELECT
      (SELECT COUNT(*) FROM users) AS 총인원,
      (SELECT AVG(balance) FROM users) AS 평균연봉,
      (SELECT AVG(age) FROM users) AS 평균나이
    ;

  -- 단일행 서브쿼리 - UPDATE에서의 활용
  UPDATE users
  SET balance = (SELECT AVG(balance) FROM users);

  -- 다중행 서브쿼리
  Q. users에서 이은정과 같은 지역에 사는 사람의 수는?
  A. 
    SELECT COUNT(*)
    FROM users
    WHERE country IN (
      SELECT country
      FROM users
      WHERE first_name = '은정' AND last_name = '이'
    );

  -- 다중칼럼 서브쿼리
  Q. 특정 성씨에서 가장 어린 사람들의 이름과 나이
  A.
    -- 1
    SELECT
      last_name,
      MIN(age)
    FROM users
    GROUP BY last_name;

    -- 2
    SELECT
      last_name,
      first_name,
      age
    FROM users
    WHERE (last_name, age) IN (
      SELECT
        last_name,
        min(age)
      FROM users
      GROUP BY last name)
    ORDER BY last_name;
```