## FI(file inclusion)
"파일 실행 공격"
- [[LFI]](Local FI)
- [[RFI]](Remote FI)
![[Pasted image 20241007120517.png]]
- 값의 확인 없이 바로 실행

![[Pasted image 20241007120655.png]]
- /에 대한 공백 처리가 없어 lfi 공격이 가능하다
- http:// https:// 덕분에 rfi 공격이 불가능해졌다.
- html / 브라우저의 취약점으로 공략 가능
	- Http, httP, HTTP 모두 http로 인식


![[Pasted image 20241007121602.png]]
- file에 저장된 값이 리스틍 포함되어 있는지 검사
- file로 시작하고 include.php가 아닌 
- ![[Pasted image 20241007122116.png]]
- file로 시작하는 프로토콜은 해결 못함

![[Pasted image 20241007122344.png]]
- 실행되는 파일만 지정했다.
![[Pasted image 20241007122548.png]]
