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
