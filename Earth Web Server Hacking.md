# 1] 정보 수집 (Scaning)
> [!Note]
> Attacker
> - ip: 192.168.56.105/24
> - victi
## 1-1] Victim 대상 찾기
> netdiscover, nmap 등 scaning tool을 활용해 피해자 PC의 IP를 찾는다.
- `nmap 192.168.56.0/24`![[{502F8A71-3DD0-4168-9BC5-DEA47F1F3170}.png]]
- `netdiscover -r 192.168.56.0/24`
- 