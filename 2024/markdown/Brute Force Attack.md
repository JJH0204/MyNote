[[브루트 포스]]기법을 이용해 무차별 대입 공격을 하는 것을 의미

![[Pasted image 20240930123858.png]]
소문자 옵션 : 알고 있을때
대문자 옵션 : 모를때

![[Pasted image 20240930124209.png]]
![[Pasted image 20241007093855.png]]
- zone the riper 로 문구가 등장하지 않을 때까지 무차별 대입 공격을 할 수 있다.
- ![[Pasted image 20241007094041.png]]
- 위 파라미터를 활용해 진행할 수 있다.
- 파라미커가 표시되면 대부분 http 메소드 중 get을 사용한다.
- ![[Pasted image 20241007094516.png]]
![[Pasted image 20241007094221.png]]
- 세션의 쿠키 값을 확인할 수 있다.
- 히드라 툴을 사용해 공격 준비
![[Pasted image 20241007094847.png]]
![[Pasted image 20241007095355.png]]hydra 192.168.56.118 http-form-get "/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:Username and/or password incorrect.:H=Cookie:security=low;PHPSESSID:aqsgn666ja2jubcdvc40euees2"
![[Pasted image 20241007100635.png]]
- 취약한 아이디 리스트 / 패스워드 리스트 파일을 작성하고 명령어에 사용하도록 입력

![[Pasted image 20241007100956.png]]
- 서버의 취약점 원인
- 보안과 관련된 코드 없이 사용자의 입력을 무조건 비교 확인하기 때문에 취약점이 발생한다.

