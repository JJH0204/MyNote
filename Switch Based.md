스위치에 연결된 포트를 기반으로 VLAN을 구성하는 기술

# 과정1
---
- [[Subnetting]]을 통해 단말 장치에 우선적으로 독립된 IP를 할당한다.
- Switch에 접속: enable > conf t
- VLAN 을 생성: vlan 번호 > name vlan이름 > exit
- 포트 접속: int 포트이름
- 포트 access 모드로 변경: switchport mode access
- 해당 포트가 가리킬 VLAN 설정: switchport access vlan 번호
- 종료

위 과정을 VLAN 개수 만큼 수행한다.

# [[Native VLAN]]
---

# Router 설정
---
과정1을 마친 상태라면 같은 네트워크의 장치끼리 통신은 원활하지만 다른 네트워크와 통신을 불가능한 상태다.
이 문제를 Router 설정을 통해 해결할 수 있다.
아래 설정은 VLAN을 위한 Router의 Gateway 설정 방법이다.
- 라우터 접속: enable > conf t
- [인터페이스 활성화](obsidian://open?vault=MyNote&file=Gateway%20%EC%84%A4%EC%A0%95): no shutdown
- 스위치와 연결된 인터페이스의 vlan 접속: int 인터페이스.vlan번호
- [[trunk protocol]] 설정: encapsulation protocol이름 vlan번호[enca]