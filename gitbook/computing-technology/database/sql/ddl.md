# DDL

## DDL (Data Definition Language, 데이터 정의어)란?

- 데이터베이스의 테이블, 인덱스, 뷰 등의 구조를 관리하는 SQL 명령어
- 데이터를 저장하는 형식과 구조를 설정하는 역할을 수행하는 SQL의 하위 집합

---

## CREATE (객체 생성)

- 데이터베이스의 객체(테이블, 인덱스, 뷰, 스키마 등)를 생성하는 명령어
- 데이터를 저장할 테이블의 구조를 정의할 때 사용된다.
- 테이블의 각 컬럼의 데이터 타입과 제약 조건을 설정할 수 있다. 

~~~sql
CREATE TABLE 테이블명 (
    컬럼1 데이터타입 [제약조건],
    컬럼2 데이터타입 [제약조건],
    ...
);
~~~

~~~sql
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    city VARCHAR(50)
);
~~~

✔️ 테이블뿐만 아니라 INDEX, VIEW, SCHEMA 등을 생성할 수도 있다.

---

## ALTER (객체 수정)

- 기존 테이블이나 데이터베이스 객체의 구조를 변경하는 명령어
- 컬럼 추가, 삭제, 데이터 타입 변경, 제약 조건 변경 등이 가능

~~~sql
ALTER TABLE 테이블명 ADD 컬럼명 데이터타입;
ALTER TABLE 테이블명 DROP COLUMN 컬럼명;
ALTER TABLE 테이블명 MODIFY COLUMN 컬럼명 새로운_데이터타입;
~~~

~~~sql
-- 컬럼 추가
ALTER TABLE Customers ADD email VARCHAR(100);

-- 컬럼 삭제
ALTER TABLE Customers DROP COLUMN city;

-- 데이터 타입 변경
ALTER TABLE Customers MODIFY COLUMN age SMALLINT;
~~~

✔️ 기존 데이터를 유지하면서 테이블 구조를 변경할 수 있다.

---

## DROP (객체 삭제)

- 테이블, 인덱스, 뷰 등 데이터베이스 객체를 완전히 삭제하는 명령어
- 삭제된 데이터는 복구할 수 없음(ROLLBACK 불가능)
- 테이블을 삭제하면 관련된 모든 데이터와 인덱스도 삭제된다.

~~~sql
DROP TABLE 테이블명;
DROP DATABASE 데이터베이스명;
DROP INDEX 인덱스명;
DROP VIEW 뷰명;
~~~

~~~sql
-- Customers 테이블 삭제
DROP TABLE Customers;

-- 특정 데이터베이스 삭제
DROP DATABASE ShopDB;
~~~

✔️ 데이터와 테이블 구조가 완전히 제거된다.
✔️ DROP과 다르게 TRUNCATE는 테이블 구조를 유지하면서 데이터만 삭제한다.

---

## TRUNCATE

---

## DDL과 트랜잭션

---

## DDL 명령어 비교

---

## DDL과 DML의 차이