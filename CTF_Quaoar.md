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