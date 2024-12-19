# \[정보 탐색]
## 1. nmap
`nmap 192.168.56.0/24`
![[Pasted image 20241002102358.png]]

## 2. 웹 접속
![[Pasted image 20241002102508.png]]
![[Pasted image 20241002102535.png]]
- 클릭 시 이미지를 보여주는 기능이 동작 중이다.
![[Pasted image 20241002102631.png]]

## dirb
- 추가로 접속 가능한 페이지가 있는지 탐색하기 위해 명령어 실행
- `dirb http://192.168.56.116/`
- http://192.168.56.116/robots
![[Pasted image 20241002103414.png]]
- http://192.168.56.116/wordpress/index.php
![[Pasted image 20241002105038.png]]
- http://192.168.56.116/wordpress/index/
(!) WARNING: NOT_FOUND[] not stable, unable to determine correct URLs {30X}.
    (Try using FineTunning: '-f')

- http://192.168.56.116/wordpress/readme
![[Pasted image 20241002105126.png]]

- http://192.168.56.116/wordpress/wp-admin/

- http://192.168.56.116/wordpress/wp-links-opml
```
This XML file does not appear to have any style information associated with it. The document tree is shown below.  

<opml version="1.0">

<head>

<title>Links for Quaoar</title>

<dateCreated>Wed, 02 Oct 2024 10:52:13 GMT</dateCreated>

<!-- generator="WordPress/3.9.14" -->

</head>

<body> </body>

</opml>
```

- http://192.168.56.116/upload/include/yui/README
- http://192.168.56.116/wordpress/wp-admin/      
+ http://192.168.56.116/upload/include/yui/event/event
+ http://192.168.56.116/upload/include/yui/event/README
+ http://192.168.56.116/upload/include/yui/yahoo/README                    
+ http://192.168.56.116/upload/include/yui/yahoo/yahoo                                   
## wpscan
![[Pasted image 20241002114900.png]]
- 메일 관련 플러그인 발견

## searchsploit
![[Pasted image 20241002115212.png]]
- 메일 관련 플러그인에 취약점 확인

![[Pasted image 20241002120809.png]]

로그인 정보를 갖기 위해 브루트 포스 공격 실행

프록시를 설정해 로그인 시 페이지와 주고 받는 데이터 확인
![[Pasted image 20241002125017.png]]

post 데이터를 활용해 브루트 포스 공격 시도
`hydra 192.168.56.116 http-form-post "/wordpress/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=%2Fwordpress%2Fwp-admin%2F&testcookie=1:Lost your password" -l admin -P ./weakpass.txt`
![[Pasted image 20241002125000.png]]
admin:admin 인 것을 확인
![[Pasted image 20241002125106.png]]

플러그인 관련 취약점을 활용한 소스코드 다운 받는다.
https://github.com/p0dalirius/CVE-2016-10956-mail-masta

실행 결과
![[Pasted image 20241002130512.png]]
![[Pasted image 20241002130708.png]]
![[Pasted image 20241002130730.png]]

wpadmin으로 ssh 접속을 시도했지만 취약한 비밀번호는 사용하지 않는 것 같다.

웹 셸을 이용해서 시스템에 접근하려 했지만 차단된 것 같다.

![[Pasted image 20241002143339.png]]

mail-masta를 활용한 익스플로잇 들을 조사하는 와중 좋은 깃 소스를 발견했다.
https://github.com/Hackhoven/wp-mail-masta-exploit

![[Pasted image 20241002144307.png]]
![[Pasted image 20241002144244.png]]
sql 인젝션을 통해 얻은 패스워드와 계정을 바로 사용한다.

![[Pasted image 20241002144412.png]]
![[Pasted image 20241002144436.png]]
![[Pasted image 20241002144505.png]]
