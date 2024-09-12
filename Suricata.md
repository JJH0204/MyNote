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

""" 결과
lo               UNKNOWN        127.0.0.1/8 ::1/128
enp0s3           UP             192.168.1.118/16 fe80::a00:27ff:fe41:6cb2/64
"""

vi /etc/suricata/suricata.yaml

"""
 18     HOME_NET: "[192.168.0.0/16]" # 사설 IP 대역들이 추가되어 있음

 61 default-log-dir: /var/log/suricata/ #로그 적제 디렉토리

 136       community-id: true

 621   - interface: enp0s3 # --brief로 확인한 인터페이스로 변경(패킷 탐지할 인터페이스)

 798       promisc: true

 814   - interface: enp0s3 # 패킷 캡쳐할 인터페이스 설정
"""
:wq 

# 설정 파일 문법 검사
suricata -T -c /etc/suricata/suricata.yaml -v

""" 결과
Notice: suricata: This is Suricata version 7.0.6 RELEASE running in SYSTEM mode
Info: cpu: CPUs/cores online: 2
Info: suricata: Running suricata under test mode
Info: suricata: Setting engine mode to IDS mode by default
Info: exception-policy: master exception-policy set to: auto
Info: logopenfile: fast output device (regular) initialized: fast.log
Info: logopenfile: eve-log output device (regular) initialized: eve.json
Info: logopenfile: stats output device (regular) initialized: stats.log
Info: detect: 1 rule files processed. 39802 rules successfully loaded, 0 rules failed, 0
Info: threshold-config: Threshold config parsed: 0 rule(s) found
Info: detect: 39805 signatures processed. 1158 are IP-only rules, 4116 are inspecting packet payload, 34321 inspect application layer, 108 are decoder event only
Notice: suricata: Configuration provided was successfully loaded. Exiting.
"""

# suricata 실행
suricata -c /etc/suricata/suricata.yaml -i enp0s3
```

- 서비스 추가
```
vi /etc/systemd/system/suricata.service

"""
  1 [Unit]
  2 Description=Suricata IDS/IPS
  3 After=network.target
  4
  5 [Service]
  6 ExecStart=/usr/bin/suricata -c /etc/suricata/suricata.yaml -i enp0s3
  7
  8 [Install]
  9 WantedBy=default.target
:wq 
"""
```
	- 새로운 서비스를 추가하고 싶다면 이 방법으로 추가

- 서비스 실행
```
systemctl enable suricata

systemctl daemon-reload
systemctl start suricata
```
	-  정상 실행 안된다면 위 설정 다시 보기

- 테스트
```
curl https://testmynids.org/uid/index.html
```
![[Pasted image 20240912104047.png]]
- 같은 내용이 출력되면 정상

![[Pasted image 20240912104241.png]]

- 침해 상황을 볼 수 있는 로그 파일
```
cat /var/log/suricata/fast.log
```

- json 툴 설치
```
apt install -y jq
```

- jp 사용법
```
jq 'select(.alert .signature_id==2100498)' /var/log/suricata/eve.json
jp '명령어(.요소 .요소==찾는 값)' json 파일 경로
```

- 룰 작성
```
cd /root/suricata-7.0.6/rules
vi ./local.rules

# [[Snort Rule]]과 방식이 같음
alert icmp any any -> $HOME_NET any (msg:"icmp packit";sid:100001;rev:1;)
```

- 룰 추가
```
vi /etc/suricata/suricata.yaml
2166   - /etc/suricata/rules/local.rules
```