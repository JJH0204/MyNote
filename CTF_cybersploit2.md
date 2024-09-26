## \[1] 자료 수집
- nmap tool 을 이용한 victim server ip 찾기![[Pasted image 20240926142539.png]]
- `http://192.168.56.106/` 접속![[Pasted image 20240926142726.png]]
- 소스 분석
  ![[Pasted image 20240926142943.png]]
  ROT47 알고리즘에 대한 언급이 있다. 무슨 연관이 있을까?
- `dirb http://192.168.56.106/`: 접근 가능한 웹 디렉터리 조사
- `http://192.168.56.106/noindex/common/css/styles`에 접근 가능함[[cybersploit_css_styles]]
- 