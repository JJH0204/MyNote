# \[자료 조사]
## IP 탐색
> `arp-scan -l`
![[Pasted image 20240930092029.png]]
![[Pasted image 20240930092144.png]]

> `fping -g 192.168.56.0/24 --ipv4 -s`
![[Pasted image 20240930092506.png]]
![[Pasted image 20240930092622.png]]

## 서비스 탐색
> `nmap 192.168.56.110 -sV -v -p- -sC`
![[Pasted image 20240930092835.png]]

> `dirb http://192.168.56.110:8080/`
![[Pasted image 20240930093942.png]]

> `nikto -h 192.168.56.110:8080 -C all`
![[Pasted image 20240930094208.png]]

gobuster
![[Pasted image 20240930094310.png]]![[Pasted image 20240930094521.png]]
- wordlist_files 를 활용
![[Pasted image 20240930094610.png]]![[Pasted image 20240930094659.png]]

# \[사이트 접속]
![[Pasted image 20240930094802.png]]

![[Pasted image 20240930100543.png]]
- 파이썬을 활용해 웹을 만들었구나

![[Pasted image 20240930100642.png]]

![[Pasted image 20240930100715.png]]
- 인젝션에 취약한 서버라고 한다.
![[Pasted image 20240930100925.png]]
- 잘못된 구문이라도 서버에서 반응하면 sql 인젝션에 취약할 가능성이 높다
- 수동 점검과 자동 점검이 있다.

## sql 자동 점검
![[Pasted image 20240930101249.png]]


# \[zap active scaning]
[[Zap]]
![[Pasted image 20240930100500.png]]
