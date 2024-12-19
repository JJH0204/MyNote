- [관련자료](https://nirsa.tistory.com/32)

# Open Shortest Path First
- 라우터 라우팅 프로토콜
- 최적 경로를 계산할 때 SPF(Shortest Path First) 또는 다익스트라 알고리즘을 이용해 목적지 까지 최적의 경로를 계산


## 장점
---
- area 단위로 구성되어 대규모 네트워크를 안정적으로 운영할 수 있다.
- 표준 라우팅 프로토콜이다.
- 다른 라우팅 프로토콜에 비해 convergence time이 빠르다.
- Stub이라는 강력한 축약 기능을 지원한다.

## 특징
---
- 경계 대역을 광고할 때 Area Num을 사용한다.
- No Auto~ 가 필요 없다.

## 명령어
---
`router ospf [process-id]`
	: ospf 환경을 설정하기 위해 실행하는 명령어, id는 관리자가 관리
`net [ip] [wildcard] area [Area Num]`
	: 라우터와 연결된 네트워크의 구역을 설정 및 외부와 공유

### 주의사항
- Area Num가 0인 구역을 backbone area 라고 부르며 외부와 통신하기 위해서는 꼭 backbone area와 연결되어 있어야 가능하다. (backbone 설정 없이 area num을 1이상 설정하면 네트워크 통신이 불가능해 진다.)
- Virtual-link 기능으로 우회 할 수 있지만 물리적 환경이 어쩔 수 없을 때만 사용

## 관리 명령어
---
`sh ip ospf` : 원하는 ospf의 정보 확인
`sh ip ospf neighbor` : 이웃 정보 출력
`sh ip ospf database` : 라우팅 경로 정보 출력
`sh ip ospf int [인터페이스 이름]`
	: net type과 protocol에 의해 장치에 설정된 정보 출력
그 외에도 많음

## [[Redistribution]]
---