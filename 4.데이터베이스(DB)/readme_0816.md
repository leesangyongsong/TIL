# 📚 0816 데이터베이스(DB)

## 📌 Database
```python
# Database란?
- '체계화된 데이터'의 모임
- 여러 사람이 공유하고 사용할 목적으로 
  통합 관리되는 정보의 집합
- 논리적으로 연관된 (하나 이상의) 자료 모음으로
  그  내용을 고도로 구조화함으로써
  검색과 갱신의 효율화를 꾀한 것
- 즉, '몇 개의 자료 파일을 조직적으로 통합하여
  자료 항목의 중복을 없애고 자료를 구조화하여 
  기억시켜놓은 자료의 집합체' 

# 데이터베이스로 얻는 장점들
- 데이터 중복 최소화
- 데이터 무결성(정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지

# 관계형 데이터베이스(RDB, Relational Database)
: 서로 관련된 데이터를 저장하고 접근할 수 있는 DB 유형,
  키(Key)와 값(Value)들의 관계를 표로 정리한 DB

# 관계형 데이터베이스의 종류
1. 스키마(schema)
: 데이터베이스에서 자료의 구조, 표현방법, 관계 등
  전반적인 '명세를 기술'한 것

2. 테이블(table)
: 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 
  조직된 데이터 요소들의 집합

  - 열(column)
  : 각 열에 고유한 데이터 형식 지정

  - 행(row)
  : 실제 데이터가 저장되는 형태

  - 기본키(Primary Key)
  : 각 행(레코드)의  고유  값
    반드시 설정해야 하며, 데이터베이스 관리 및 
    관계 설정 시 주요하게 활용됨

# 관계형 데이터베이스 관리 시스템(RDBMS)
: 관계형 모델을 기반으로 하는 데이터베이스 관리시스템

# 관계형 데이터베이스 관리 시스템(RDBMS)의 종류
1. SQLite
- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 
  넣어서 사용하는 '비교적 가벼운 데이터베이스'
- 구글 안드로이드 운영체제에 기본적으로 탑재된 DB이며,
  임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB구성을 할 수 있으며,
  오픈소스 프로젝트이기 때문에 자유롭게 사용가능

2. ORACLE
3. MYSQL
4. PostgreSQL
5. SQLServer

# SQLite Data Type
1. NULL
2. INTEGER
  : 크기에 따라 0, 1, 2, 3, 4, 6 또는
    8바이트에 저장된 부호 있는 정수
3. REAL
  : 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB
  : 입력된 그대로 정확히 저장된 데이터
    (별다른 타입 없이 그대로 저장)

# Sqlite Type Affinity (1/2)
: 특정 컬럼에 저장하도록 권장하는 데이터 타입
1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC
```

## 📌 SQL
```python
# SQL(Structured Query Language)이란?
- 관계형 데이터베이스 관리시스템의 '데이터 관리'를 위해
  '특수 목적으로 설계된 프로그래밍 언어'
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

# SQL의 분류
1. 데이터 정의 언어-DDL(Date Definition Language)
: 관계형 데이터베이스 구조(테이블, 스키마)를 
  정의하기 위한 명령어

2. 데이터 조작 언어-DML(Date Manipulation Language)
: 데이터 저장, 조회, 수정, 삭제 등을 하기 위한 명령어

3. 데이터 제어 언어-DCL(Data Control Language)
: DB 사용자의 권한 제어를 위해 사용하는 명령어

# SQL Keywords - Date Manipulation Language
- INSERT: 새로운 데이터 삽입(추가)
- SELECT: 저장되어 있는 데이터 조회
- UPDATE: 저장되어 있는 데이터 갱신
- DELETE: 저장되어 있는 데이터 삭제

# 테이블 생성 및 삭제
1. 데이터베이스 생성하기
  $ sqlite3 tutorial.sqlite3
  sqlite> .database 
  # '.'은 sqlite에서 활용되는 명령어

2. CSV 파일을 table로 만들기
  sqlite> .mode csv
  sqlite> .import hellodb.csv exmaples
  sqlite> .tables
  examples

3. SELECT로 조회(확인)하기
  SELECT * FROM examples;
  # SELECT문은 특정 테이블의 레코드(행) 정보를 반환!

4. (Optional) 터미널 view 변경하기
  sqlite> .headers on
  sqlite> SELECT * FROM examples;

  sqlite> .mode column
  sqlite> SELECT * FROM examples;

# 테이블 생성 및 삭제 statement
- CREATE TABLE
  - 데이터베이스에서 테이블 생성

- DROP TABLE
  - 데이터베이스에서 테이블 제거

1. CREATE
  CREATE TABLLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
  );

2. 테이블 확인하기
  sqlite> CREATE TABLLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT
     ...> );
  sqlite> .tables
  classmates examples
  # CREATE는 테이블을 생성!

3. 특정 테이블의 schema 조회
  sqlite> .schema cllassmates
  CREATE TABLLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
  );

4. DROP
  sqlite> DROP TABLE classmates;
  sqlite> .tables
  exmaples

# 필드제약조건
- NOT NULL 
  : NULL 값 입력 금지
- UNIQUE 
  : 중복 값 입력 금지(NULL 값 중복 입력 가능)
- PRIMARY KEY 
  : 테이블에서 반드시 하나
- FOREIGN KEY
  : 외래키. 다른 테이블의 Key
- CHECK
  : 조건으로 설정된 값만 입력 허용
- DEFAULT
  : 기본 설정 값

# CRUD(Creat Read Update Delete)
1. Create
  1) INSERT
  - "Insert a single row into a table"
  - 테이블에 단일 행 삽입
  - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

2. READ
  1) SELECT
  - "query data from a table"
  - 테이블에서 데이터를 조회
  - SELECT 문은 SQLite에서 가장  기본이 되는 문이며,
    다양한 절(clause)와 함께 사용
  
  2) LIBIT
  - "constrain the number of rows 
    returned by a query"
  - 쿼리에서 반환되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 
    OFFSET 키워드와 함께 사용하기도 함

  3) WHERE
  - "specify the search condition 
    for rows returned by the query"
  - 쿼리에서 반환도니 행에 대한 특정 검색 조건을 지정

  4) SELECT DISTINCT
  - "remove duplicate rows in the result set"
  - 조회 결과에서 중복 행을 제거
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야함
```