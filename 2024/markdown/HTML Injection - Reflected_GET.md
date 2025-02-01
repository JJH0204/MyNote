# Low
![[Pasted image 20241010104257.png]]![[Pasted image 20241010104308.png]]![[Pasted image 20241010104324.png]]![[Pasted image 20241010104332.png]]
html 코드의 삽입 취약점이 있는 것을 알 수 있음
![[Pasted image 20241010104403.png]]
사용자의 입력을 저장하는 파라미터에 위약함을 알 수 있다.

# Medium
![[Pasted image 20241010104554.png]]![[Pasted image 20241010104558.png]]
문자열로 처리된다.

# Check
![[Pasted image 20241010105258.png]]
![[Pasted image 20241010110315.png]]![[Pasted image 20241010110445.png]]
![[Pasted image 20241010110606.png]]
## low_level
![[Pasted image 20241010110814.png]]

## Medium
![[Pasted image 20241010110909.png]]
<: gt
\>: lt
[아스크코드](https://www.ascii-code.com/)로 인코딩해 입력하면 될 것 같다. = [[URL 인코딩]]
![[Pasted image 20241010111637.png]]
![[Pasted image 20241010111441.png]]
```
<h1>hello</h1> = %3ch1%3ehello%3c%2fh1%3e
```
![[Pasted image 20241010111748.png]]
- html은 입력을 서버에 넘길때 아스키 코드로 인코딩해 전달
- 서버는 받은 입력을 디코딩
- 두 값의 비교는 인코딩 전 입력 값으로 비교하기 때문에 먼저 인코딩하여 전달할 경우 처리를 우회할 수 있게 된다.

## high
![[Pasted image 20241010111951.png]]

![[Pasted image 20241010111000.png]]
- html injection을 방어하는 가장 좋은 방법은 htmlspecialchars()를 사용하는 것
- 또는 입력하는 문자열의 길이를 제한하는 것 또한 좋은 방법이 될 것이다.

