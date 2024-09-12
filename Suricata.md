- IDS / IPS / NSM(Network Security Monitoring)
- https://oisf.net/, https://suricata.io/download/

## Install of Ubuntu Linux
### 환경 구성
---
- 환경 구성 패키지 설치
```
apt -y install libpcre2-dev libpcre3 libpcre3-dbg libpcre3-dev build-essential autoconf automake libtool libpcap-dev libyaml-0-2 libyaml-dev libcap-ng-dev libcap-ng0 make libmagic-dev libjansson-dev libjansson4 pkg-config libnspr4-dev libnss3-dev liblz4-dev rustc cargo python3-pip
```

- net filter : 네트워크 패킷 필터링을 위해 필요한 패키지
```
apt install -y libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev libnfnetlink0
```

- suricata 리소스 다운로드
```
wget https://www.openinfosecfoundation.org/download/suricata-7.0.6.tar.gz
```

- 압축 해제
```
tar xzf suricata-7.0.6.tar.gz
```

- 파일