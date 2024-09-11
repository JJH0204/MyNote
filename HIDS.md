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

<email_notification>no</email_notification> : 문제 발생 시 에러를 전달할 이메일

<rules> ... </rules> : 적용 중인 룰 들

```

- rootkit? 관리자 권한 탈취를 위해 사용하는 것