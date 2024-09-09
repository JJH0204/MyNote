# Distribute Denial of Service
- 분산 서비스 거부 공격
- hping3 / SlowHTTPTest / GoldenEye / LOIC 등

## SYN Flooding Attack
---
![[Pasted image 20240909115159.png]]
- TCP 핸드 셰이크 원리를 이용한 공격
- Layer4 공격에 포함

### hping3 tool 을 활용한 SYN Floodin
```sh
hping3 [Victim_IP] -S [추가 옵션]
```

예시: `hping3 192.168.1.111 -S -i u50 -c 1000`
### SYN Flooding
패턴1: 소스IP 변조를 통한 반사 공격
- 소스IP주소를 스푸핑 하여 핸드 셰이크 프로세스를 비정상적으로 만드는 방식
- Land Attack, Smurf Attack