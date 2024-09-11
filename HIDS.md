# Host-Based IDS (OSSEC)
- 호스트에서 발생하는 침입 사례를 검증
- Snort와 같이 RULE을 활용해 패킷 검출

## 설치(Ubuntu)
---
### 라이브러리 설치
```bash
apt install -y build-essential make zlib1g-dev libpcre2-dev libevent-dev libssl-dev libz-dev libsqlite3-dev

wget -q -O - https://updates.atomicorp.com/installers/atomic | bash

apt update
```

### 서버 설치
```
apt install -y ossec-hids-server
```

### 환경설정 파일
```
vi /var/ossec/etc/ossec.conf

113   <remote>
114     <connection>secure</connection>
115     <allowed-ips>192.168.0.0/16</allowed-ips> #추가
116   </remote>

```

- rootkit? 관리자 권한 빼앗기 위해 사용하는 것

### 관리자 툴 실행
```
cd /var/ossec/bin
manage_agents
```
#### agent 추가
```
****************************************
* OSSEC HIDS v3.7.0 Agent manager.     *
* The following options are available: *
****************************************
   (A)dd an agent (A).
   (E)xtract key for an agent (E).
   (L)ist already added agents (L).
   (R)emove an agent (R).
   (Q)uit.
Choose your action: A,E,L,R or Q: a (추가 선택)

- Adding a new agent (use '\q' to return to the main menu).
  Please provide the following:
   * A name for the new agent: win
   * The IP Address of the new agent: 192.168.1.8
   * An ID for the new agent[001]: 001
Agent information:
   ID:001
   Name:win
   IP Address:192.168.1.8

Confirm adding it?(y/n): y
Agent added with ID 001.
```

#### 키 발급
```
****************************************
* OSSEC HIDS v3.7.0 Agent manager.     *
* The following options are available: *
****************************************
   (A)dd an agent (A).
   (E)xtract key for an agent (E).
   (L)ist already added agents (L).
   (R)emove an agent (R).
   (Q)uit.
Choose your action: A,E,L,R or Q: e (키 발급 선택)

Available agents:
   ID: 001, Name: win, IP: 192.168.1.8
Provide the ID of the agent to extract the key (or '\q' to quit): 001

Agent key information for '001' is:
MDAxIHdpbiAxOTIuMTY4LjEuOCBlMjAwOGQyNDZkMGY4YjJkNGYyOTU0OWYzNDZjMWZiOTFmYWZiMGQ3MDM5MWI4MDA3YjQzY2FmNWJjZjkxNjNi

** Press ENTER to return to the main menu.
```
- 키는 꼭 기억하고 있어야 한다
### 서버 구동
```
./ossec-control start
# ./ossec-control 만 입력하면 사용가능한 명령어 확인 가능
```


### 메시지
```
tree /var/ossec/logs # 로그 확인 가능
tail -f /var/ossec/logs/alerts/alerts.log # 실시간 확인
```

## 윈도우 설치
![[Pasted image 20240911094941.png]]![[Pasted image 20240911095102.png]]
![[Pasted image 20240911102412.png]]![[Pasted image 20240911102949.png]]![[Pasted image 20240911102541.png]]![[Pasted image 20240911102551.png]]![[Pasted image 20240911102636.png]]
![[Pasted image 20240911102704.png]]![[Pasted image 20240911102726.png]]