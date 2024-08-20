스위치에 연결된 포트를 기반으로 VLAN을 구성하는 기술

# 과정
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
