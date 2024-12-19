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
1. PMM-server 구성
![[Pasted image 20241018102241.png]]
![[Pasted image 20241018102329.png]]
2. PMM-Agent 구성
![[Pasted image 20241018102547.png]]
3. node 연결
```sh
 pmm-admin config --server-insecure-tls --server-url=https://admin:choa0306@@@192.168.56.126:443
```
![[Pasted image 20241018102654.png]]
4. pmm 계정 생성
```sql
CREATE USER 'pmm'@'127.0.0.1' IDENTIFIED BY '1234' WITH MAX_USER_CONNECTIONS 10;
grant select, process, super, replication client, reload, show view on *.* to 'pmm'@'127.0.0.1';
grant select, update, drop, delete on performance_schema.* to 'pmm'@'127.0.0.1';
flush privileges;
show grants for 'pmm'@'127.0.0.1';
```
![[Pasted image 20241018102859.png]]
5. Agent 설정 추가
![[Pasted image 20241018103039.png]]
6. Agent 실행


## \[WAF]


# CTF_Momentum2
## \[정보 수집]
![[Pasted image 20241018162608.png]]
```sh
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http://192.168.56.128/ -x html,php,bak,txt,php.bak
```
![[Pasted image 20241018174442.png]]

- docker 설치
```
sudo dnf remove docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-engine

# Docker의 공식 리포지터리 추가
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Docker 설치
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Docker 서비스 시작
sudo systemctl start docker

# Docker 부팅 시 자동 실행 설정
sudo systemctl enable docker

```

- 원터치
`docker-compose.yml`
```yml
version: '3.1'

services:

  wordpress:
    image: wordpress:4.7-php5.6-apache  # PHP 5.6과 워드프레스 4.7이 포함된 이미지
    container_name: wordpress
    restart: always
    ports:
      - 8080:80  # 워드프레스 컨테이너에서 포트 80을 호스트의 포트 8080으로 연결
    environment:
      WORDPRESS_DB_HOST: wordpress_db
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: rootpass
      WORDPRESS_DB_NAME: WordpressDB
	networks:
	  - wp_network
    volumes:
      - ./wordpress_data:/var/www/html  # 워드프레스 파일이 저장될 경로

  wordpress_db:
    image: mariadb:10.5  # MariaDB 10.5 이미지 사용
    container_name: wordpress_db
    restart: always
    environment:
      MARIADB_DATABASE: WordpressDB
      MARIADB_USER: root
      MARIADB_PASSWORD: rootpass
      MARIADB_ROOT_PASSWORD: rootpass
    networks:
	  - wp_network
    volumes:
      - ./db_data:/var/lib/mysql  # MariaDB 데이터베이스 파일 저장 경로

  phpmyadmin:
    image: phpmyadmin/phpmyadmin  # phpMyAdmin 컨테이너
    restart: always
    ports:
      - 8081:80  # phpMyAdmin 포트 8081에서 실행
    environment:
      PMA_HOST: wordpress_db
      MYSQL_ROOT_PASSWORD: rootpass

  waf-proxy:
    build: ./waf-proxy 
    container_name: waf-proxy
    ports: 
      - "8080:80" 
    networks: 
      - wp_network 

  pmm-client: 
    image: percona/pmm-client:latest 
    container_name: pmm-client 
    environment: 
      PMM_SERVER: "192.168.56.126" # PMM 서버의 IP 주소 
    command: /bin/bash -c "while true; do sleep 1000; done"
    networks: 
      - wp_network

networks: 
  wp_network: 
    driver: bridge
```

- selinux를 꺼보자
- 