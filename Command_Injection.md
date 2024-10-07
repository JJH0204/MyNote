
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
- 어떤 명령어든 검사 없이 변수에 저장 후 cmd로 실행

![[Pasted image 20241007103810.png]]
보안 레벨을 올린다.

![[Pasted image 20241007103830.png]]![[Pasted image 20241007103903.png]]

![[Pasted image 20241007103936.png]]
&& 과 ; 를 공백으로 만드는 것 만으로는 완전히 방어는 어렵다

![[Pasted image 20241007104038.png]]
![[Pasted image 20241007104108.png]]![[Pasted image 20241007104138.png]]
- 모든 연결 키워드가 공백으로 변경 시킨다.
![[Pasted image 20241007104358.png]]
- 하지만 파이프라인(|)을 방어할 때 실수를 하는 바람에 명령어 실행이 가능했다.

![[Pasted image 20241007104730.png]]
![[Pasted image 20241007104640.png]]
- token을 사용하는 것이 주 특징
- 1회성 인증에 사용되는 token을 이용해 세션의 일치 확인
- 입력 받은 값을 .을 기준으로 4개의 옥텟으로 나누고 각 옥텟이 숫자인지 검사하는 등 디테일한 검사를 하기에 command injection을 방어할 수 있게 된다.
- 다른 공격 기법과 융합해 공격하면 뚫릴 수도 있다.
