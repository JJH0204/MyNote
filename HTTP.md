# HTTP (Hyper Text Transfer Protocol)
---
- 서버 클라이언트의 데이터 교환을 요청(Request), 응답(Response) 형식으로 정의한 [프로토콜](Network_Protocol.md)
- 팀 버너스 리(Team Berners-Lee)와 그의 팀이 제정한 이후, 현대 웹 서비스의 바탕이 되는 [프로토콜](Network_Protocol.md)로 자리 잡았다.
- 기본 메커니즘은 클라이언트가 서버에 요청하면, 서버가 응답하는 것 뿐
- 웹 서버는 HTTP 섭를 HTTP [서비스 포트](Service_Port.md)에 대기 시킨다.
- 포트는 일반적으로 TCP/80 또는 TCP/8080로 정해진다.
- 클라이언트가 [서비스 포트](Service_Port.md)에 HTTP 요청을 전송 > 이를 해석해 적절한 응답을 반환한다.

# HTTP 메시지
---
- 클라이언트가 전송하는 HTTP 요청, 서버가 반환하는 HTTP 응답이 있다.
- 기능과 세부 구조의 차이를 제외하고 HTTP 헤더와 바디로 구성되는 공통점이 있다.
### HTTP 헤더 (Headers)
- 각 줄은 CRLF로 구분
- 첫 줄은 시작 줄(Start line), 나머지 줄은 헤더(Header)라 부른다.
- 영문 표기에 주의해야 한다. (Headers와 Header)
- 헤더의 끝은 빈 줄로 나타낸다.