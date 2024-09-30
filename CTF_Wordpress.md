[[slitaz linux set]]

# \[탐색]
![[Pasted image 20240930112524.png]]
![[Pasted image 20240930112731.png]]
- CVE-2003-1418 디렉토리에 적용가능한 취약점을 알려줌

도메인 이름을 설정하고 탐색 가능
![[Pasted image 20240930113646.png]]

탐색할 디렉토리에 대한 정보를 알려주는 것 또한 가능
![[Pasted image 20240930114046.png]]

`readme.html`에서 버전을 확인
![[Pasted image 20240930113945.png]]

# \[웹 접속]
![[Pasted image 20240930113020.png]]
![[Pasted image 20240930114904.png]] 힌트

워드프래스 스캔
![[Pasted image 20240930120427.png]]
![[Pasted image 20240930120847.png]]
![[Pasted image 20240930120753.png]]
- admin에 대한 로그인 정보가 있다는 것을 알 수 있다.

# \[Password Attack]
프록시를 설정하고 로그인 페이지와 내가 주고 받는 정보를 볼 수 있다.
![[Pasted image 20240930121424.png]]
parameter='value'& 구조로 되어 있다.
![[Pasted image 20240930121958.png]]
- action 파라미터에 성공에 대한 정보가 들어가면 로그인이 될 것이다.

[[브루트 포스 공격]]

![[Pasted image 20240930122530.png]]
포스트 방식으로 서버에 요청한 점을 활용
