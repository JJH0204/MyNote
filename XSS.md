![[Pasted image 20241008150628.png]]
- 1회성(반사형) 스크립트
![[Pasted image 20241008150827.png]]
- 입력 받은 문자열을 새로운 문자열 생성

```
<script>alert(document.cookie)</script>
```
![[Pasted image 20241008151019.png]]
![[Pasted image 20241008151154.png]]
- 받은 입력을 name 에 저장하고 비엇는지만 검사하고 비지 않았다면 출력

medium
![[Pasted image 20241008151337.png]]
![[Pasted image 20241008151403.png]]
- `<script>`를 공백으로 바꿔줌으로 방어
- 소문자 스크립트 또는 변형된 스트립트는 적용된다.
```
<sCript>alert(document.cookie)</script>
```
![[Pasted image 20241008151617.png]]
```
<sc<script>ript>alert(document.cookie)</script>
```

hight
![[Pasted image 20241008151739.png]]
![[Pasted image 20241008151755.png]]
- 단일 문자는 전부 공백(대소문자 관계없이)으로 preg_replace()로 처리하도록 되어있다.

`<img src=x onerror=prompt()>`
![[Pasted image 20241008152641.png]]

impossible
![[Pasted image 20241008152720.png]]
- htmlspecialchars(): html에 사용되는 모든 특수 문자 삭제
![[Pasted image 20241008152815.png]]


![[Pasted image 20241008150742.png]]
- 다용성(저장형) 스크립트

low
![[Pasted image 20241008153018.png]]
