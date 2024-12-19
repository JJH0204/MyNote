# Reflected (GET)
---
- 반사형
![[Pasted image 20241011114128.png]]![[Pasted image 20241011114136.png]]
medium
![[Pasted image 20241011114225.png]]
high
![[Pasted image 20241011114256.png]]

# Reflected (POST)
---

# Reflected (JSON)
---
![[Pasted image 20241011114358.png]]![[Pasted image 20241011114443.png]]![[Pasted image 20241011114503.png]]
반응은 하지만 값을 출력하지는 않다.
![[Pasted image 20241011114556.png]]
이전의 스크립트는 종료하고 새로운 스트립트를 추가
```
</script><script>alert(document.cookie)</script>
```
![[Pasted image 20241011114657.png]]
적용된다.

medium
![[Pasted image 20241011114835.png]]
```
<img src=x onerror=alret('hello')>
```
![[Pasted image 20241011114923.png]]

# Reflected (Back Button)
---
![[Pasted image 20241011115023.png]]
![[Pasted image 20241011120214.png]]
```
Referer: http://192.168.56.122/bWAPP/xss_back_button.php
```
- 뒤로가기로 넘어가는 사이트
![[Pasted image 20241011120402.png]]

# Reflected (Custom Header)
---
![[Pasted image 20241011121950.png]]
![[Pasted image 20241011121909.png]]
![[Pasted image 20241011122210.png]]

# Reflected (Eval)
---
![[Pasted image 20241011122416.png]]
![[Pasted image 20241011122507.png]]
![[Pasted image 20241011122533.png]]![[Pasted image 20241011122540.png]]

# Reflected (HREF)
---
![[Pasted image 20241011122842.png]]
![[Pasted image 20241011122900.png]]
![[Pasted image 20241011122935.png]]
![[Pasted image 20241011122948.png]]
- 원하는 동작은 아니지만 비정상적으로 움직임다.
![[Pasted image 20241011123055.png]]
```
</a><script>alert(document.cookie)</script><a>
```
로 입력을 수정하면 원하는 결과가 나올 것 같다.
![[Pasted image 20241011123243.png]]
정답


# Reflected (Login Form)
---

# phpMyAdmin BBCode Tag XSS
---


# Reflected ([[PHP_SELF]])
---
![[Pasted image 20241011123549.png]]

![[Pasted image 20241011123757.png]]

![[Pasted image 20241011123815.png]]

![[Pasted image 20241011123950.png]]

