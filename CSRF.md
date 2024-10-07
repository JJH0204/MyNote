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

- 

피해자 입장
- dvwa, 이메일 로그아웃 - 웹 브라우저 닫기
- 메일 확인 dvwa 로그인 -> 공격자가 정한 비밀번호로 변경 됨
- 