-- SQLite
CREATE TABLE users (
  id INT PRIMARY KEY,
  name TEXT,
  role_id INT
);

INSERT INTO users VALUES
  (1, '관리자', 1),
  (2, '김철수', 2),
  (3, '이영희', 2);

CREATE TABLE role (
  id INT PRIMARY KEY,
  title TEXT
);

INSERT INTO role VALUES
  (1, 'admin'),
  (2, 'staff'),
  (3, 'student');

CREATE TABLE articles (
  id INT PRIMARY KEY,
  title TEXT,
  content TEXT,
  user_id INT
);

INSERT INTO articles VALUES
  (1, '1번글', '111', 1),
  (2, '2번글', '222', 2),
  (3, '3번글', '333', 1),
  (4, '4번글', '444', NULL);

-- 확인
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;

-- INNER JOIN
SELECT * FROM users INNER JOIN role
ON users.role_id = role.id;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- 스태프(2)만 출력
SELECT * FROM users INNER JOIN role
ON users.role_id = role.id
WHERE role.id = 2;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- 이름을 내림차순으로 출력하세요.
SELECT * FROM users INNER JOIN role
ON users.role_id = role.id
ORDER BY users.name DESC;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin

-- LEFT OUTER JOIN
SELECT * FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

-- LEFT OUTER JOIN(NULL X)
SELECT * FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1

-- FULL OUTER JOIN
SELECT * FROM articles FULL OUTER JOIN users
ON articles.user_id = users.id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444
--                              3   이영희   2

-- CROSS JOIN
SELECT * FROM articles CROSS JOIN users;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 1   1번글    111      1        2   김철수   2
-- 1   1번글    111      1        3   이영희   2
-- 2   2번글    222      2        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 2   2번글    222      2        3   이영희   2
-- 3   3번글    333      1        1   관리자   1
-- 3   3번글    333      1        2   김철수   2
-- 3   3번글    333      1        3   이영희   2
-- 4   4번글    444               1   관리자   1
-- 4   4번글    444               2   김철수   2
-- 4   4번글    444               3   이영희   2