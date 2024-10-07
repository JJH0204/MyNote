![[Pasted image 20241007123017.png]]
![[Pasted image 20241007123142.png]]a = aad 
i = in

![[Pasted image 20241007124552.png]]
```
	function chk_form(){
		var id = document.web02.id.value ;
		var pw = document.web02.pw.value ;
		if ( id == pw )
		{
			alert("You can't join! Try again");
			document.web02.id.focus();
			document.web02.id.value = "";
			document.web02.pw.value = "";
		}
		else
		{
			document.web02.submit();
		}
	}
```
![[Pasted image 20241007124955.png]]
유저가 입력할 때는 아이디와 패스워드가 같으면 안되는데 결과를 계산할 때는 같아야 한다.
프록시 툴을 이용해 입력은 다르게 결과는 같게 바꾸면 해결된다.
![[Pasted image 20241007140902.png]]

![[Pasted image 20241007142533.png]]