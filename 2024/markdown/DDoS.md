# Distribute Denial of Service
- 분산 서비스 거부 공격
- hping3 / SlowHTTPTest / GoldenEye / LOIC 등 다양한 Attack Tool이 있다.
- 대다수 공격자는 대량의 zombi pc를 만들어 공격에 활용
- 이때 공격자 PC를 C&C라고 하고 공격에 사용되는 zombi pc 를 zombi system, zombi pc 들을 zombi net이라고 한다.

## Basics DoS Attack
---
```
hping3 --icmp [IP] [추가 옵션]
```
- --icmp: 공격 패킷 형태(ping 패킷 외 다른 패킷 설정 가능)
## SYN Flooding Attack
---
![[Pasted image 20240909115159.png]]
- TCP 핸드 셰이크 원리를 이용한 공격
- Layer4 공격에 포함
- [관련자료](https://m.blog.naver.com/techtrip/222561492285)

### hping3 tool 을 활용한 SYN Floodin
```sh
hping3 [Victim_IP] -S [추가 옵션]
```

예시: `hping3 192.168.1.111 -S -i u50 -c 1000`
### SYN Flooding 공격 패턴
#### 패턴1: 소스IP 변조를 통한 반사 공격
- 소스IP주소를 스푸핑 하여 핸드 셰이크 프로세스를 비정상적으로 만드는 방식
- Land Attack, Smurf Attack 등

#### 패턴2: SYN/ACK 패킷 차단 후 공격

#### 패턴3: 봇넷을 활용한 DDoS 형태의 공격

### 공격 방어
- [[IDS]] / IPS / UTM(IDS, IPS 통합) 시스템 활용

## DDoS 공격 현황
---
- [https://horizon.netscout.com/](https://horizon.netscout.com/)
![[Pasted image 20240909121834.png]]
