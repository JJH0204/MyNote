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
- dirb를 사용해서 접속하능한 웹 서버 디렉토리를 스캔한다.

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
