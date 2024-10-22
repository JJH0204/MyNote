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
   - Tan 코드를 입력해 로그인을 시도할 때 Proxy를 통해 hidden name을 목표로 하는 Jane으로 바꿔서 요청하면 성공![[Pasted image 20241022103935.png]]
1) 
2) String SQL Injection
![[Pasted image 20241022093320.png]]
2) 