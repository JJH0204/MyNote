cybersploit ctf
# 정보 수집
`nmap 192.168.56.0/24`
```
Nmap scan report for 192.168.56.105
Host is up (0.00017s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 08:00:27:2A:8F:05 (Oracle VirtualBox virtual NIC)
```

`nmap 192.168.56.0/24 -sV -v -p-`
