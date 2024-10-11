# CAPTCHA Bypassing
---
![[Pasted image 20241011090635.png]]
![[Pasted image 20241011090822.png]]
![[Pasted image 20241011090948.png]]![[Pasted image 20241011091048.png]]
- 아이디 패스워드에 대한 페이로드가 필요하다
![[Pasted image 20241011091209.png]]
![[Pasted image 20241011091415.png]]![[Pasted image 20241011091422.png]]![[Pasted image 20241011091546.png]]![[Pasted image 20241011091622.png]]![[Pasted image 20241011091753.png]]총 30개 조합으로 대입 공격 시행
![[Pasted image 20241011091840.png]]![[Pasted image 20241011091959.png]]![[Pasted image 20241011091926.png]]꼭 활성화 확인

![[Pasted image 20241011092127.png]]![[Pasted image 20241011092208.png]]![[Pasted image 20241011092352.png]]![[Pasted image 20241011092526.png]]

- 캡챠는 프록시 설정으로 유지하고 아이디/패스워드 대입이 가능하다
- CAPTCHA BROKEN

# Forgotten Function
---
![[Pasted image 20241011092810.png]]
- 이메일을 입력하면 패스워드를 알려줄 것 같다.

![[Pasted image 20241011092834.png]]![[Pasted image 20241011092917.png]]![[Pasted image 20241011092948.png]]![[Pasted image 20241011093003.png]]
- 이메일을 안다면 시크릿 메시지를 알 수 있다. > 비밀번호를 알 수 있다.

![[Pasted image 20241011093243.png]]![[Pasted image 20241011093254.png]]

medium
![[Pasted image 20241011093539.png]]


# Insecure Login Forms
---
![[Pasted image 20241011093744.png]]![[Pasted image 20241011093753.png]]
![[Pasted image 20241011093929.png]]
![[Pasted image 20241011094002.png]]
![[Pasted image 20241011094207.png]]
![[Pasted image 20241011094411.png]]
![[Pasted image 20241011094423.png]]

medium
![[Pasted image 20241011094517.png]]
![[Pasted image 20241011095159.png]]
- 나중에 선언된 변수가 적용됨
```
var a = bWAPP.charAt(0); var d = bWAPP.charAt(3); var r = bWAPP.charAt(16);
var b = bWAPP.charAt(1); var e = bWAPP.charAt(4); var j = bWAPP.charAt(9);
var c = bWAPP.charAt(2); var f = bWAPP.charAt(5); var g = bWAPP.charAt(4);
var j = bWAPP.charAt(9); var h = bWAPP.charAt(6); var l = bWAPP.charAt(11);
var g = bWAPP.charAt(4); var i = bWAPP.charAt(7); var x = bWAPP.charAt(4);
var l = bWAPP.charAt(11); var p = bWAPP.charAt(23); var m = bWAPP.charAt(4);
var s = bWAPP.charAt(17); var k = bWAPP.charAt(10); var d = bWAPP.charAt(23);
var t = bWAPP.charAt(2); var n = bWAPP.charAt(12); var e = bWAPP.charAt(4);
var a = bWAPP.charAt(1); var o = bWAPP.charAt(13); var f = bWAPP.charAt(5);
var b = bWAPP.charAt(1); var q = bWAPP.charAt(15); var h = bWAPP.charAt(9);
var c = bWAPP.charAt(2); var h = bWAPP.charAt(2); var i = bWAPP.charAt(7);
var j = bWAPP.charAt(5); var i = bWAPP.charAt(7); var y = bWAPP.charAt(22);
var g = bWAPP.charAt(1); var p = bWAPP.charAt(4); var p = bWAPP.charAt(28);
var l = bWAPP.charAt(11); var k = bWAPP.charAt(14);
var q = bWAPP.charAt(12); var n = bWAPP.charAt(12);
var m = bWAPP.charAt(4); var o = bWAPP.charAt(19);
```
```
var secret = (d + "" + j + "" + k + "" + q + "" + x + "" + t + "" +o + "" + g + "" + h + "" + d + "" + p);
```


# Logout Management
---
![[Pasted image 20241011100920.png]]
![[Pasted image 20241011100846.png]]
- 웹 페이지에서는 아무 정보도 얻을 수 없다.
- 프록시를 설정해서 확인한다.
- 