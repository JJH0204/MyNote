- IDS: 침입 탐지 시스템 구축을 위해 사용되는 우분투 리눅스 기반 엔진
- 
## **Ubuntu snort install**
- Ubuntu 가 설치되어 있어야 함
- 원활한 작업을 위해 (iputils-ping, vim, wget 미리 설치)
### 의존성 파일 설치
---
```
apt install build-essential libpcap-dev libpcre3-dev libnet1-dev zlib1g-dev luajit hwloc libdumbnet-dev bison flex liblzma-dev openssl libssl-dev pkg-config libhwloc-dev cmake cpputest libsqlite3-dev uuid-dev libcmocka-dev libnetfilter-queue-dev libmnl-dev autotools-dev libluajit-5.1-dev libunwind-dev libfl-dev -y
```

### Source File 설치
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

### snort 설치
---
```
cd
wget https://github.com/snort3/snort3/archive/refs/heads/master.zip
~~~
apt install unzip
unzip master.zip
cd snort3-master/
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc
# --prefix (설치 경로 옵션)
~~~
cd ./build
make # 컴파일 명령어
make install # 설치
```