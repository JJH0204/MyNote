- Spanning Tree Protocol (즉, 가지치기 기능)
- 연결된 스위치 간에 여러 포트가 연결된 경우 유효한 연결 한개만 남기고 나머지 연결을 비활성화 시키는 기능
![[Pasted image 20240821003413.png]]
- 즉, 단일 경로를 제공하는데 사용된다.
- VLAN 마다 설정 가능하다. (VLAN 마다 사용할 연결을 다르게 설정할 수 있다.)

# 포트 비활성화 규칙(Port Election)
---
1. Priority 값이 낮은 Switch 이 우선
	- 같을 경우 BID(Bridge ID)의 Address가 가장 낮은 Switch
	- root Switch의 모든 port는 Forword(전송) 상태가 된다.
![[Pasted image 20240821004450.png]]
> [!note]
> Priority 값은 VLAN 연결마다 따로 설정 가능하다.
> 설정 시 0을 포함해 4096의 배수로  설정해야 한다.


2. Non Root Switch에서 하나의 Root Port를 선택
	1) Root Switch로 향하는 Cost 가 가장 적은 포트
	2) Cost가 같은 경우 Port ID가 낮은 가장 낮은 port

3. 각 세그먼트에서 하나의 DP 선출
	- 그 외 port는 non DP가 된다.
		BLK 상태가 되어 데이터 송수신이 불가능 해진다.

# 자동 갱신 주기
---
![[Pasted image 20240821004844.png]]
스위치 간 신호 확인은 2초에 한번 (최대 20초) 대기 후 연결 여부를 결정한다.
연결이 동기화 되는데 총 55초(20 + 15 + 20) 가 소요된다.
스위치 종류에 따라 달라진다.