- [공식사이트](https://www.zabbix.com/)

## 구축과정
---
```
 dnf install -y httpd php php-mysqli mariadb-server
 dnf install -y php-fpm # fpm-fcgi
```

#### 외부 저장소 추가 후 설치
```
rpm -Uvh https://repo.zabbix.com/zabbix/7.0/alma/9/x86_64/zabbix-release-7.0-2.el9.noarch.rpm
[root@Linux2 yum.repos.d]# ls
rocky-addons.repo  rocky-devel.repo  rocky-extras.repo  rocky.repo  zabbix.repo
# 설치된 것을 확인 가능
```
```
dnf clean all
```

#### 프로그램 설치
```
dnf install zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-sql-scripts zabbix-selinux-policy zabbix-agent

firewall-cmd --permanent --add-service=http
firewall-cmd --reload

systemctl start httpd mariadb
systemctl enable httpd mariadb

mysql_secure_installation

```

#### DB 세팅
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


```
cd /usr/share/zabbix-sql-scripts/mysql/

# DB 생성 스크립트 실행하며 함께 설정 값 전달
zcat ./server.sql.gz | mysql --default-character-set=utf8mb4 -u [사용자 이름] -p '사용자 비번' [적용할 DB]

```