## \[1] 자료 수집
- nmap tool 을 이용한 victim server ip 찾기![[Pasted image 20240926142539.png]]
- `http://192.168.56.106/` 접속![[Pasted image 20240926142726.png]]
- 소스 분석
  ![[Pasted image 20240926142943.png]]
  ROT47 알고리즘에 대한 언급이 있다. 무슨 연관이 있을까?
- `dirb http://192.168.56.106/`: 접근 가능한 웹 디렉터리 조사
- `http://192.168.56.106/noindex/common/css/styles`에 접근 가능함[[cybersploit_css_styles]]
- [[nikto_cybersploit2_result]]
> [!삽질기록]
> 소스에 ROT47이라는 주석과 소스 바디에 작성된 유저 이름, 비밀번호를 관찰해보면 적용 할만한 문자열이 보인다.
> 컬럼 이름이 한칸씩 밀려서 잘 몰랐지만 첫 열이 계정 이름이고 둘째 열이 비밀번호다.
- `ssh shailendra@192.168.56.106` 비밀번호 `cybersploit1`로 원격 접속에 성공했다.
- ![[Pasted image 20240926153800.png]]
  힌트를 발견했다.
  도커의 취약점을 활용해야 하는 것 같다. 
- `docker --version` 도커 버전을 우선 확인한다.![[Pasted image 20240926154034.png]]  
- 도커 관련 취약점 검색 결과![[Pasted image 20240926154526.png]]
- 마음에 드는 악성 코드를 찾았다.![[Pasted image 20240926155636.png]]
- 로컬에서 실행하기 위해서 공격자 PC에 서버를 구축하고 victim 서버에서 내려 받을 수 있도록 한다.