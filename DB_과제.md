![[Pasted image 20241016120503.png]]
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

---
![[Pasted image 20241016123137.png]]
![[Pasted image 20241016123204.png]]
![[Pasted image 20241016123220.png]]

---
## S_AGE를 기준으로 오름차순 정렬
![[Pasted image 20241016123522.png]]
## S_SECURITY를 기준으로 내림차순 정렬
![[Pasted image 20241016123606.png]]

## S_WEIGHT값이 70이상인 것에 대해 오름차순 정렬
![[Pasted image 20241016124016.png]]

## S_NAME union S_SECURITY 데이터 출력
![[Pasted image 20241016125003.png]]
## Student_Info Left join / Right join / inner join > Student_Score

## S_NETWORK 점수 합계 구하기
![[Pasted image 20241016131217.png]]

## S_SECURITY 평균 점수 구하기
![[Pasted image 20241016131314.png]]

## S_BLOOD_TYPE을 기준으로 중복 데이터 제거하기
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

## 5번 학생의 과목 합계와 평균 구하기


