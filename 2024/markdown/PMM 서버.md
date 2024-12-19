Percona Monitoring & Management

# 설치 방법
- 소스 코드
- 패키지 관리자 (클라이언트)
- docker (서버)

# 서버 설치
## docker 설치
---
```sh
dnf update -y
dnf install -y docker
```
## 이미지 설치
---
```sh
docker pull percona/pmm-server:latest
```
![[Pasted image 20241017091129.png]]
```sh
docker images
```
## 볼륨 생성
---
```sh
docker volume create pmm-data
```
## 실행 중인 도커 이미지 확인
---
```sh
docker ps
docker ps -a
```
## 이미지 실행
---
```sh
docker run --detach --restart always --publish 443:443 -v pmm-data:/srv --name pmm-server docker.io/percona/pmm-server:latest
```
![[Pasted image 20241017092139.png]]
![[Pasted image 20241017092405.png]]
- 기본 admin/admin
# Agent 설정
## pmm 패키지 설치
---
```sh
dnf install -y https://repo.percona.com/yum/percona-release-latest.noarch.rpm
dnf install -y pmm2-client
pmm-admin --version
```
![[Pasted image 20241017094716.png]]![[Pasted image 20241017094745.png]]
## Node 등록
---
```sh
pmm-admin config --server-insecure-tls --server-url=https://admin:choa0306@@@192.168.56.123:443
```
![[Pasted image 20241017100253.png]]
## DB 서버
---
### pmm agent 설정 파일
```sh
vi /usr/local/percona/pmm2/config/pmm-agent.yaml
```
![[Pasted image 20241017100751.png]]
### DB 설치 여부 확인
```sh
dnf install -y mariadb
systemctl start mariadb
mysql -u root -p
```
### pmm 계정 생성
```sql
CREATE USER 'pmm'@'127.0.0.1' IDENTIFIED BY '1234' WITH MAX_USER_CONNECTIONS 10;
```
### 계정 권한 할당
```sql
grant select, process, super, replication client, reload, show view on *.* to 'pmm'@'127.0.0.1';
grant select, update, drop, delete on performance_schema.* to 'pmm'@'127.0.0.1';
flush privileges;
show grants for 'pmm'@'127.0.0.1';
```
### 설정 파일 내용 추가
```sh
vi /usr/local/percona/pmm2/config/pmm-agent.yaml
```
```yaml
slow_query_log = ON
slow_query_log_file = /log/slow_query.log
long_query_time = 1
log_output = FILE
performance_schema = ON
```
### pmm-server 연동
```sh
pmm-admin add mysql --query-source=perfschema --username=pmm --password=1234
```

```
pmm-admin add mysql --query-source=perfschema --username=pmm --password=1234 --host=wordpress-db-1 --port=3306

docker network create mynetwork
docker run -d --name mariadb --network=mynetwork -e MYSQL_ROOT_PASSWORD=rootpass mariadb
docker run -d --name pmm-client --network=mynetwork percona/pmm-client:latest

docker start wordpress-db-1
```
