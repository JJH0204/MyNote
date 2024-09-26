# [[nmap]]
---
0-1023(잘 알려진 포트):
1024-49151: 예약된 포트
49152-65535: 사설 포트

## TCP Scan
---
`-sT` 
### `-sS`: SYN 플래그
- kali > SYN(80) > earth -> kali < SYN + ACK(80) < earth()
  : TCP 응답에 따라 포트가 활성화 되어 있는지 확인한다.
  : 포트가 
`-sN`
`-sF`: FIN 플래그
`-sX`
`-xM`
`-sA`: ACK 플래그
`-sW`
`-sL`