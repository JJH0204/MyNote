```
nikto -h 192.168.56.106 -C all
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.56.106
+ Target Hostname:    192.168.56.106
+ Target Port:        80
+ Start Time:         2024-09-26 01:53:36 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.37 (centos)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Apache/2.4.37 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST, TRACE .
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
^[[1;5D+ /icons/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 26639 requests: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2024-09-26 01:54:55 (GMT-4) (79 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```