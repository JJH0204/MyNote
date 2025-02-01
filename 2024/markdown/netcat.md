- 현대의 네트워크 통신은 네트워크 소켓을 통해 이뤄진다.
	- 소켓은 통신을 위한 가장 작은 단위의 프로토콜이다.
- 서버에서 특정 포트를 통해 서비스를 동작시키는 환경을 구성한다.
	- 이때 클라이언트가 이 프로그램과 통신하기 위해서 사용하는 것이 **nc(netcat)** 이다.

# nc 설치
	`sudo apt update && sudo apt install netcat`

# nc 사용법
```bash
$ nc
usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
      [-m minttl] [-O length] [-P proxy_username] [-p source_port]
      [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit]
      [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]]
      [destination] [port]
$
```

- `nc hostname(ip) port`형식으로 간단하게 사용 가능하다.

# 사용 예시
- 웹 서비스에 접속해서 푸는 형태의 워게임은 브라우저를 사용해서 접속할 수 있지만, ELF 바이너리가 서비스로 등록되어 제공되는 워게임의 경우 nc로 접속해서 해결해야 한다.
![[Pasted image 20240806122040.png]]
