# Host-Based IDS (OSSEC)
- 호스트에서 발생하는 침입 사례를 검증
- Snort와 같이 RULE을 활용해 패킷 검출

## 설치
---
### 라이브러리 설치
```bash
apt install -y build-essential make zlib1g-dev libpcre2-dev libevent-dev libssl-dev libz-dev libsqlite3-dev

wget -q -O - https://updates.atomicorp.com/installers/atomic | bash
```

