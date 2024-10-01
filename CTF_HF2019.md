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

[+] WordPress readme found: http://192.168.56.115/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.56.115/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.56.115/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.2.3 identified (Insecure, released on 2019-09-04).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.56.115/?feed=rss2, <generator>https://wordpress.org/?v=5.2.3</generator>
 |  - http://192.168.56.115/?feed=comments-rss2, <generator>https://wordpress.org/?v=5.2.3</generator>

[+] WordPress theme in use: twentyseventeen
 | Location: http://192.168.56.115/wp-content/themes/twentyseventeen/
 | Last Updated: 2024-07-16T00:00:00.000Z
 | Readme: http://192.168.56.115/wp-content/themes/twentyseventeen/README.txt
 | [!] The version is out of date, the latest version is 3.7
 | Style URL: http://192.168.56.115/wp-content/themes/twentyseventeen/style.css?ver=5.2.3
 | Style Name: Twenty Seventeen
 | Style URI: https://wordpress.org/themes/twentyseventeen/
 | Description: Twenty Seventeen brings your site to life with header video and immersive featured images. With a fo...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 2.2 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.115/wp-content/themes/twentyseventeen/style.css?ver=5.2.3, Match: 'Version: 2.2'

[+] Enumerating Most Popular Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] wp-google-maps
 | Location: http://192.168.56.115/wp-content/plugins/wp-google-maps/
 | Latest Version: 9.0.40
 | Last Updated: 2024-07-12T06:29:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | The version could not be determined.

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <======================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] webmaster
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Tue Oct  1 03:03:22 2024
[+] Requests Done: 62
[+] Cached Requests: 7
[+] Data Sent: 18.341 KB
[+] Data Received: 523.76 KB
[+] Memory used: 265.371 MB
[+] Elapsed time: 00:00:08

```
  ![[Pasted image 20241001152646.png]]
  - 디렉터리에 별다른 내용은 없었다.
  ![[Pasted image 20241001152804.png]]
  - wp-google-maps: 구글 지도 관련 플러그인 정보인 것 같다.
  - 확인할 내용이 많으니 다음에 하자
- 