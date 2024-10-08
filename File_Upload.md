![[Pasted image 20241008092416.png]]
![[Pasted image 20241008092327.png]]![[Pasted image 20241008092443.png]]
![[Pasted image 20241008092351.png]]
![[Pasted image 20241008092337.png]]
![[Pasted image 20241008092504.png]]
- 업로드 되는 파일에 대한 검증이 없기에 파일 업로드에 취약점이 발생한다.


medium
![[Pasted image 20241008092654.png]]
- JPEG PNG 파일만 올릴 수 있다고 한다.
- [[MIME]] 라고 하는데 브라우저가 확장자를 인식할 수 있도록 개발자가 관리하는 내용에 의해 파일을 인식한다.
- MIME를 속인다면 원하는 파일을 업로드 할 수 있을 것 같다.
![[Pasted image 20241008093247.png]]![[Pasted image 20241008093312.png]]
- 확장자가 바뀌어도 코드는 유지된다.

![[Pasted image 20241008093424.png]]
- 업로드 되었다.
![[Pasted image 20241008093501.png]]
- 이렇게 명령어를 넣으면 실행할 수 있을까?
![[Pasted image 20241008093528.png]]
- 실행은 안된다.

- 프록시를 사용하면 실행할 수 있을 것 같다.

![[Pasted image 20241008094116.png]]
- 파일을 업로드할 때 intercept 된 내용이다.
- 파일 이름을 .php로 바꾼다.![[Pasted image 20241008094139.png]]
- 이후 패킷을 전달하면 파일이름이 바뀌어 업로드 된다.![[Pasted image 20241008094509.png]]
![[Pasted image 20241008094602.png]]
- 업