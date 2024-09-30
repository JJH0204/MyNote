# \[정보수집]
## 1. IP 검색
`nmap 192.168.56.0/24`
![[Pasted image 20240930150614.png]]
- 192.168.56.112: 서비스 중인 서버 IP
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
### login page
![[Pasted image 20240930162545.png]]
- Credentials guest:guest can be used to access the guest account.
  (guest / guest 를 통해 guest 계정으로 로그인 가능하다고 한다.)

### enter page
![[Pasted image 20240930162719.png]]
- Venus에 대한 설명이 적혀있다.
- 온도: 464C, 표면 압력: 93bar, 대기 조성: 이산화탄소 96.5%, 질소 3.5%
- 별다른 내용은 없다.
![[Pasted image 20240930163120.png]]
- 로그인 과정에서 오고가는 패킷 중 보내는 패킷에 대한 내용이다.
- 웹 페이지의 관리자 권한으로 로그인할 수 있는 방법으로 보내는 패킷을 변조하는 것이 가능할 것 같다.
# \[브루트 포스 공격]
## `hydra 192.168.56.112 -s 8080 http-form-post "/:username=^USER^&password=^PASS^:Invalid username." -L weakuser.txt -P weakpass.txt`
- 웹 페이지 관리자 권한으로 로그인할 수 있는 계정을 알아내기 위해 무차별 대입 공격을 진행
- `weakuser.txt` 파일 생성
- guest, venus, magellan 추가 저장
![[Pasted image 20240930163719.png]]
- 찾은 계정 이름과 패스워드로 로그인![[Pasted image 20240930164944.png]]
- 로그인 과정에서 주고 받은 패킷 정보![[Pasted image 20240930165013.png]]![[Pasted image 20240930170443.png]]![[Pasted image 20240930170514.png]]
- [쿠키](cookie.md) 값 형태가 이상하다.(의도적으로 쿠키를 암호화한 것 같다.)
- guest:guest > Z3Vlc3Q6dGhyZmc= > (base64)guest:thrfg![[{F48FBC79-B02B-4AA7-A18D-EEECD77409DC}.png]]
![[{BBCC6A66-29A2-49DD-9608-67BE9F51E43D}.png]]
- venus:123456 > ![[{AD2EA223-A75E-4C4F-BA82-B1B97BFB0481}.png]] 쿠키에 변화가 없다
- 
- venus; dmVudXM6aXJhaGY=; venus:irahf > magellan:irahf
- magellan; bWFnZWxsYW46aXJhaGZ2bmF0cmJ5YnRsMTk4OQ==; magellan:irahfvnatrbybtl1989 > ROT13 디코딩
- 

![[Pasted image 20240930181250.png]]
![[Pasted image 20240930181420.png]]

find / -perm -u=s -type f 2>/dev/null
![[Pasted image 20240930181625.png]]

취약점이 있는 프로그램을 찾는다.
![[{6FE372E8-75EC-4804-8411-40A42C4886E7}.png]]![[{D402A44B-7A8F-4ABA-A275-B9DE443A63BC}.png]]
- 뭐지... 다른 걸 찾아보자
![[{A301CA31-E0D9-4690-87D8-8B2346EBCB40}.png]]


해당 프로그램에서 사용할 수 있는 악성코드를 설치한다.


칼리 웹 서버를 통해 피해자 서버로 악성코드를 옮긴다.
make로 컴파일한다.

실행한다.


![[Pasted image 20240930190307.png]]