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
