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
```
vi student.sql
'''
TABLE IF EXISTS `student`;            // student라는 이름의 테이블 존제 확인
CREATE TABLE `student` (              // 없으면 생성(각 칼럼의 설정 값)
  `id` tinyint(4) NOT NULL,
  `name` char(4) NOT NULL,
  `sex` enum('남자','여자') NOT NULL,
  `address` varchar(50) NOT NULL,
  `distance` INT NOT NULL,
  `birthday` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
// 데이터 삽입 명령어
INSERT INTO `student` VALUES (2, '박재숙', '남자', '서울',  10, '1985-10-26 00:00:00');
INSERT INTO `student` VALUES (1, '이숙경', '여자', '청주', 200, '1982-11-16 00:00:00');
INSERT INTO `student` VALUES (3, '백태호', '남자', '경주', 350, '1989-2-10 00:00:00');
INSERT INTO `student` VALUES (4, '김경훈', '남자', '제천', 190, '1979-11-4 00:00:00');
INSERT INTO `student` VALUES (8, '김정인', '남자', '대전', 200, '1990-10-1 00:00:00');
INSERT INTO `student` VALUES (6, '김경진', '여자', '제주', 400, '1985-1-1 00:00:00');
INSERT INTO `student` VALUES (7, '박경호', '남자', '영동', 310, '1981-2-3 00:00:00');
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
```
select * from student order by distance asc;
```
![[Pasted image 20241016094635.png]]

## 연산자
### 집계 함수
sum, avg, max, min, count, stdev(표준편차), ...

### 조건 함수
having (조건)
```
select sex, distance from student group by sex order by sum(distance) desc;
```