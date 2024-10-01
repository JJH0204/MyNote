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
#### dirb
![[Pasted image 20241001155707.png]]
- 자주 사용하는 `http://ip/wordpress/` 또는 `http://ip/admin/`은 403 에러로 찾을 수 없다.
#### nikto
![[Pasted image 20241001160011.png]]
![[Pasted image 20241001151853.png]]
- 워드프레스로 작성된 웹 페이지 임을 인지하고 nikto 명령어로 분석
- 해도 의미 있는 자료는 찾을 수 없다.
- 별다른 소득이 없어 wpscan 진행

#### wpscan
- `wpscan --url 192.168.56.115 --enumerate p,u`
```
[+] XML-RPC seems to be enabled: http://192.168.56.115/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/
```
![[Pasted image 20241001160548.png]]
```
[+] WordPress readme found: http://192.168.56.115/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
```
![[Pasted image 20241001160609.png]]
```
[+] Upload directory has listing enabled: http://192.168.56.115/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
```
![[Pasted image 20241001152646.png]]
```
[+] The external WP-Cron seems to be enabled: http://192.168.56.115/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299
```

```
[+] wp-google-maps
 | Location: http://192.168.56.115/wp-content/plugins/wp-google-maps/
 | Latest Version: 9.0.40
 | Last Updated: 2024-07-12T06:29:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | The version could not be determined.

```
![[Pasted image 20241001152804.png]]
  - wp-google-maps: 구글 지도 관련 플러그인 정보인 것 같다.

##### google