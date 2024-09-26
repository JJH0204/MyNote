cybersploit ctf
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
```
dirb http://192.168.56.105/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Sep 25 22:11:18 2024
URL_BASE: http://192.168.56.105/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

                                                                             GENERATED WORDS: 4612

---- Scanning URL: http://192.168.56.105/ ----
                                                                             + http://192.168.56.105/cgi-bin/ (CODE:403|SIZE:290)                        
+ http://192.168.56.105/hacker (CODE:200|SIZE:3757743)                      
+ http://192.168.56.105/index (CODE:200|SIZE:2333)                          
+ http://192.168.56.105/index.html (CODE:200|SIZE:2333)                     
+ http://192.168.56.105/robots (CODE:200|SIZE:79)                           
+ http://192.168.56.105/robots.txt (CODE:200|SIZE:79)                       
+ http://192.168.56.105/server-status (CODE:403|SIZE:295)                   
                                                                               
-----------------
END_TIME: Wed Sep 25 22:11:20 2024
DOWNLOADED: 4612 - FOUND: 7
                                                   
```

## \[1-3] 웹 서비스 스캐닝
```
nikto -h 192.168.56.105 -C all
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.56.105
+ Target Hostname:    192.168.56.105
+ Target Port:        80
+ Start Time:         2024-09-25 22:13:17 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Ubuntu)
+ /: Server may leak inodes via ETags, header found with file /, inode: 153327, size: 2333, mtime: Sat Jun 27 00:46:41 2020. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /index: Uncommon header 'tcn' found, with contents: list.
+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.html. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
+ 26640 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2024-09-25 22:14:11 (GMT-4) (54 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
발견된 취약점: anti-clickjacking, X-Content-Type-Options
Apache/2.2.22의 취약점: 
`#wp-config.php#`: 워드프레스로 웹 서버 구축한 것으로 보인다.

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

## \[2]