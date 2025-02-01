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
![[Pasted image 20241011101120.png]]
- 별다른 내용이 없다.
![[Pasted image 20241011101238.png]]![[Pasted image 20241011101249.png]]
- 로그인을 하고 다시 뒤로가기를 하니 다시 로그인이 되었다.
- 세션 관리가 재대로 이뤄지지 않는 것 같다.
![[Pasted image 20241011101415.png]]
```
Referer: http://192.168.56.122/bWAPP/ba_logout.php
...
PHPSESSID=0c8f5635616d89c3400772ee194fbf44
```
![[Pasted image 20241011101820.png]]
위 페이지를 이동할 떄 세션 처리가 정상적으로 이뤄지지 않아 잘못된 인증을 허용하여 로그아웃 후 뒤로가기를 통해 다시 로그인이 되는 상황이다.

medium 이상에서는 함수로 세션을 처리하는 것 같다.


# Password Attacks
---
1) 브루트 포스 패스워드 공격으로 확인 가능
2) 또 다른 방법
![[Pasted image 20241011102206.png]]
![[Pasted image 20241011102309.png]]
![[Pasted image 20241011102325.png]]
![[Pasted image 20241011102449.png]]
- 비밀번호를 어렵게 만들어야 하는 이유
- 조합이 다양해 질 수록 경우의 수가 기하급수적으로 상승한다.
- 테스트를 위해 값을 수정
![[Pasted image 20241011102626.png]]
![[Pasted image 20241011102659.png]]
![[Pasted image 20241011102750.png]]![[Pasted image 20241011102845.png]]
- Successfull login! 과 같은 결과가 나올때까지 진행
![[Pasted image 20241011103042.png]]
![[Pasted image 20241011104608.png]]
- Successfull login!에 1이 표시되어야 하는데 철자를 잘못 입력해서 뜨지 않았다.
- 하지만 찾긴했다.
![[Pasted image 20241011104750.png]]
값을 넣고 포워드 하면 로그인에 성공한다.

# Weak Passwords
---
![[Pasted image 20241011105014.png]]

# Administrative Portals
---
![[Pasted image 20241011111640.png]]![[Pasted image 20241011111648.png]]
```
http://192.168.56.122/bWAPP/smgmt_admin_portal.php?admin=1
```
![[Pasted image 20241011111715.png]]

medium
![[Pasted image 20241011111733.png]]
![[Pasted image 20241011111829.png]]
![[Pasted image 20241011111852.png]]

# Cookies (session 하이제킹)
---
[[cookie]]
![[Pasted image 20241011112303.png]]
![[Pasted image 20241011112248.png]]
![[Pasted image 20241011112338.png]]
![[Pasted image 20241011112533.png]]

(좌)일반 계정 (우)관리자 계정 접속
![[Pasted image 20241011112844.png]]![[Pasted image 20241011112913.png]]
![[Pasted image 20241011113008.png]]
관리자 세션의 쿠키로 변경

- 일반 계정이 없어서 발생한 에러
![[Pasted image 20241011113026.png]]
- 일반 계정이 있다면 관리자로 로그인이 가능할 것이다.

## https
http와 같다

# Session ID in URL
---

# Strong Sessions
---
![[Pasted image 20241011113842.png]]
