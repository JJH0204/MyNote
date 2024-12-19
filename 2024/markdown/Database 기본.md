# 언어 구조
- DDL(Definition) - 데이터 정의어
	- create, alter, drop, truncate, rename, ...
- DML(Manipulation) - 데이터 조작어
	- select, insert, update, delete, ...
- DCL(Control) - 데이터 제어어
	- grant, revoke, ...
- TCL(Transaction) - 트랜잭션 제어어
	- commit, rollback, savepoint, ...

# CRUD
C-Create: 데이터 생성(insert)
R-Read: 데이터 읽기(select)
U-Update: 데이터 갱신(update)
D-Delete: 데이터 삭제(delete)

# 실습
```
mysql -u root
create database school;
```
![[Pasted image 20241016091955.png]]
```sql
vi student.sql
'''
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` tinyint(4) NOT NULL,
  `name` char(4) NOT NULL,
  `sex` enum('남자','여자') NOT NULL,
  `location_id` tinyint(4) NOT NULL,
  `birthday` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
DROP TABLE IF EXISTS `location`;
CREATE TABLE `location` (
`id`  tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
`name`  varchar(20) NOT NULL ,
`distance`  tinyint UNSIGNED NOT NULL ,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;;

INSERT INTO `location` VALUES (1, '서울', 10);
INSERT INTO `location` VALUES (2, '청주', 200);
INSERT INTO `location` VALUES (3, '경주', 255);
INSERT INTO `location` VALUES (4, '제천', 190);
INSERT INTO `location` VALUES (5, '대전', 200);
INSERT INTO `location` VALUES (6, '제주', 255);
INSERT INTO `location` VALUES (7, '영동', 255);
INSERT INTO `location` VALUES (8, '광주', 255);
INSERT INTO `student` VALUES (1, '이숙경', '여자', 1, '1982-11-16 00:00:00');
INSERT INTO `student` VALUES (2, '박재숙', '남자', 2, '1985-10-26 00:00:00');
INSERT INTO `student` VALUES (3, '백태호', '남자', 3, '1989-2-10 00:00:00');
INSERT INTO `student` VALUES (4, '김경훈', '남자', 4, '1979-11-4 00:00:00');
INSERT INTO `student` VALUES (6, '김경진', '여자', 5, '1985-1-1 00:00:00');
INSERT INTO `student` VALUES (7, '박경호', '남자', 6, '1981-2-3 00:00:00');
INSERT INTO `student` VALUES (8, '김정인', '남자', 5, '1990-10-1 00:00:00');
'''

mysql -u root
use school;
source /root/student.sql;
```
![[Pasted image 20241016092611.png]]
```
desc student;
```
![[Pasted image 20241016092658.png]]
```
select * from student;
```
![[Pasted image 20241016092730.png]]

```
mysql -u root -p toor --host=localhost < /root/student.sql

vi sql.sh
'''
#!/bin/bash
mysql -u root -p toor --host=localhost < /root/student.sql
'''
./sql.sh

cat /root/student.sql | mysql -u root -p toor
```

## Group by
```
select * from student;
select sex from student group by sex;
select sex, sum(distance), avg(distance) from student group by sex;
```
![[Pasted image 20241016094130.png]]
- 첫 번째 칼럼을 기준으로 그룹화 진행

## Order by
### 내림차순
```
select * from student order by distance desc;
```
![[Pasted image 20241016094600.png]]

### 오름차순
```sql
select * from student order by distance asc;
```
![[Pasted image 20241016094635.png]]

```sql
select sex, distance from student group by sex order by sum(distance) desc;
```
![[Pasted image 20241016095252.png]]
```sql
select * from student order by name desc;
```
![[Pasted image 20241016095301.png]]

## 연산자
### 집계 함수
sum, avg, max, min, count, stdev(표준편차), ...

### 조건 함수
having (조건)

## 인덱싱
primary: 중복 x
normal: 중복 허용
unique: 중복 
foreign: 테이블 관계성 부여
full test: 자연어 검색

```sql
desc student;
```
![[Pasted image 20241016100542.png]]
```sql
select * from student where id=3;
```
![[Pasted image 20241016100643.png]]
```sql
select * from student where birthday='1982-11-16 00:00:00';
```
![[Pasted image 20241016100802.png]]
```sql
select * from student where sex='남자';
```
![[Pasted image 20241016100920.png]]
- 중복이 허용되는 인덱싱은 normal 인덱싱

```sql
desc location;
```
![[Pasted image 20241016101649.png]]
```sql
select * from location;
```
![[Pasted image 20241016101729.png]]
## SQL Join
![[Pasted image 20241016101843.png]]
### OUTER JOIN
### INNER JOIN
```sql
select * from student inner join location on student.location_id=location.id;
```
![[Pasted image 20241016103608.png]]
- 좀 더 이쁘게 칼럼 출력
```sql
select student.name, student.sex, student.birthday, location.name, location.distance from student inner join location on student.location_id=location.id;
```
![[Pasted image 20241016103804.png]]

### LEFT JOIN
### RIGHT JOIN

