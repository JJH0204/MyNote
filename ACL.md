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
###
`access-list <name or num> <option> <network> <wildcard>`

