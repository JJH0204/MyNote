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

# \[zap active scaning]
[[Zap]]
