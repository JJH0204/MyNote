- [공식사이트](https://www.zabbix.com/)

## 구축과정
---
```
dnf update -y && dnf install -y httpd php php-mysqli mariadb-server
dnf install -y php-fpm # fpm-fcgi
```

#### 외부 저장소 추가 후 설치
```
rpm -Uvh https://repo.zabbix.com/zabbix/7.0/alma/9/x86_64/zabbix-release-7.0-2.el9.noarch.rpm && dnf clean all
```

#### 프로그램 설치
```bash
dnf install -y zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-sql-scripts zabbix-selinux-policy zabbix-agent

firewall-cmd --permanent --add-service=http
firewall-cmd --reload

systemctl start httpd mariadb
systemctl enable httpd mariadb

mysql_secure_installation

```

#### DB 초기 세팅
```
# DB 접속
mysql -u root -p

# DB 생성
create database zabbix_db character set utf8 collate utf8_bin;

# 사용자 생성
create user 'zabbix_user'@'localhost' identified by '비밀번호';

# 사용자 권한 설정
grant all privileges on zabbix_db.* to 'zabbix_user'@'localhost' with grant option;

# 사용자에게 추가 지급할 권한(로그 생성 권한)
set global log_bin_trust_function_creators = 1;

# 권한 적용
flush privileges;
```

#### DB 생성
```
cd /usr/share/zabbix-sql-scripts/mysql/

# DB 생성 스크립트 실행하며 함께 설정 값 전달
zcat ./server.sql.gz | mysql --default-character-set=utf8mb4 -u[사용자 이름] -p'사용자 비번' [적용할 DB]

# DB 확인
mysql -u root -p
show databases; use zabbix_db; show tables;
```

#### 환경설정
```
cd /etc/zabbix

# 서버 설정 파일 수정
vi zabbix_server.conf

107 DBName=zabbix_db
123 DBUser=[DB 사용자 이름]
131 DBPassword=[사용자 패스워드]
:wq 

# 에이전트 파일 수정
vi zabbix_agentd.conf
117 Server=127.0.0.1
171 ServerActive=127.0.0.1
182 Hostname=Zabbix server
:wq 

systemctl start zabbix-server zabbix-agent
systemctl enable zabbix-server zabbix-agent
systemctl restart httpd php-fpm

```

#### php 설정(zabbix 연동)
```
vi /etc/php-fpm.d/www.conf

(추가)
440 php_value[max_execution_time] = 300
441 php_value[memory_limit] = 128M
442 php_value[post_max_size] = 16M
443 php_value[upload_max_filesize] = 2M
444 php_value[max_input_time] = 300
445 php_value[max_input_vars] = 10000
446 php_value[always_populate_raw_post_data] = -1
447 php_value[data.timezone] = Asia/Seoul
:wq

systemctl restart zabbix-agent httpd php-fpm
```

#### zabbix http 설정
```
cd /usr/share/zabbix
ls

mkdir /var/www/html/zabbix
cp -R /usr/share/zabbix/* /var/www/html/zabbix
cd /var/www/html/zabbix
ls
```

#### 웹 접속/설정
```
IP/zabbix
```
![[Pasted image 20240910143138.png]]
![[Pasted image 20240910143343.png]]
- 서버와 DB가 같은 장치에 설치되어 있는 경우 port 0 가능
![[Pasted image 20240910143629.png]]
![[Pasted image 20240910143750.png]]
- 설정에 문제가 있다면 etc/zabbix/web/zabbix.conf.php 에서 수정 가능
![[Pasted image 20240910143829.png]]
- id: Admin pw: zabbix

## 인터페이스
---
- SNMP를 통해 Agent와 NMS가 통신
- 이때 Agent-d 사용
- zabbix는 SNMP를 개선안 zbx 를 사용
![[Pasted image 20240910144806.png]]

## Agent add
---
https://www.zabbix.com/download_agents
![[Pasted image 20240910150624.png]]
- agent 추가를 위한 파일 설치
- 운영체제와 환경에 맞는 파일 설치

#### windows set
![[Pasted image 20240910151833.png]]
- 172.0.0.1 > 서버 IP로 수정
- LisenPort > 주석 해제
- Hostname > 원하는 이름으로 수정

zabbix_agentd.exe 실행(관리자 권한)
![[Pasted image 20240910160545.png]]

서비스 실행(services.msc 실행 후 Zabbix 서비스 실행)
![[Pasted image 20240910160654.png]]

방화벽 새 규칙 추가
![[Pasted image 20240910152956.png]]
- port > tcp > 10050 > 연결 허용 > 다음 > 이름 설정 > 마침

서버 포트 개방
![[Pasted image 20240910153414.png]]
- firewall-cmd --permanent --add-port=10051/tcp
- firewall-cmd --reload

#### CentOS linux set
zabbix 설치
```
cd /etc/yum.repos.d/
rpm -Uvh https://repo.zabbix.com/zabbix/7.0/alma/9/x86_64/zabbix-release-7.0-2.el9.noarch.rpm
dnf clean all
dnf install -y zabbix-agent
vi /etc/zabbix/zabbix_agentd.conf

systemctl start zabbix-agent
systemctl enable zabbix-agent
firewall-cmd --permanent --add-port=10050/tcp
firewall-cmd --reload
```

#### Ubuntu linux set
zabbix 설치
- repository 설정
```
wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_7.0-2+ubuntu24.04_all.deb
dpkg -i ./zabbix-release_7.0-2+ubuntu24.04_all.deb
```

- agent 설치
```
apt update
apt install -y zabbix-agent
```

- agent 설정 수정
```
vi /etc/zabbix/zabbix_agentd.conf
###
Server=#zabbix 서버 ip
ServerActive=#zabbix 서버 ip
Hostname=#원하는 이름
:wq 
###
```

- 서비스 재시작
```
systemctl start zabbix-agent
systemctl enable zabbix-agent

firewall-cmd --permanent --add-port=10050/tcp
firewall-cmd --reload
```
#### agent 추가
서버 접속
![[Pasted image 20240910153620.png]]
- 모니터링 > hosts > create host
![[Pasted image 20240910154033.png]]
- 윈도우 설정에 맞게 설정 값 입력
![[Pasted image 20240910161001.png]]
