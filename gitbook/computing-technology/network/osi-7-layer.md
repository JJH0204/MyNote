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

---

### 물리 계층 (Physical Layer)

- 데이터를 전기적 신호(이진수)로 변환하여 전송
- 네트워크 장비 간 물리적 연결(케이블, 전파, 광신호 등)
- 데이터 속도, 전송 방식(직렬/병렬), 전송 매체 결정

> 장비: 리피터, 허브, 광케이블, 동축 케이블
> 프로토콜: RS-232, IEEE 802.11(Wi-Fi)

---

### 데이터 링크 계층 (Data Link Layer)

- MAC 주소 기반 통신 & 오류 감지 (Frame 단위)
- 물리 계층에서 받은 데이터를 프레임(Frame)으로 변환
- 네트워크 장치 간 직접적인 데이터 전송 및 흐름 제어
- 오류 감지(Parity Check, CRC) 기능 제공

> 장비: 스위치, 브리지
> 프로토콜: Ethernet, Wi-Fi, MAC

---

### 네트워크 계층 (Network Layer)



---

### 전송 계층 (Transport Layer)

---

### 세션 계층 (Session Layer)

---

### 표현 계층 (Presentation Layer)

---

### 응용 계층 (Application Layer)

