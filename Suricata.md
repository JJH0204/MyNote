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

- suricata 환경 설정
```
./configure --enable-efqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
```

- 컴파일 및 설치
```
make && make install-full
```

- 결과 창
![[Pasted image 20240912100640.png]]
- [suricata 설치 경로] -c [suricata 설정 파일 경로] -i [적용할 인터페이스]
- 탐지를 위한 룰 설치가 완료 되었다고 함
- 룰을 포함해 관리 시스템을 업데이트 하기위해 필요한 명령어를 설명해준다.

- 버전 확인
```
suricata -V
```

- 설정 파일 수정
```
systemctl stop suricata

# 인터페이스 설정 확인
ip --brief
ip --brief add

""" 출력 결과
lo               UNKNOWN        127.0.0.1/8 ::1/128
enp0s3           UP             192.168.1.118/16 fe80::a00:27ff:fe41:6cb2/64
"""

vi /etc/suricata/suricata.yaml

 18     HOME_NET: "[192.168.0.0/16]"
 
```