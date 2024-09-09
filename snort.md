- IDS: 침입 탐지 시스템 구축을 위해 사용되는 우분투 리눅스 기반 엔진
- [관련자료](https://velog.io/@2jinu/Snort-%EC%84%A4%EC%B9%98-0nl990xy)
## **Ubuntu snort install**
- Ubuntu 가 설치되어 있어야 함
- 원활한 작업을 위해 (`iputils-ping`, `vim`, `wget`, `unzip` 미리 설치)
  `apt-get install -y iputils-ping vim wget unzip`

### 의존성 파일 설치
---
```
apt install build-essential libpcap-dev libpcre3-dev libnet1-dev zlib1g-dev luajit hwloc libdumbnet-dev bison flex liblzma-dev openssl libssl-dev pkg-config libhwloc-dev cmake cpputest libsqlite3-dev uuid-dev libcmocka-dev libnetfilter-queue-dev libmnl-dev autotools-dev libluajit-5.1-dev libunwind-dev libfl-dev -y
```

### Source File install
---
- 깃(git)을 활용해 프로그램 설치
![[Pasted image 20240909142850.png]]
```
git clone https://github.com/snort3/libdaq.git
./bootstrap
./configure
make
make install
```

### gperftools install
---
```
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.13/gperftools-2.13.tar.gz
```
![[Pasted image 20240909143905.png]]
```
tar zxf ./gperftools-2.13.tar.gz
cd ./gperftools-2.13
./configure      # 환경 구성 명령어
~~~
make
make install
```

### snort install
---
```
cd
wget https://github.com/snort3/snort3/archive/refs/heads/master.zip
~~~
unzip master.zip
cd snort3-master/
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc
~~~
cd ./build
make # 컴파일 명령어
make install # 설치
```

### snort setting file
---
```
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
```

### snort rules install
---
```
wget -qO- https://www.snort.org/downloads/community/snort3-community-rules.tar.gz | tar xz -C /usr/local/etc/snort/rules/
```

```
vi /usr/local/etc/snort/snort.lua


24 HOME_NET = '192.168.0.0/16'
...
28 EXTERNAL_NET = '!$HOME_NET'

207     variables = default_variables,
208     rules = [[
209       include /usr/local/etc/snort/rules/snort3-community-rules/snort3-community.rules
210     ]]
```

```
cd /usr/local/etc/snort/rules/snort3-community-rules/
more snort3-community.rules #  커뮤니티 룰 확인 가능

cd ..
vi local.rules
```

```
alert icmp any any -> $HOME_NET any (msg:"icmp msg";sid:1000001;rev:1;)
:wq
# sid = 정책 식별 번호 (고유)
# rev = 정책 번호
```
![[Pasted image 20240909174043.png]]
```
vi /usr/local/etc/snort/snort.lua

208     rules = [[
209       include /usr/local/etc/snort/rules/local.rules
210       include /usr/local/etc/snort/rules/snort3-community-rules/snort3-community.rules
211     ]]
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

