cisco에서 개발한 IGRP 기반의 개방형 라우팅 프로토콜
망 구성 방식이 변경된 뒤 일어나는 불안정한 라우팅을 최소화하는데 최적화 됨

- [관련정보](https://m.blog.naver.com/luexr/222441096481)

# 연결
---
![[Pasted image 20240821231728.png]]
위와 같이 초기 설정된 topology에 AS를 구분해서 라우팅 진행

각 라우터의 연결 정보는 `sh ip route`를 통해 확인한다.

다음은 라우터에서 광고할 네트워크를 설정하는 과정이다.
![[Pasted image 20240821232313.png]]
`conf t` > `router eigrp ASN`> `net 네트워크IP 와일드카드`
모든 네트워크를 모두 설정 완료 했다면 `no auto-summary`를 실행해 자동 축약을 해제한다.
연결된 다른 라우터에서도 동일하게 작업을 진행한다.

그러면 같은 AS 안에서는 ping 송수신이 원활할 것이다.
![[Pasted image 20240821233135.png]]
연결이 정상이라면 ip 