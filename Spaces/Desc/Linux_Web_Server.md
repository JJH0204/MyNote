# [[리눅스 일반]]에서 웹 서버 구축


```sh
[root@localhost home]# dnf install httpd mariadb php -y  // 툴 설치
[root@localhost home]# systemctl start httpd // 툴 실행
[root@localhost home]# cd /var/www/html
[root@localhost html]# vi index.html
[root@localhost html]# ls -al
```

## systemctl
---
```sh
[root@localhost home]# systemctl start httpd // 툴 실행
[root@localhost home]# systemctl enable httpd // 설정적용
# status, stop, restart, disable 등 추가 명령어 들
```


## index.html
---
```html
<html>
        <body>
                welcome to jjh's Site!!!
        </body>
</html>
```