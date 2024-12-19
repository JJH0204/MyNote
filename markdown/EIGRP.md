cisco에서 개발한 IGRP 기반의 개방형 라우팅 프로토콜
망 구성 방식이 변경된 뒤 일어나는 불안정한 라우팅을 최소화하는데 최적화 됨
hop count가 커 대학/병원 등에서 사용한다.
rip와 달리 경로 비용을 가중치로 관리해 유동적이다.

- [관련정보](https://m.blog.naver.com/luexr/222441096481)

# 연결
---
![[Pasted image 20240821231728.png]]
위와 같이 초기 설정된 topology에 AS를 구분해서 라우팅 진행

각 라우터의 연결 정보는 `sh ip route`를 통해 확인한다.

다음은 라우터에서 광고할 네트워크를 설정하는 과정이다.
![[Pasted image 20240821232313.png]]
`conf t` > `router eigrp ASN`> `net 네트워크IP 와일드카드`
- [[ASN]]
- [[와일드카드 마스크]]
모든 네트워크를 모두 설정 완료 했다면 `no auto-summary`를 실행해 자동 축약을 해제한다.
연결된 다른 라우터에서도 동일하게 작업을 진행한다.

그러면 같은 AS 안에서는 ping 송수신이 원활할 것이다.

![[Pasted image 20240821233135.png]]
연결이 정상이라면 라우팅 테이블에 D 코드로 이웃한 네트워크 정보가 저장된다.

`sh ip eigrp neighbors`를 통해 이웃 정보를 확인할 수 있다.
![[Pasted image 20240821233357.png]]
이곳에 이웃 정보가 없다면 네트워크 광고 데이터를 받지 못해 라우팅 테이블을 갱신할 수 없게 된다.

경로의 최적 경로를 계산하기 위해 `sh int 인터페이스이름`의 포트 정보에서 확인할 수 있는 MTU, BW, DLY 값을 활용한다.
![[Pasted image 20240821233636.png]]

네트워크 광고로 받은 모든 경로 데이터는 `sh ip eigrp topology`에서 확인할 수 있다.
FD 값이 가장 작은 경로가 최적 경로가 된다.

# 서로 다른 ASN 끼리 재분배
---
ASN 값이 서로 다른 경우 재분배 설정이 없으면 네트워크 정보를 받아올 수 없다.
서로 다른 라우터 끼리 연결 하는 기능을 Redistribution이라 한다.

두 가지로 방법이 나뉜다.
## Multi : 양 라우터에 재분배
## Single 한쪽 라우터에 재분배
---
재분배 할 라우터에 접속한다.

`router eigrp ASN` > `redistribute eigrt 연결할ASN`
![[Pasted image 20240822000407.png]]

`router eigrp 연결할ASN` > `redistribute eigrt ASN` > 네트워크 추가 > `no auto-summery`
```
Router(config)#router eigrp 100
Router(config-router)#redistribute eigrp 200

Router(config-router)#do sh ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
* - candidate default, U - per-user static route, o - ODR
P - periodic downloaded static route
Gateway of last resort is not set
192.168.20.0/24 is variably subnetted, 2 subnets, 2 masks
C 192.168.20.192/26 is directly connected, Serial0/3/1
L 192.168.20.194/32 is directly connected, Serial0/3/1
192.168.30.0/24 is variably subnetted, 5 subnets, 2 masks
C 192.168.30.0/26 is directly connected, Loopback0
L 192.168.30.1/32 is directly connected, Loopback0
D 192.168.30.64/26 [90/2297856] via 192.168.30.130, 00:05:13, Serial0/3/0
C 192.168.30.128/26 is directly connected, Serial0/3/0
L 192.168.30.129/32 is directly connected, Serial0/3/0

Router(config-router)#net 192.168.20.192 0.0.0.63
Router(config-router)#
%DUAL-5-NBRCHANGE: IP-EIGRP 100: Neighbor 192.168.20.193 (Serial0/3/1) is up: new adjacency

Router(config-router)#no auto-summary
```

재분배한 라우터에서는 D 코드로 다른 AS 네트워크의 경로 정보가 표시된다.
다른 라우터에서는 D EX로 외부에서 온 네트워크라는 점을 확인할 수 있도록 표시한다.

라우팅 프로토콜이 같으면 네트워크를 중복으로 광고해도 문제가 없다.
다르면 한쪽에서만 진행, 중복 광고 시 error

# [[Redistribution]]
---
