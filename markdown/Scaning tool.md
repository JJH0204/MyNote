# [nmap](https://nmap.org/)
---
0-1023(잘 알려진 포트):
1024-49151: 예약된 포트
49152-65535: 사설 포트

## TCP Scan: `-sT` 
---
`-sS`: SYN 플래그
- kali > SYN(80) > earth -> kali < SYN + ACK(80) < earth()
  : TCP 응답에 따라 포트가 활성화 되어 있는지 확인한다.
  : 포트에 반응이 없다면 활성화 되지 않았다는 의미
`-sN`: Null 플래그
- 아무 플래그가 없이 패킷 전달
`-sF`: FIN 플래그
`-sX`: xMas Scan
- 다양한 종류의 플래그를 패킷 전달함 한번에 전달하는 방식
`-xM`: 둘 이상 플래그를 조합해서 패킷에 포함
`-sA`: ACK 플래그
`-sW`: windows scan(windows size)
- 웹 사이트의 정보를 담은 windows의 정보를 알아내는 플래그
`-sL`: idle
- 좀비 시스템에서 사용하는 플래그

## UDP Scan: `-sU`
---
`-F`: Fast
`-r`: 순차적

## Timing Option
---
스캐닝 대상으로 하여금 공격을 위한 스캐닝인지 알 수 없도록 딜레이 시간을 설정하는 방법
0 : 5분 마다
1 : 15초 마다
2 : 0.4초 마다
3 : 다중 대상에 다중 탐색(기본 옵션)
4 : 정해진 시간(5분 동안) 만큼
5 : 75초만 

## NSE(Nmap Script Engine)
---
- 인증, 기본(-sC, -A), 발견, 익스플로잇, DoSS, 침투(), 취약점 점검 등
- https://nmap.org/ 에서 새로운 엔진을 설치 받을 수 있다.
- `-vuln-` : 취약점 점검 스크립트

### 파일 경로
---
`/usr/share/nmap`: nmap 설정 파일 경로
![[Pasted image 20240926094254.png]]
- [[nmap-os-db]]: 운영체제 정보 스크립트
- [[scripts]]: 스크립트 엔진 파일 경로

## 방화벽/IDS 등 장비 우회 옵션
---
-f: 패킷을 세분화
--source-ports, -g "출발 ip": 출발 ip 변조
--data-length "데이터 사이즈": 패킷 길이 조작
--scan-delay "시간":
-D(가짜 ip 생성)

---
nmap 
0-1023(Well-Known Port)
1024-49151 : 등록된 포트
49152-65535 : 비등록된 포트(사설 포트)

TCP Scan : -sT
(-sS / -sN / -sF / -sX / -sM / -sA / -sW / -sl)
UDP Scan : -sU
(-F(Fast) / -r

Timing Option
0 : 매 5분, 1 : 매 15초, 2 : 매 0.4초, 3 : 다중 대상에 다중 탐색(기본옵션)
4 : 5분 동안만, 5 : 대상 스캔 간격이 75초만

NSE(Nmap Script Engine)
- 인증, 기본(-sC, -A), 발견, 익스플로잇, DoS, 침투, 취약점 점검 등

방화벽 / IDS 등의 장비 우회 옵션
-f(패킷 세분화)
--source-ports, -g(출발지 포트 속이기)
--data-length
--scan-delay 
-D(가짜 IP 생성)