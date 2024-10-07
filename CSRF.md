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
