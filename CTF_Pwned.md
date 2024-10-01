# \[정보탐색]
## IP 탐지
![[Pasted image 20241001091017.png]]
> [!Note]
> victim ip: 192.168.56.113
> service: 21/tcp(ftp), 22/tcp(ssh), 80/tcp(http)

## 웹 탐색
`http://192.168.56.113:80`
![[Pasted image 20241001091212.png]]
> I am Annlynn. I am the hacker hacked your server with your employees but they don't know how i used them. 
                   Now they worry about this. Before finding me investigate your employees first. (LOL) then find me Boomers XD..!!

> 저는 앤린입니다. 해커가 직원들과 함께 귀하의 서버를 해킹했지만 그들은 제가 어떻게 사용했는지 모릅니다. 
                   이제 그들은 이것에 대해 걱정합니다. 저를 찾기 전에 먼저 직원들을 조사하세요. (LOL) 그런 다음 저를 Boomers XD를 찾아주세요..!!!


![[Pasted image 20241001091528.png]]
- 주석에서 힌트 같은 것을 획득했다.
> <!-- I forgot to add this on last note
     You are pretty smart as i thought 
     so here i left it for you 
     She sings very well. l loved it  -->
> <!-- 마지막 메모에 추가하는 것을 잊었습니다
     당신은 생각대로 꽤 똑똑합니다 
     그래서 당신을 위해 남겨두었습니다 
     그녀는 노래를 매우 잘합니다. 정말 좋았어요 -->

### 접속 가능한 웹 디렉터리 탐색
![[Pasted image 20241001091730.png]]
- `http://192.168.56.113/index.html` (CODE:200|SIZE:3065)
  (기존 웹 페이지)
+ `http://192.168.56.113/robots.txt` (CODE:200|SIZE:41)![[Pasted image 20241001091947.png]]
+ `http://192.168.56.113/server-status` (CODE:403|SIZE:279)![[Pasted image 20241001091919.png]]

서버와 클라이언트가 주고 받는 액션이 없어 쿠키나 그 외 다른 장치는 의미 없는 것 같다.

## ftp 접속 시도
- 웹 페이지에서 획득한 정보를 활용해 ftp 서버에 접속을 시도한다.
- 실패할 경우 웹 페이지에서 추가 정보를 찾아본다.

![[Pasted image 20241001092634.png]]
- Anonymous 접속 불가능
- 다른 사용자 계정으로 유추할 만한 이름들을 모두 넣었지만 접속 실패
- 다시 웹 탐색으로 넘어간다.

## 웹 탐색 2차
`http://192.168.56.113/robots.txt`의 정보를 기반으로
`http://192.168.56.113/nothing/`에 접속하는데 성공
![[Pasted image 20241001093141.png]]

![[Pasted image 20241001093437.png]]
- 농락당하는 느낌이다.
- 유의미한 정보를 얻지 못했다.
- 접속할 수 있는 다른 웹 디렉터리는 없는 걸까?

### nikto tool
![[Pasted image 20241001094110.png]]
![[Pasted image 20241001094139.png]]
- 웹 사이트 내 취약점 탐색
  [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418)

- `http://192.168.56.113/icons/README`에 접속할 수 있음을 확인![[Pasted image 20241001094906.png]]

### dirbuster
- dirb 의 강화 버전으로 유의미한 정보를 찾을 수 없어 사용하게 되었다.
![[Pasted image 20241001103920.png]]
- 굉장히 자세히 조사하는 만큼 시간도 매우 오래 걸린다.
![[Pasted image 20241001131753.png]]
### gobuster wordlist 변경
![[Pasted image 20241001105411.png]]
![[Pasted image 20241001105854.png]]
- 뭔가 새로운 정보가 찾아 진다.
![[Pasted image 20241001105946.png]]
- 숨겨진 디렉토리 경로 리스트 인 것 같다. (하나씩 대입해서 접속 가능한지 확인해 보자)

![[Pasted image 20241001110929.png]]
- 리스트 중 유일하게 접속 가능한 페이지를 발견했다.
- ![[Pasted image 20241001111201.png]]
- 주석 내용을 읽어보니 ID 와 Password를 찾을 수 있었다.
  `$un=='ftpuser' && $pw=='B0ss_B!TcH'`
ID 와 Password를 찾았으니 ftp 접속을 해보자(이제는 가능할 것 같다.)

## ftp 접속 2차 시도
![[Pasted image 20241001111609.png]]
id: ftpuser / pw: B0ss_B!TcH
![[Pasted image 20241001112221.png]]
공유 받을 수 있는 디렉터리를 찾았지만 정확한 정보를 확인할 수 없다.
![[Pasted image 20241001112327.png]]

ssh에 ftpuser 계정으로 접속을 시도하여 파일 정보를 알아낸다.
![[Pasted image 20241001112517.png]]

ftp로 ssh key 파일을 다운 받았다.
![[Pasted image 20241001112735.png]]
![[Pasted image 20241001112839.png]]

임시 관리자 권한을 받아 올 수 없다고 한다. ![[Pasted image 20241001113146.png]]

더 얻을 수 있는 정보가 없는지 더 찾아 다닌다.
![[Pasted image 20241001113551.png]]
ftpuser 계정으로 알아낼 수 있는 정보는 이제 없는 것 같다. 
다른 계정으로 로그인 하자
ftp에서 가져온 ssh_key 값을 활용하기로 했다.
![[Pasted image 20241001115405.png]]
- user_flag를 찾았다.(ㅅㅂ...)![[Pasted image 20241001115440.png]]
- ![[Pasted image 20241001115700.png]]
> 아리아나 개인 일기 :::
> 오늘 셀레나는 저와 함께 아제이를 위해 싸웁니다. 그래서 서버에서 그녀의 hidden_text를 열었습니다. 이제 그녀는 이 문제를 책임지고 있습니다.

selena로 로그인을 시도하려는데 막혀있다.
![[Pasted image 20241001120259.png]]

다시 아리아나로 로그인해 방법을 찾는다.

아리아나 계정이 ./messenger.sh 를 실행할 권한을 가졌다.
![[Pasted image 20241001121246.png]]

home 디렉터리 아래에 ![[Pasted image 20241001120654.png]] 파일이 의심스럽다.
![[Pasted image 20241001120923.png]]
![[Pasted image 20241001120852.png]]
![[Pasted image 20241001122609.png]]
그렇다는데

selena의 쉘을 가져오는데 성공했다.
![[Pasted image 20241001122911.png]]

두번째 플래그를 찾았다.
![[Pasted image 20241001123117.png]]
서로 남탓만 하고 있는 것 같다.
![[Pasted image 20241001123217.png]]

아래 명령어로 안전한 쉘을 탈취했다.
![[Pasted image 20241001123754.png]]

실행 중인 도커 정보이다.
![[Pasted image 20241001124341.png]]
셀레나는 docker를 사용할 수 있는 사용자이다.
이전에 docker를 이용해 root 쉘을 강탈한 적 있다.
똑같이 해보자
https://www.google.com/search?q=docker+privesc&oq=&gs_lcrp=EgZjaHJvbWUqCQgAEEUYOxjCAzIJCAAQRRg7GMIDMgkIARBFGDsYwgMyCQgCEEUYOxjCAzIJCAMQRRg7GMIDMgkIBBBFGDsYwgMyCQgFEEUYOxjCAzIJCAYQRRg7GMIDMgkIBxBFGDsYwgPSAQwxNjQ2MTIyMmowajeoAgiwAgE&sourceid=chrome&ie=UTF-8
https://flast101.github.io/docker-privesc/
privesc 이미지가 설치 되어 있어
![[Pasted image 20241001131325.png]]
위 스크립트를 victim 서버에서 test.sh로 만들어 실행 시켰다.

![[Pasted image 20241001131403.png]]
![[Pasted image 20241001131444.png]]


https://medium.com/@z6157881/pwned-1-vulnhub-walkthorugh-46dce5337e06