## DNS 구축 자료
---
- [리눅스 서버에 구축](https://velog.io/@sherlockid8/Linux-CentOS-7-DNS-%EB%84%A4%EC%9E%84%EC%84%9C%EB%B2%84-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0)
- [윈도우 서버에 구축](https://ast-216.tistory.com/14)


# Linux DNS
---
```sh
dnf install bind bind-* -y # bind tool 설치

vi /etc/named.conf # name server 설정 파일 열기
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
``` sh
systemctl restart named # (시스템 재시작)
systemctl enable named # (시스템 활성화)
systemctl status named # or netstat -nlp (시스템 상태확인)
```

### 방화벽 허용
```sh
firewall-cmd --permanent --add-port=53/tcp
firewall-cmd --permanent --add-port=53/udp
firewall-cmd --reload
firewall-cmd --list-all
```

### DNS 설정 추가
```sh
vi /etc/named.conf
...
# 설정 추가 (이때 큰 따옴표는 필수)
zone "도메인" IN { 
	type master;
	tile "도메인.zone";
	allow-update { none; };
};
:wq
...
named-checkconf named.conf
```

### 도메인 등록 파일
```sh
# (큰 따옴표는 생략)
cp /var/named/named.localhost /var/named/"도메인".zone
chown root.named /var/named/"도메인".zone
vi /var/named/"도메인".zone
...

$TTL 1D
@    IN    SOA    @    rname.invalid.    ( 2    1D    1H    1W    1H )
           IN     NS   @
           IN     A    "IP"

www        IN     A    "IP"
ftp        IN     A    "IP"
:wq 

...

cd /var/named/
named-checkzone wolf.com wolf.com.zone
```

이후 시스템 활성화 
(도메인 이름에 "_" 같은 특문 넣지 마라 에러 난다)

### DNS 작동확인
```sh
nslookup 
> server "DNS IP"
> www."찾을 도메인"
```
![[Pasted image 20240908154221.png]]

### 랜카드 설정 파일 위치
`/etc/NetworkManager/system-connections/`

### DNS 설정 파일
`/etc/resolv.conf` (수정 후 재부팅)

## Master & Slave
---
- 주, 보조 관계로서 서로 동기화를 통해 DNS 서버를 이중화 하는 기능
- 데이터가 동기화되는 것은 Master 서버에서 관리하는 zone database에서만 가능
- Master에 생성되어 있는 zone 파일이 업로드 되는대로 Slave에 전송됨
![[Pasted image 20240908173228.png]]
- Master: DNS 서버 변경의 주체로, 도메인 관련 정보에 대한 zone 파일을 관리
- Slave: Master 서버로부터 생성된 DNS 설정을 미러링하는 백업 서버 역할 수행
	  Master로부터 Zone 파일을 복제

- [관련자료](https://rlahjxx.tistory.com/15)
### 1) Master 구축
- 초기에는 기본 구축과 같음


### 2) Slave 구축
