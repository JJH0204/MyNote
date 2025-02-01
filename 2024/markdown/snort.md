- IDS: 침입 탐지 시스템 구축을 위해 사용되는 우분투 리눅스 기반 엔진
- [관련자료](https://velog.io/@2jinu/Snort-%EC%84%A4%EC%B9%98-0nl990xy)
## **Ubuntu snort install**
- 원활한 작업을 위해 
  (`iputils-ping`, `vim`, `wget`, `unzip`, `git` 미리 설치)
  `apt-get install -y iputils-ping vim wget unzip git`

### 의존성 파일 설치
---
```
apt install build-essential libpcap-dev libpcre3-dev libnet1-dev zlib1g-dev luajit hwloc libdumbnet-dev bison flex liblzma-dev openssl libssl-dev pkg-config libhwloc-dev cmake cpputest libsqlite3-dev uuid-dev libcmocka-dev libnetfilter-queue-dev libmnl-dev autotools-dev libluajit-5.1-dev libunwind-dev libfl-dev -y
```
```
sudo apt update
sudo apt install -y \
  build-essential \
  libpcap-dev \
  libpcre3-dev \
  zlib1g-dev \
  libdumbnet-dev \
  bison \
  flex \
  liblzma-dev \
  openssl \
  libssl-dev \
  pkg-config \
  libhwloc-dev \
  cmake \
  libsqlite3-dev \
  uuid-dev \
  libnetfilter-queue-dev \
  libmnl-dev \
  libluajit-5.1-dev \
  libdaq-dev \
  autoconf \
  libtool
```
### Source File install
---
- 깃(git)을 활용해 프로그램 설치
![[Pasted image 20240909142850.png]]
```
git clone https://github.com/snort3/libdaq.git # git에서 소스 파일 다운로드
cd ./libdaq

./bootstrap && ./configure                     # 초기 설정 스크립트 실행
make && make install                           # 소스 컴파일, 컴파일 된 소스 실행
```

### gperftools install
---
```
# gperftools 소스 설치
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.13/gperftools-2.13.tar.gz
```
![[Pasted image 20240909143905.png]]
```
tar zxf ./gperftools-2.13.tar.gz # gperftools 소스 압축 해제
cd ./gperftools-2.13
./configure                      # 환경 구성 스크립트 실행
make                             # 소스 컴파일
make install                     # 컴파일된 프로그램 실행
```

### snort install
---
```
cd                                # root의 home 디렉토리로 이동
wget https://github.com/snort3/snort3/archive/refs/heads/master.zip # snort 소스 다운
unzip master.zip                  # 소스 압축 해제
cd snort3-master/
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc
cd ./build
make # 컴파일 명령어
make install # 설치

snort -V      # 버전 확인
snort -c /usr/local/etc/snort/snort.lua   # 오류 검출
```
- 한 줄 코드
```
cd && wget https://github.com/snort3/snort3/archive/refs/heads/master.zip && unzip master.zip && cd ./snort3-master/ && ./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc && cd ./build && make && make install
```
### snort setting file
---
```
vi /etc/systemd/system/snort3-nic.service

[Unit]
Description=Set Snort 3 NIC in promiscuous mode and Disable GRO, LRO on boot
After=network.target
 
[Service]
Type=oneshot
ExecStart=/usr/sbin/ip link set dev enp0s3 promisc on
ExecStart=/usr/sbin/ethtool -K enp0s3 gro off lro off
TimeoutStartSec=0
RemainAfterExit=yes
 
[Install]
WantedBy=default.target

:wq

systemctl daemon-reload
systemctl start snort3-nic
systemctl enable snort3-nic
```

### 패킷 탐지 활성화
---
```
ip link set dev enp0s3 promisc on
```

### 네트워크 수신 설정
---
```
ethtool -k enp0s3 | grep receive -offload   # 외부 패킷 수신 정보 확인
ethtool -K enp0s3 gro off lro off           # 외부 패킷 수신 x
```

### snort community rules install
---
```
mkdir /usr/local/etc/snort/rules    # 룰 설치 경로 생성
wget -qO- https://www.snort.org/downloads/community/snort3-community-rules.tar.gz | tar xz -C /usr/local/etc/snort/rules/ # 커뮤니티 룰 설치
```

```
vi /usr/local/etc/snort/snort.lua


24 HOME_NET = '192.168.0.0/16'
...
28 EXTERNAL_NET = '!$HOME_NET'

192     variables = default_variables,
193     rules = [[
194       include /usr/local/etc/snort/rules/snort3-community-rules/snort3-community.rules
195     ]]

:wq 

cd /usr/local/etc/snort/rules/snort3-community-rules/
more snort3-community.rules #  커뮤니티 룰 확인 가능
```

### snort custom rules make
---
```
cd ..
vi local.rules

alert icmp any any -> $HOME_NET any (msg:"icmp msg";sid:1000001;rev:1;)
:wq

# sid = 정책 식별 번호 (고유)
# rev = 정책 번호
```
![[Pasted image 20240909174043.png]]
```
vi /usr/local/etc/snort/snort.lua

192     rules = [[
193       include /usr/local/etc/snort/rules/local.rules
194       include /usr/local/etc/snort/rules/snort3-community-rules/snort3-community.rules
195     ]]
```

```
wget https://www.snort.org/downloads/openappid/33380 -O OpenAppId-33380.tgz
tar -xzvf OpenAppId-33380.tgz
cp -R odp /usr/local/lib/
vi /usr/local/etc/snort/snort.lua
```

```
105 appid =
106 {
107     -- appid requires this to use appids in rules
108     app_detector_dir = '/usr/local/lib',
109     log_stats = true,
110
111 }
112
113 appid_listener =
114 {
115     json_logging = true,
116     file = "/var/log/snort/appid-output.log",
117 }
```

시스템 확인
```
snort -c /usr/local/etc/snort/snort.lua
snort -c /usr/local/etc/snort/snort.lua -R /usr/local/etc/snort/rules/local.rules
```

탐지 실행 명령어
```
snort -c /usr/local/etc/snort/snort.lua -R /usr/local/etc/snort/rules/local.rules -i enp0s3 -A alert_fast -s 65535 -k none
```


# [[Snort Rule]]
