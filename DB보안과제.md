![[Pasted image 20241018090610.png]]
## \[취약한 Wordpress 서버 구축]
![[Pasted image 20241018091050.png]]
![[Pasted image 20241018091334.png]]
### 1. docker 환경 구축
![[Pasted image 20241018091650.png]]
### 2. docker 환경 설정 파일
```yml
version: '3.1'

services:

  wordpress:
    image: wordpress:4.7-php5.6-apache  # PHP 5.6과 워드프레스 4.7이 포함된 이미지
    restart: always
    ports:
      - 8080:80  # 워드프레스 컨테이너에서 포트 80을 호스트의 포트 8080으로 연결
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: exampleuser
      WORDPRESS_DB_PASSWORD: examplepass
      WORDPRESS_DB_NAME: exampledb
    volumes:
      - ./wordpress_data:/var/www/html  # 워드프레스 파일이 저장될 경로

  db:
    image: mariadb:10.5  # MariaDB 10.5 이미지 사용
    restart: always
    environment:
      MARIADB_DATABASE: exampledb
      MARIADB_USER: exampleuser
      MARIADB_PASSWORD: examplepass
      MARIADB_ROOT_PASSWORD: rootpass
    volumes:
      - ./db_data:/var/lib/mysql  # MariaDB 데이터베이스 파일 저장 경로

  phpmyadmin:
    image: phpmyadmin/phpmyadmin  # phpMyAdmin 컨테이너
    restart: always
    ports:
      - 8081:80  # phpMyAdmin 포트 8081에서 실행
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: rootpass

```
### 3. 실행
```sh
docker compose up -d
```
![[Pasted image 20241018092214.png]]
### 4. wordpress 설정
![[Pasted image 20241018092358.png]]![[Pasted image 20241018092452.png]]![[Pasted image 20241018092518.png]]
## \[DB 보안 설정]
### 1-1. DB 접속
---
#### 1.1. DB 실행 여부 확인
![[Pasted image 20241018092850.png]]
- mariadb:10.5 실행 확인

#### 1.2. DB 접속
```sh
# docker exec -it <컨테이터_이름> mysql -u<DB계정> -p
docker exec -it wordpress-db-1 mysql -uroot -p
```
- root/rootpass

### 1-2. 웹 DB 접속
---
```
http://192.168.56.125:8081/
```
- 비밀번호는 이전과 동일
![[Pasted image 20241018093734.png]]
### 2. 계정 생성
> [!조건_1]
> test, 1234 - 192.168.56.125 에서 접속 가능하도록 사용자 생성
> 워드프레스 DB의 모든 권한 설정
```sql
grant all privileges on *.* to 'test'@'192.168.56.125' identified by '1234';
```

> [!조건_2]
> local에서 접속 가능한 본인 이름의 사용자 생성
```sql
create user 'jaeho'@'localhost' identified by 'choa0306@@';
```

> [!조건_3]
> test1, 9876 사용자에 대한 권한 설정 및 제거
```sql
grant all privileges on *.* to 'test1'@'%' identified by '9876';
```
![[Pasted image 20241018095035.png]]
```sql
revoke all on *.* from 'test1'@'%';
```
![[Pasted image 20241018095232.png]]

> [!조건_4]
> test2, 4321 사용자의 패스워드를 5678로 변경
```sql
create user 'test2'@'localhost' identified by '4321';
```
```sql
ALTER USER 'test2'@'localhost' IDENTIFIED BY '5678';
```

- DB 적용
```sql
flush privileges;
```

### 3. 시스템 메모리 관리
```sh
grep MemTotal /proc/meminfo
grep SwapTotal /proc/meminfo
```
![[Pasted image 20241018100301.png]]

### 4. DB 메모리 확인
#### 4.1. 명령어
1. 메모리 설정 변수 확인
```sql
SHOW VARIABLES LIKE '%buffer%';
```
![[Pasted image 20241018100808.png]]
2. 실제 사용량 확인
```sql
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_bytes%';
```
![[Pasted image 20241018101003.png]]
- `Innodb_buffer_pool_bytes_data`는 실제 데이터가 차지하는 메모리의 바이트 수.
- `Innodb_buffer_pool_bytes_free`는 사용 가능한 여유 메모리의 바이트 수.

#### 4.2. PMM 사용
> [!기본 설정]
> wordpress (192.168.56.125) = PMM-Agent
> PMM-server (192.168.56.126) = PMM-Server

