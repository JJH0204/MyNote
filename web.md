# [[리눅스]]에서 웹 서버 구축
```sh
[root@localhost home]# dnf install httpd -y  // 툴 설치
[root@localhost home]# systemctl start httpd // 툴 실행
[root@localhost home]# cd /var/www/html
[root@localhost html]# vi index.html
[root@localhost html]# ls -al
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