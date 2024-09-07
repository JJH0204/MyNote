## DNS 구축 자료
---
- [리눅스 서버에 구축](https://velog.io/@sherlockid8/Linux-CentOS-7-DNS-%EB%84%A4%EC%9E%84%EC%84%9C%EB%B2%84-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0)
- [윈도우 서버에 구축](https://ast-216.tistory.com/14)


# Linux DNS
---
```
dnf install bind bind-* -y // bind tool 설치

vi /etc/named.conf // name server 설정 파일 열기
```

### named.conf 수정
```sh
11: listen-on port 53 { any; };
12: listen-on-v6 port 53 {none; }; 
19: allow-query { any; };
33: dnssec-validation no;
:wq 
```

127.0.0.1 : localhost (자신)
\* : any (모든 네트워크)

### 시스템 상태 활성화
```
systemctl restart named (시스템 재시작)
systemctl enable named (시스템 활성화)
systemctl enable named or netstat -nlp (시스템 상태확인)
```

### 방화벽 허용
```
firewall-cmd --permanent --add-port=53/tcp
firewall-cmd --permanent --add-port=53/udp
firewall-cmd --reload
firewall-cmd --list-all
```

### DNS 작동확인
```
nslookup 
> server "장치IP"
> www.letskorail.com
> www.kobus.co.kr
```
