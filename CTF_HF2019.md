# \[정보 탐색]
## 1. ip 탐색
![[Pasted image 20241001151344.png]]
- 피해자 PC를 찾았다.
### health scan
![[Pasted image 20241001155142.png]]

## 2. 포트 탐색
- 인증 관련 정보를 몰라도 접속 가능한 웹 페이지를 우선 탐색한다.
![[Pasted image 20241001155432.png]]
- wordpress로 제작된 페이지인 것을 바로 알 수 있다.
### 80/tcp(http)
![[Pasted image 20241001151853.png]]
- 워드프레스로 작성된 웹 페이지 임을 인지하고 nikto 명령어로 분석

- 별다른 소득이 없어 wpscan 진행
  (`wpscan --url 192.168.56.115 --enumerate p,u`)
  ![[Pasted image 20241001152646.png]]
  - 디렉터리에 별다른 내용은 없었다.
  ![[Pasted image 20241001152804.png]]
  - wp-google-maps: 구글 지도 관련 플러그인 정보인 것 같다.
  - 확인할 내용이 많으니 다음에 하자
- 