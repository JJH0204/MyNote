# OSI 7 Layer

## OSI 7 계층 모델(OSI 7 Layer Model)이란?

* 네트워크 통신을 계층화하여 표준화한 모델
* 국제 표준화 기구(ISO)에서 정의한 네트워크 프로토콜 구조
* 각 계층별 역할을 분리하여 네트워크 통신을 설명하는 개념이다.

✔ **네트워크 통신 과정을 7개의 계층으로 분할하여 정리**

✔ **각 계층이 독립적으로 동작하며, 계층 간 상호작용을 통해 데이터가 전달됨**

✔ **TCP/IP 모델과 비교할 때 기본 개념으로 많이 사용됨**

***

<figure><img src="../../.gitbook/assets/Pasted image 20240819202412.png" alt=""><figcaption><p>OSI 7 Layer 와 TCP/IP</p></figcaption></figure>

## OSI 7 계층 구조

### 요약

<table><thead><tr><th width="100">계층</th><th>명칭</th><th>역할</th><th>주요 프로토콜 및 장비</th></tr></thead><tbody><tr><td>7</td><td>응용 계층<br>Application Layer</td><td>사용자와 네트워크 간 상호작용</td><td>HTTP, FTP, SMTP, DNS</td></tr><tr><td>6</td><td>표현 계층<br>Presentation Layer</td><td>데이터 형식 변환, 암호화/복호화</td><td>JPEG, MP3, ASCII, TLS, SSL</td></tr><tr><td>5</td><td>세션 계층<br>Session Layer</td><td>통신 세션 관리, 연결 설정 및 종료</td><td>NetBIOS, RPC, PPTP</td></tr><tr><td>4</td><td>전송 계층<br>Transport Layer</td><td>신뢰성 있는 데이터 전송, 흐름/오류 제어</td><td>TCP, UDP</td></tr><tr><td>3</td><td>네트워크 계층<br>Network Layer</td><td>데이터 패킷 라우팅, IP 주소 관리</td><td>IP, ICMP, ARP<br>라우터</td></tr><tr><td>2</td><td>테이터 링크 계층<br>Data Link Layer</td><td>물리적 주소(MAC)관리, 오류 감지</td><td>이더넷, 스위치, MAC 주소</td></tr><tr><td>1</td><td>물리 계층<br>Physical Layer</td><td>전기적 신호, 데이터 전송 매체</td><td>케이블, 허브, 리피터</td></tr></tbody></table>

### 1 계층: 물리 계층
