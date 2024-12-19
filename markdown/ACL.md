- [관련자료](https://simpleisit.tistory.com/21)
# Access Control List
- 접근 제어 목록
- 라우터를 통하는 트래픽을 검사 후 분류해 지정된 처리를 수행

## 제어기준
---
- standard : 출발지 IP만 제어 기준에 적용
- extended : 출발지 IP를 포함해 목적지 IP 사용되는 프로토콜(port)등 좀 더
  상세한 설정을 적용

## 주의
---
- ACL 설정은 목적지와 가까운 라우터에 진행
	(라우터에서 실행하는 검사 횟수 = 트래픽 = 부하)

## ACL Standard Set
---
### 방법
`access-list <name or num> <option> <network> <wildcard>`

## ACL Extended Set (추천)
---
### 방법
`ip access-list <standard-extended> <1-99, name>`
`<option_1> <protocol> <source ip> <destination ip> <option_2> <service>`
	예시) permit tcp host 10.10.10.0 host 192.168.10.1 eq www
	해석) 10.10.10.0에서 출발해 192.168.10.1로 향하는 http 트래픽을 허용
※ 서브넷 설정은 와일드카드로 적용 됨(단일 네트워크의 경우 0.0.0.0)

## ACL 적용
---
- access-list 설정 후 적용할 인터페이스에 접속
- `ip access-group <1-99, name> <in, out>` 설정
	- in: 인터페이스를 통해 라우터로 들어오는 패킷에 대해 적용
	- out: 인터페이스를 통해 라우터 밖으로 나가는 패킷에 대해 적용

## ACL 정책 적용 기준
---
- Access-list 기준 위에서 아래로 순서대로 적용된다.
- ACL 적용 시 Access-list에 작성되지 않는 트래픽은 Deny 된다.
	- 그 외 패킷을 허용하기 위해 `permit ip any any` 설정을 추가해야 한다.

## 그 외 정보
---
- tcp 기반 서비스: http, https, ftp
- icmp 기반 서비스: ping
	- ping의 경우 차단 또는 허용이 필요할 때 `echo`/`echo-reply` 모두 허용

## 네트워크 보안에 사용되는 ACL
---
[[RACL]]
[[DACL]]