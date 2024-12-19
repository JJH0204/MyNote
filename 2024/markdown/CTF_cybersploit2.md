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
  ![[Pasted image 20240926160307.png]]
  wget 을 사용할 수 없구나...
- 다른 방법을 생각해보자 ...
  victim에서 도커는 사용가능했으니까 도커를 이용해서 파일을 올리고 내려받을 수 있것 같다.
---
다른 공격 방법
- Docker의 취약점을 활용해 루트 쉘을 얻을 수 있는 이미지 파일이 있다.
- https://gtfobins.github.io/gtfobins/docker/ alpine
- 이 이미지를 서버에서 실행하면 일반 사용자가 관리자 권한을 가지 쉘을 사용할 수 있게 된다.
- ![[Pasted image 20240926174416.png]]
- victim 은 외부로 원격 접속, 접근 등이 불가능한점을 인지하고 Attacker에서 victim으로 이미지 파일을 전달할 방법을 찾아야 한다.

![[Pasted image 20240926174548.png]]
이미지 설치
![[Pasted image 20240926174606.png]]
이미지 파일을 압축해 전달할 준비
![[Pasted image 20240926174654.png]]
도커의 scp 명령어를 통해 압축한 이미지 파일 전송

![[Pasted image 20240926174749.png]]
id 명령어를 통해 사용자가 docker 사용자임을 확인
![[Pasted image 20240926174816.png]]
공격자로부터 받은 압축파일 확인
![[Pasted image 20240926174838.png]]
압축해제 (해도 표시는 안됨)
![[Pasted image 20240926174857.png]]
취약점을 사용하는 이미지를 실행시킨다.
![[Pasted image 20240926174923.png]]
쉘을 얻는데 성공

---
CyberSploit 2
다양한 도구를 통해 정보 수집 후 접속
페이지 소스 보기 -> rot47 확인 -> rot47 검색 후 decoder 사이트 이동
 decoder (shailendra / cybersploit1) 

ssh shailendra@대상 IP
ls, uname -a, cat /etc/issue, cat hint.txt, id 등 명령어로 시스템 정보 확인

docker 계정 확인 후 docker privilege escalation 검색
docker | GTFOBins : github 사이트 확인

ssh
docker run -v /:/mnt --run -it alpine chroot /mnt sh
id -> root 상승 확인
cd /root
flag.txt 확인