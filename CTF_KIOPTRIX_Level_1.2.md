# README.txt
DISCLAIMER!
We at Kioptrix are not responsible for any damaged directly, or indirectly, 
caused by using this system. We suggest you do not connect this installation
to the Internet. It is, after all, a vulnerable setup. 
Please keep this in mind when playing the game.

This machine is setup to use DHCP.
Before playing the game, please modify your attacker's hosts file.
<ip>	kioptrix3.com
This challenge contains a Web Application.

If you have any questions, please direct them to:
comms[at]kioptrix.com


Hope you enjoy this challenge.
-Kioptrix Team


![[Pasted image 20241007162432.png]]
vmw 파일을 버츄얼 머신에서 구동하는 방법은 없을까?

## vmdk 파일 실행하기
- https://brunch.co.kr/@moaikim/60

# 정보 탐색
## nmap
![[Pasted image 20241007163335.png]]
![[Pasted image 20241007163414.png]]
- 22/tcp : ssh 서비스 동작 중
- 80/tcp : http 서비스 동작 중

## http://192.168.56.119
### host 설정
![[Pasted image 20241007163708.png]]
### 접속
![[Pasted image 20241007163919.png]]
![[Pasted image 20241007164009.png]]
![[Pasted image 20241007164216.png]]
![[Pasted image 20241007164327.png]]

## dirb http://kioptrix3.com/
```
-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Mon Oct  7 03:45:00 2024
URL_BASE: http://kioptrix3.com/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://kioptrix3.com/ ----
==> DIRECTORY: http://kioptrix3.com/cache/                                                                                                                              
==> DIRECTORY: http://kioptrix3.com/core/                                                                                                                               
+ http://kioptrix3.com/data (CODE:403|SIZE:324)                                                                                                                         
+ http://kioptrix3.com/favicon.ico (CODE:200|SIZE:23126)                                                                                                                
==> DIRECTORY: http://kioptrix3.com/gallery/                                                                                                                            
+ http://kioptrix3.com/index.php (CODE:200|SIZE:1819)                                                                                                                   
==> DIRECTORY: http://kioptrix3.com/modules/                                                                                                                            
==> DIRECTORY: http://kioptrix3.com/phpmyadmin/                                                                                                                         
+ http://kioptrix3.com/server-status (CODE:403|SIZE:333)                                                                                                                
==> DIRECTORY: http://kioptrix3.com/style/                                                                                                                              
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/cache/ ----
+ http://kioptrix3.com/cache/index.html (CODE:200|SIZE:1819)                                                                                                            
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/core/ ----
==> DIRECTORY: http://kioptrix3.com/core/controller/                                                                                                                    
+ http://kioptrix3.com/core/index.php (CODE:200|SIZE:0)                                                                                                                 
==> DIRECTORY: http://kioptrix3.com/core/lib/                                                                                                                           
==> DIRECTORY: http://kioptrix3.com/core/model/                                                                                                                         
==> DIRECTORY: http://kioptrix3.com/core/view/                                                                                                                          
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/gallery/ ----
+ http://kioptrix3.com/gallery/index.php (CODE:500|SIZE:5651)                                                                                                           
==> DIRECTORY: http://kioptrix3.com/gallery/photos/                                                                                                                     
==> DIRECTORY: http://kioptrix3.com/gallery/themes/                                                                                                                     
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/modules/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/phpmyadmin/ ----
+ http://kioptrix3.com/phpmyadmin/favicon.ico (CODE:200|SIZE:18902)                                                                                                     
+ http://kioptrix3.com/phpmyadmin/index.php (CODE:200|SIZE:8136)                                                                                                        
==> DIRECTORY: http://kioptrix3.com/phpmyadmin/js/                                                                                                                      
==> DIRECTORY: http://kioptrix3.com/phpmyadmin/lang/                                                                                                                    
+ http://kioptrix3.com/phpmyadmin/libraries (CODE:403|SIZE:340)                                                                                                         
+ http://kioptrix3.com/phpmyadmin/phpinfo.php (CODE:200|SIZE:0)                                                                                                         
==> DIRECTORY: http://kioptrix3.com/phpmyadmin/scripts/                                                                                                                 
==> DIRECTORY: http://kioptrix3.com/phpmyadmin/themes/                                                                                                                  
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/style/ ----
+ http://kioptrix3.com/style/admin.php (CODE:200|SIZE:356)                                                                                                              
+ http://kioptrix3.com/style/index.php (CODE:200|SIZE:0)                                                                                                                
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/core/controller/ ----
+ http://kioptrix3.com/core/controller/index.php (CODE:200|SIZE:0)                                                                                                      
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/core/lib/ ----
+ http://kioptrix3.com/core/lib/index.php (CODE:200|SIZE:0)                                                                                                             
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/core/model/ ----
+ http://kioptrix3.com/core/model/index.php (CODE:200|SIZE:0)                                                                                                           
                                                                                                                                                                        
---- Entering directory: http://kioptrix3.com/core/view/ ----
+ http://kioptrix3.com/core/view/index.php (CODE:200|SIZE:0)            
-----------------
END_TIME: Mon Oct  7 03:45:10 2024
DOWNLOADED: 46120 - FOUND: 17

```