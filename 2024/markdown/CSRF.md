# Cross-Site Request Forgery
- 요청 대행 공격

공격자는 권한이 없는 상태에서 권한이 있는 사용자에게 특정 명령어를 실행하도록 요청하여 공격자가 원하는 데로 서비스를 장악하는 공격

![[Pasted image 20241007110811.png]]
1234 / 1234로 관리자의 패스워드 변경

`http://192.168.56.118/vulnerabilities/csrf/?password_new=1234&password_conf=1234&Change=Change#`
- get 방식의 매소드인점 확인
- 

![[Pasted image 20241007111451.png]]
html 형식으로 메일 쓰기

![[Pasted image 20241007112007.png]]
- 피해자가 메일을 클릭하여 실행하는 것 만으로도 계정의 비밀번호가 공격자 마음대로 바뀐다.
![[Pasted image 20241007112144.png]]
```
<p><img src=URL></p>
```
- 피해자가 이메일을 열람하면서 자동으로 html 코드가 실행되어 피해 발생

- width, height 값을 0으로 설정하면 xbox도 사라짐

피해자 입장
- dvwa, 이메일 로그아웃 - 웹 브라우저 닫기
- 메일 확인 dvwa 로그인 -> 공격자가 정한 비밀번호로 변경 됨

low
![[Pasted image 20241007112856.png]]- 보안 코드 없이 사용자의 입력을 무조건 신뢰하고 값을 비교하여 처리한다.

midium
![[Pasted image 20241007113148.png]]
- 도메인 이름이 url에 포함되어 있는지 대소문자 구분 없이 검사하지만 의미는 없다.

hight
![[Pasted image 20241007113344.png]]
- 사용자 토큰 요구
- mysql_real_escape_string: 태그에 임의의 값이 들어가는 것을 사전에 검출
- csrf 공격이 거의 불가능해짐

