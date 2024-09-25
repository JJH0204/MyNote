# 1] 정보 수집 (Scaning)
> [!Note]
> Attacker
> - ip: 192.168.56.105/24
> 
> victim
> - 같은 동일한 네트워크 대역에 있다고 가정하고 진행
## 1-1] Victim 대상 찾기
---
> netdiscover, nmap 등 scaning tool을 활용해 피해자 PC의 IP를 찾는다.
- `nmap 192.168.56.0/24`![[{502F8A71-3DD0-4168-9BC5-DEA47F1F3170}.png]]
- `netdiscover -r 192.168.56.0/24`![[{DF454A6C-E996-4D79-91DC-61722923A87A}.png]]

> [!Note]
> Attacker
> - ip: 192.168.56.105/24
> 
> victim
> - ip: 192.168.56.104/24
> - ssh, http, https 서비스가 동작 중임을 확인했다.
> - ssh 접속을 먼저 시도하는 것은 흔적(Log)을 남길 수 있기 때문에 지양하고,
>   ip 를 활용해 web 접속을 시도한다.

## 1-2] Browser 접속
---
> victim server에서 서비스 중인 웹 서비스를 활용해 접속을 시도한다.
- browser 접속: `http://192.168.56.104/`![[{A4990424-8C50-484E-B93C-5ED7441EF255}.png]]
- browser 접속: `https://192.168.56.104/`![[{B05F8D55-B9BD-4510-99E4-FADA7F1FB17A}.png]]![[{9FDE5F88-F1C5-4AF5-95DE-47F74DE38D0A}.png]]
- 