![[Pasted image 20241016120503.png]]
```sql
DROP TABLE IF EXISTS 'Student_Info';
DROP TABLE IF EXISTS 'Student_Score';
DROP TABLE IF EXISTS 'Student_Health';

CREATE TABLE 'Student_Info' (
	'S_ID' tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
	'S_NAME' varchar(20) NOT NULL ,
	'S_ADDR' varchar(20) NOT NULL ,
	'S_AGE' tinyint UNSIGNED NOT NULL ,
	PRIMARY KEY (`S_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE 'Student_Score' (
	'S_ID' tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
	'S_NETWORK' tinyint UNSIGNED NOT NULL ,
	'S_SERVER' tinyint UNSIGNED NOT NULL ,
	'S_SECURITY' tinyint UNSIGNED NOT NULL ,
	PRIMARY KEY (`S_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE 'Student_Health' (
	'H_ID' tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
	'S_VISION' float NOT NULL,
	'S_WEIGHT' tinyint UNSIGNED NOT NULL ,
	'S_STATURE' tinyint UNSIGNED NOT NULL ,
	'S_BLOOD_TYPE' char(4) NOT NULL,
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

INSERT INTO `Student_Health` VALUES (1, 1.0, 80, 176, '');
```