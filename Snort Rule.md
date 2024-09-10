![[Pasted image 20240909174043.png]]

# action
---
- alert: 경고
- log:
- pass:
- active:
- reject: 패킷 차단 + log화 + 상대에 메시지 전달
- drop: 패킷 차단 + log화
- sdrop: 패킷 차단

# protocol
---
- 탐지할 패킷 종류
- tcp / icmp / udp / ip / any

# source A&P / Destination A&P
---
- `any`: 모든 Address 또는 모든 Port
- port num
	- `10-20`: 10번에서 20번 사이
	- `:10`: 10번 포트 이하
	- `10:`: 10번 포트 이상
	- `!10`: 10번 포트 제외 모든 포트
- 