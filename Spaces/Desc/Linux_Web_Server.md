# [[리눅스 일반]]에서 웹 서버 구축

```sh
[root@localhost home]# dnf install httpd mariadb php -y  // 툴 설치
[root@localhost home]# systemctl start httpd // 툴 실행
[root@localhost home]# cd /var/www/html // 
[root@localhost html]# vi index.html
[root@localhost html]# ls -al
```

## 포트 개방
---
```
firewall-cmd ~~
```
- `--list-all`: 방화벽 정보 출력
- `--permanent`: 재부팅 후에도 이후 명령어 적용(영구적용)
	- `--add-service=[서비스이름]`
- `--reload`: 방화벽 정책 변경 후 적용 (필수)
## systemctl
---
```sh
[root@localhost home]# systemctl start httpd // 툴 실행
[root@localhost home]# systemctl enable httpd // 툴 등록
# status, stop, restart, disable 등 추가 명령어 들
```
- [관련 링크](https://www.kernelpanic.kr/20)

## index.html
---
```html
<html>
        <body>
                welcome to jjh's Site!!!
        </body>
</html>
```

## httpd 홈 디렉토리
---
```
/etc/httpd
```
- 웹 서비스 관련 데이터 저장 디렉토리
- `httpd.conf`에서 웹 서비스 관련 설정을 수정할 수 있다.
	- <Directory/>접근 권한 정보</Directory>
	- LogLevel:

## 웹 서비스 기본 포트
---
port: 80
FQDN: 임의의 ip(192.169.1.101):80