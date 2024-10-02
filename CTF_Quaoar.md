# \[정보 탐색]
## 1. nmap
`nmap 192.168.56.0/24`
![[Pasted image 20241002102358.png]]

## 2. 웹 접속
![[Pasted image 20241002102508.png]]
![[Pasted image 20241002102535.png]]
- 클릭 시 이미지를 보여주는 기능이 동작 중이다.
![[Pasted image 20241002102631.png]]

## dirb
- 추가로 접속 가능한 페이지가 있는지 탐색하기 위해 명령어 실행
- `dirb http://192.168.56.116/`
### http://192.168.56.116/LICENSE
```
License
=======
LEPTON Core is released under the GNU General Public License,
Copyright (C) 2010-2016 LEPTON CMS Project
http://www.gnu.org/licenses/gpl.txt


LICENSE INFORMATION

LEPTON Core is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

Notice: LEPTON CMS package files are released under several different licences.
Please see the individual license in the header of each single file or info.php of modules and templates..

LEPTON CMS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA. 


LICENSE Terms

1. All existing copyright notices in every single file have to stay untouched
2. Following text and links in the backend must stay visible and untouched:

 <a href="http://www.LEPTON-cms.org" title="LEPTON CMS" target="_blank">LEPTON Core</a> is released under the
 <a href="http://www.gnu.org/licenses/gpl.html" title="LEPTON Core is GPL" target="_blank">GNU General Public License</a>.
 <br /><a href="http://www.LEPTON-cms.org" title="LEPTON Package" target="_blank">LEPTON CMS Package</a> is released under several different licenses. 

3. A frontend-link to 
	http://www.lepton-cms.org 
   is aprecciated.
```



```
---- Scanning URL: http://192.168.56.116/ ----                                                          
+ http://192.168.56.116/hacking (CODE:200|SIZE:616848)                                                             
+ http://192.168.56.116/index (CODE:200|SIZE:100)                                                                  
+ http://192.168.56.116/index.html (CODE:200|SIZE:100)                                                             
+  (CODE:200|SIZE:1672)                                                               
+ http://192.168.56.116/robots (CODE:200|SIZE:271)                                                                 
+ http://192.168.56.116/robots.txt (CODE:200|SIZE:271)                                               
==> DIRECTORY: http://192.168.56.116/upload/                                                                       
==> DIRECTORY: http://192.168.56.116/wordpress/ # 워드프레스 사용중인 것 같다.

---- Entering directory: http://192.168.56.116/upload/ ----
==> DIRECTORY: http://192.168.56.116/upload/account/                                                               
==> DIRECTORY: http://192.168.56.116/upload/admins/ # 관리자 폴더로 추측된다.                                  
+ http://192.168.56.116/upload/config (CODE:200|SIZE:0)                                                            
==> DIRECTORY: http://192.168.56.116/upload/framework/                                                             
==> DIRECTORY: http://192.168.56.116/upload/include/                                                               
+ http://192.168.56.116/upload/index (CODE:200|SIZE:3040)                                                          
+ http://192.168.56.116/upload/index.php (CODE:200|SIZE:3040)                                                      
==> DIRECTORY: http://192.168.56.116/upload/languages/                                                             
==> DIRECTORY: http://192.168.56.116/upload/media/                                                                 
==> DIRECTORY: http://192.168.56.116/upload/modules/                                                               
==> DIRECTORY: http://192.168.56.116/upload/page/                                                                  
==> DIRECTORY: http://192.168.56.116/upload/search/                                                                
==> DIRECTORY: http://192.168.56.116/upload/temp/                                                                  
==> DIRECTORY: http://192.168.56.116/upload/templates/                                                             
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/ ----
==> DIRECTORY: http://192.168.56.116/wordpress/index/                                                              
+ http://192.168.56.116/wordpress/index.php (CODE:301|SIZE:0)                                                      
+ http://192.168.56.116/wordpress/license (CODE:200|SIZE:19930)                                                    
+ http://192.168.56.116/wordpress/readme (CODE:200|SIZE:7195)                                                      
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/                                                           
+ http://192.168.56.116/wordpress/wp-blog-header (CODE:200|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-config (CODE:200|SIZE:0)                                                      
==> DIRECTORY: http://192.168.56.116/wordpress/wp-content/                                                         
+ http://192.168.56.116/wordpress/wp-cron (CODE:200|SIZE:0)                                                        
==> DIRECTORY: http://192.168.56.116/wordpress/wp-includes/                                                        
+ http://192.168.56.116/wordpress/wp-links-opml (CODE:200|SIZE:217)                                                
+ http://192.168.56.116/wordpress/wp-load (CODE:200|SIZE:0)                                                        
+ http://192.168.56.116/wordpress/wp-login (CODE:200|SIZE:2530)                                                    
+ http://192.168.56.116/wordpress/wp-mail (CODE:500|SIZE:3011)                                                     
+ http://192.168.56.116/wordpress/wp-settings (CODE:500|SIZE:0)                                                    
+ http://192.168.56.116/wordpress/wp-signup (CODE:302|SIZE:0)                                                      
+ http://192.168.56.116/wordpress/wp-trackback (CODE:200|SIZE:135)                                                 
+ http://192.168.56.116/wordpress/xmlrpc (CODE:200|SIZE:42)                                                        
+ http://192.168.56.116/wordpress/xmlrpc.php (CODE:200|SIZE:42)                                                    
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/account/ ----
==> DIRECTORY: http://192.168.56.116/upload/account/css/                                                           
+ http://192.168.56.116/upload/account/forgot (CODE:302|SIZE:0)                                                    
+ http://192.168.56.116/upload/account/index (CODE:302|SIZE:0)                                                     
+ http://192.168.56.116/upload/account/index.php (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/upload/account/login (CODE:302|SIZE:0)                                                     
+ http://192.168.56.116/upload/account/logout (CODE:302|SIZE:0)                                                    
+ http://192.168.56.116/upload/account/preferences (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/account/signup (CODE:302|SIZE:0)                                                    
==> DIRECTORY: http://192.168.56.116/upload/account/templates/                                                     
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/ ----
==> DIRECTORY: http://192.168.56.116/upload/admins/access/                                                         
==> DIRECTORY: http://192.168.56.116/upload/admins/addons/                                                         
==> DIRECTORY: http://192.168.56.116/upload/admins/admintools/                                                     
==> DIRECTORY: http://192.168.56.116/upload/admins/groups/                                                         
+ http://192.168.56.116/upload/admins/index (CODE:302|SIZE:0)                                                      
+ http://192.168.56.116/upload/admins/index.php (CODE:302|SIZE:0)                                                  
==> DIRECTORY: http://192.168.56.116/upload/admins/interface/                                                      
==> DIRECTORY: http://192.168.56.116/upload/admins/languages/                                                      
==> DIRECTORY: http://192.168.56.116/upload/admins/login/                                                          
==> DIRECTORY: http://192.168.56.116/upload/admins/logout/                                                         
==> DIRECTORY: http://192.168.56.116/upload/admins/media/                                                          
==> DIRECTORY: http://192.168.56.116/upload/admins/modules/                                                        
==> DIRECTORY: http://192.168.56.116/upload/admins/pages/                                                          
==> DIRECTORY: http://192.168.56.116/upload/admins/preferences/                                                    
==> DIRECTORY: http://192.168.56.116/upload/admins/profiles/                                                       
==> DIRECTORY: http://192.168.56.116/upload/admins/service/                                                        
==> DIRECTORY: http://192.168.56.116/upload/admins/settings/                                                       
==> DIRECTORY: http://192.168.56.116/upload/admins/start/                                                          
==> DIRECTORY: http://192.168.56.116/upload/admins/support/                                                        
==> DIRECTORY: http://192.168.56.116/upload/admins/templates/                                                      
==> DIRECTORY: http://192.168.56.116/upload/admins/users/                                                          
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/framework/ ----
==> DIRECTORY: http://192.168.56.116/upload/framework/functions/                                                   
+ http://192.168.56.116/upload/framework/index (CODE:302|SIZE:0)                                                   
+ http://192.168.56.116/upload/framework/index.php (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/framework/summary (CODE:403|SIZE:88)                                                
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/include/ ----
+ http://192.168.56.116/upload/include/index (CODE:302|SIZE:0)                                                     
+ http://192.168.56.116/upload/include/index.php (CODE:302|SIZE:0)                                                 
==> DIRECTORY: http://192.168.56.116/upload/include/yui/                                                           
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/languages/ ----
+ http://192.168.56.116/upload/languages/index (CODE:302|SIZE:0)                                                   
+ http://192.168.56.116/upload/languages/index.php (CODE:302|SIZE:0)                                               
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/media/ ----
+ http://192.168.56.116/upload/media/index (CODE:302|SIZE:0)                                                       
+ http://192.168.56.116/upload/media/index.php (CODE:302|SIZE:0)                                                   
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/ ----
+ http://192.168.56.116/upload/modules/admin (CODE:403|SIZE:79)                                                    
+ http://192.168.56.116/upload/modules/admin.php (CODE:403|SIZE:79)                                                
+ http://192.168.56.116/upload/modules/index (CODE:302|SIZE:0)                                                     
+ http://192.168.56.116/upload/modules/index.php (CODE:302|SIZE:0)                                                 
==> DIRECTORY: http://192.168.56.116/upload/modules/news/                                                          
==> DIRECTORY: http://192.168.56.116/upload/modules/wysiwyg/                                                       
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/page/ ----
+ http://192.168.56.116/upload/page/index (CODE:200|SIZE:0)                                                        
+ http://192.168.56.116/upload/page/index.php (CODE:200|SIZE:0)                                                    
==> DIRECTORY: http://192.168.56.116/upload/page/posts/                                                            
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/search/ ----
+ http://192.168.56.116/upload/search/index (CODE:200|SIZE:3627)                                                   
+ http://192.168.56.116/upload/search/index.php (CODE:200|SIZE:3627)                                               
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/temp/ ----
+ http://192.168.56.116/upload/temp/index (CODE:302|SIZE:0)                                                        
+ http://192.168.56.116/upload/temp/index.php (CODE:302|SIZE:0)                                                    
==> DIRECTORY: http://192.168.56.116/upload/temp/search/                                                           
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/templates/ ----
==> DIRECTORY: http://192.168.56.116/upload/templates/blank/                                                       
+ http://192.168.56.116/upload/templates/index (CODE:302|SIZE:0)                                                   
+ http://192.168.56.116/upload/templates/index.php (CODE:302|SIZE:0)                                               
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/index/ ----
(!) WARNING: NOT_FOUND[] not stable, unable to determine correct URLs {30X}.
    (Try using FineTunning: '-f')
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/ ----
+ http://192.168.56.116/wordpress/wp-admin/about (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-admin/admin (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-admin/admin.php (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/wordpress/wp-admin/comment (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/wordpress/wp-admin/credits (CODE:302|SIZE:0)                                               
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/css/                                                       
+ http://192.168.56.116/wordpress/wp-admin/customize (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/wordpress/wp-admin/edit (CODE:302|SIZE:0)                                                  
+ http://192.168.56.116/wordpress/wp-admin/export (CODE:302|SIZE:0)                                                
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/images/                                                    
+ http://192.168.56.116/wordpress/wp-admin/import (CODE:302|SIZE:0)                                                
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/includes/                                                  
+ http://192.168.56.116/wordpress/wp-admin/index (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-admin/index.php (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/wordpress/wp-admin/install (CODE:200|SIZE:1080)                                            
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/js/                                                        
+ http://192.168.56.116/wordpress/wp-admin/link (CODE:302|SIZE:0)                                                  
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/maint/                                                     
+ http://192.168.56.116/wordpress/wp-admin/media (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-admin/menu (CODE:500|SIZE:0)                                                  
+ http://192.168.56.116/wordpress/wp-admin/moderation (CODE:302|SIZE:0)                                            
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/network/                                                   
+ http://192.168.56.116/wordpress/wp-admin/options (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/wordpress/wp-admin/plugins (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/wordpress/wp-admin/post (CODE:302|SIZE:0)                                                  
+ http://192.168.56.116/wordpress/wp-admin/profile (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/wordpress/wp-admin/themes (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/wordpress/wp-admin/tools (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-admin/update (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/wordpress/wp-admin/upgrade (CODE:200|SIZE:1173)                                            
+ http://192.168.56.116/wordpress/wp-admin/upload (CODE:302|SIZE:0)                                                
==> DIRECTORY: http://192.168.56.116/wordpress/wp-admin/user/                                                      
+ http://192.168.56.116/wordpress/wp-admin/users (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/wordpress/wp-admin/widgets (CODE:302|SIZE:0)                                               
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-content/ ----
+ http://192.168.56.116/wordpress/wp-content/index (CODE:200|SIZE:0)                                               
+ http://192.168.56.116/wordpress/wp-content/index.php (CODE:200|SIZE:0)                                           
==> DIRECTORY: http://192.168.56.116/wordpress/wp-content/plugins/                                                 
==> DIRECTORY: http://192.168.56.116/wordpress/wp-content/themes/                                                  
==> DIRECTORY: http://192.168.56.116/wordpress/wp-content/upgrade/                                                 
==> DIRECTORY: http://192.168.56.116/wordpress/wp-content/uploads/                                                 
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-includes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/account/css/ ----
+ http://192.168.56.116/upload/account/css/frontend (CODE:200|SIZE:1931)                                           
+ http://192.168.56.116/upload/account/css/index (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/upload/account/css/index.php (CODE:302|SIZE:0)                                             
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/account/templates/ ----
+ http://192.168.56.116/upload/account/templates/index (CODE:302|SIZE:0)                                           
+ http://192.168.56.116/upload/account/templates/index.php (CODE:302|SIZE:0)                                       
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/access/ ----
+ http://192.168.56.116/upload/admins/access/index (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/admins/access/index.php (CODE:302|SIZE:0)                                           
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/addons/ ----
+ http://192.168.56.116/upload/admins/addons/index (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/admins/addons/index.php (CODE:302|SIZE:0)                                           
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/admintools/ ----
+ http://192.168.56.116/upload/admins/admintools/index (CODE:302|SIZE:0)                                           
+ http://192.168.56.116/upload/admins/admintools/index.php (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/upload/admins/admintools/tool (CODE:302|SIZE:0)                                            
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/groups/ ----
+ http://192.168.56.116/upload/admins/groups/add (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/upload/admins/groups/groups (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/admins/groups/index (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/admins/groups/index.php (CODE:302|SIZE:0)                                           
+ http://192.168.56.116/upload/admins/groups/save (CODE:302|SIZE:0)                                                
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/interface/ ----
+ http://192.168.56.116/upload/admins/interface/index (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/interface/index.php (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/upload/admins/interface/version (CODE:403|SIZE:90)                                         
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/languages/ ----
+ http://192.168.56.116/upload/admins/languages/details (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/upload/admins/languages/index (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/languages/index.php (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/upload/admins/languages/install (CODE:500|SIZE:0)                                          
+ http://192.168.56.116/upload/admins/languages/uninstall (CODE:302|SIZE:0)                                        
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/login/ ----
==> DIRECTORY: http://192.168.56.116/upload/admins/login/forgot/                                                   
+ http://192.168.56.116/upload/admins/login/index (CODE:200|SIZE:2929)                                             
+ http://192.168.56.116/upload/admins/login/index.php (CODE:200|SIZE:2929)                                         
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/logout/ ----
+ http://192.168.56.116/upload/admins/logout/index (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/admins/logout/index.php (CODE:302|SIZE:0)                                           
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/media/ ----
+ http://192.168.56.116/upload/admins/media/index (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/upload/admins/media/index.php (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/media/thumb (CODE:200|SIZE:0)                                                
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/modules/ ----
+ http://192.168.56.116/upload/admins/modules/details (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/modules/index (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/admins/modules/index.php (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/upload/admins/modules/install (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/modules/uninstall (CODE:302|SIZE:0)                                          
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/pages/ ----
+ http://192.168.56.116/upload/admins/pages/add (CODE:302|SIZE:0)                                                  
+ http://192.168.56.116/upload/admins/pages/delete (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/admins/pages/index (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/upload/admins/pages/index.php (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/pages/modify (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/admins/pages/restore (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/admins/pages/save (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/upload/admins/pages/sections (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/upload/admins/pages/settings (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/upload/admins/pages/trash (CODE:302|SIZE:0)                                                
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/preferences/ ----
+ http://192.168.56.116/upload/admins/preferences/index (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/upload/admins/preferences/index.php (CODE:302|SIZE:0)                                      
+ http://192.168.56.116/upload/admins/preferences/save (CODE:302|SIZE:0)                                           
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/profiles/ ----
+ http://192.168.56.116/upload/admins/profiles/index (CODE:200|SIZE:324)                                           
+ http://192.168.56.116/upload/admins/profiles/index.php (CODE:200|SIZE:324)                                       
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/service/ ----
+ http://192.168.56.116/upload/admins/service/index (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/admins/service/index.php (CODE:302|SIZE:0)                                          
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/settings/ ----
+ http://192.168.56.116/upload/admins/settings/index (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/upload/admins/settings/index.php (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/upload/admins/settings/save (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/admins/settings/setting (CODE:200|SIZE:3839)                                        
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/start/ ----
+ http://192.168.56.116/upload/admins/start/index (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/upload/admins/start/index.php (CODE:302|SIZE:0)                                            
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/support/ ----
+ http://192.168.56.116/upload/admins/support/index (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/admins/support/index.php (CODE:302|SIZE:0)                                          
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/templates/ ----
+ http://192.168.56.116/upload/admins/templates/details (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/upload/admins/templates/index (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/templates/index.php (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/upload/admins/templates/install (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/upload/admins/templates/uninstall (CODE:302|SIZE:0)                                        
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/users/ ----
+ http://192.168.56.116/upload/admins/users/add (CODE:302|SIZE:0)                                                  
+ http://192.168.56.116/upload/admins/users/index (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/upload/admins/users/index.php (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/admins/users/save (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/upload/admins/users/users (CODE:302|SIZE:0)                                                
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/framework/functions/ ----
+ http://192.168.56.116/upload/framework/functions/index (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/upload/framework/functions/index.php (CODE:302|SIZE:0)                                     
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/include/yui/ ----
==> DIRECTORY: http://192.168.56.116/upload/include/yui/event/                                                     
+ http://192.168.56.116/upload/include/yui/index (CODE:302|SIZE:0)                                                 
+ http://192.168.56.116/upload/include/yui/index.php (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/upload/include/yui/README (CODE:200|SIZE:8488)                                             
==> DIRECTORY: http://192.168.56.116/upload/include/yui/yahoo/                                                     
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/news/ ----
+ http://192.168.56.116/upload/modules/news/add (CODE:403|SIZE:82)                                                 
+ http://192.168.56.116/upload/modules/news/comment (CODE:302|SIZE:0)                                              
==> DIRECTORY: http://192.168.56.116/upload/modules/news/css/                                                      
+ http://192.168.56.116/upload/modules/news/delete (CODE:403|SIZE:85)                                              
+ http://192.168.56.116/upload/modules/news/icon (CODE:200|SIZE:1058)                                              
+ http://192.168.56.116/upload/modules/news/index (CODE:302|SIZE:0)                                                
+ http://192.168.56.116/upload/modules/news/index.php (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/modules/news/info (CODE:403|SIZE:83)                                                
+ http://192.168.56.116/upload/modules/news/info.php (CODE:403|SIZE:83)                                            
+ http://192.168.56.116/upload/modules/news/install (CODE:403|SIZE:86)                                             
==> DIRECTORY: http://192.168.56.116/upload/modules/news/languages/                                                
+ http://192.168.56.116/upload/modules/news/modify (CODE:403|SIZE:85)                                              
+ http://192.168.56.116/upload/modules/news/rss (CODE:302|SIZE:0)                                                  
+ http://192.168.56.116/upload/modules/news/search (CODE:403|SIZE:85)                                              
==> DIRECTORY: http://192.168.56.116/upload/modules/news/templates/                                                
+ http://192.168.56.116/upload/modules/news/uninstall (CODE:403|SIZE:88)                                           
+ http://192.168.56.116/upload/modules/news/upgrade (CODE:403|SIZE:86)                                             
+ http://192.168.56.116/upload/modules/news/view (CODE:403|SIZE:83)                                                
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/wysiwyg/ ----
+ http://192.168.56.116/upload/modules/wysiwyg/add (CODE:403|SIZE:85)                                              
+ http://192.168.56.116/upload/modules/wysiwyg/delete (CODE:403|SIZE:88)                                           
+ http://192.168.56.116/upload/modules/wysiwyg/icon (CODE:200|SIZE:1058)                                           
+ http://192.168.56.116/upload/modules/wysiwyg/index (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/upload/modules/wysiwyg/index.php (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/upload/modules/wysiwyg/info (CODE:403|SIZE:86)                                             
+ http://192.168.56.116/upload/modules/wysiwyg/info.php (CODE:403|SIZE:86)                                         
+ http://192.168.56.116/upload/modules/wysiwyg/install (CODE:403|SIZE:89)                                          
==> DIRECTORY: http://192.168.56.116/upload/modules/wysiwyg/languages/                                             
+ http://192.168.56.116/upload/modules/wysiwyg/modify (CODE:403|SIZE:88)                                           
+ http://192.168.56.116/upload/modules/wysiwyg/save (CODE:302|SIZE:0)                                              
+ http://192.168.56.116/upload/modules/wysiwyg/search (CODE:403|SIZE:88)                                           
==> DIRECTORY: http://192.168.56.116/upload/modules/wysiwyg/templates/                                             
+ http://192.168.56.116/upload/modules/wysiwyg/upgrade (CODE:403|SIZE:89)                                          
+ http://192.168.56.116/upload/modules/wysiwyg/view (CODE:403|SIZE:86)                                             
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/page/posts/ ----
+ http://192.168.56.116/upload/page/posts/index (CODE:302|SIZE:0)                                                  
+ http://192.168.56.116/upload/page/posts/index.php (CODE:302|SIZE:0)                                              
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/temp/search/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/templates/blank/ ----
+ http://192.168.56.116/upload/templates/blank/index (CODE:302|SIZE:0)                                             
+ http://192.168.56.116/upload/templates/blank/index.php (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/upload/templates/blank/info (CODE:403|SIZE:86)                                             
+ http://192.168.56.116/upload/templates/blank/info.php (CODE:403|SIZE:86)                                         
+ http://192.168.56.116/upload/templates/blank/preview (CODE:200|SIZE:1377)                                        
+ http://192.168.56.116/upload/templates/blank/template (CODE:200|SIZE:507)                                        
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/images/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/includes/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/maint/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/network/ ----
+ http://192.168.56.116/wordpress/wp-admin/network/about (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/wordpress/wp-admin/network/admin (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/wordpress/wp-admin/network/admin.php (CODE:302|SIZE:0)                                     
+ http://192.168.56.116/wordpress/wp-admin/network/credits (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/wordpress/wp-admin/network/edit (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/wordpress/wp-admin/network/index (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/wordpress/wp-admin/network/index.php (CODE:302|SIZE:0)                                     
+ http://192.168.56.116/wordpress/wp-admin/network/menu (CODE:500|SIZE:0)                                          
+ http://192.168.56.116/wordpress/wp-admin/network/plugins (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/wordpress/wp-admin/network/profile (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/wordpress/wp-admin/network/settings (CODE:302|SIZE:0)                                      
+ http://192.168.56.116/wordpress/wp-admin/network/setup (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/wordpress/wp-admin/network/sites (CODE:302|SIZE:0)                                         
+ http://192.168.56.116/wordpress/wp-admin/network/themes (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/wordpress/wp-admin/network/update (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/wordpress/wp-admin/network/upgrade (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/wordpress/wp-admin/network/users (CODE:302|SIZE:0)                                         
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-admin/user/ ----
+ http://192.168.56.116/wordpress/wp-admin/user/about (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/wordpress/wp-admin/user/admin (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/wordpress/wp-admin/user/admin.php (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/wordpress/wp-admin/user/credits (CODE:302|SIZE:0)                                          
+ http://192.168.56.116/wordpress/wp-admin/user/index (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/wordpress/wp-admin/user/index.php (CODE:302|SIZE:0)                                        
+ http://192.168.56.116/wordpress/wp-admin/user/menu (CODE:500|SIZE:0)                                             
+ http://192.168.56.116/wordpress/wp-admin/user/profile (CODE:302|SIZE:0)                                          
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-content/plugins/ ----
+ http://192.168.56.116/wordpress/wp-content/plugins/hello (CODE:500|SIZE:0)                                       
+ http://192.168.56.116/wordpress/wp-content/plugins/index (CODE:200|SIZE:0)                                       
+ http://192.168.56.116/wordpress/wp-content/plugins/index.php (CODE:200|SIZE:0)                                   
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-content/themes/ ----
+ http://192.168.56.116/wordpress/wp-content/themes/index (CODE:200|SIZE:0)                                        
+ http://192.168.56.116/wordpress/wp-content/themes/index.php (CODE:200|SIZE:0)                                    
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-content/upgrade/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/wordpress/wp-content/uploads/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/admins/login/forgot/ ----
+ http://192.168.56.116/upload/admins/login/forgot/index (CODE:200|SIZE:2531)                                      
+ http://192.168.56.116/upload/admins/login/forgot/index.php (CODE:200|SIZE:2531)                                  
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/include/yui/event/ ----
+ http://192.168.56.116/upload/include/yui/event/event (CODE:200|SIZE:87537)                                       
+ http://192.168.56.116/upload/include/yui/event/index (CODE:302|SIZE:0)                                           
+ http://192.168.56.116/upload/include/yui/event/index.php (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/upload/include/yui/event/README (CODE:200|SIZE:9807)                                       
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/include/yui/yahoo/ ----
+ http://192.168.56.116/upload/include/yui/yahoo/index (CODE:302|SIZE:0)                                           
+ http://192.168.56.116/upload/include/yui/yahoo/index.php (CODE:302|SIZE:0)                                       
+ http://192.168.56.116/upload/include/yui/yahoo/README (CODE:200|SIZE:2889)                                       
+ http://192.168.56.116/upload/include/yui/yahoo/yahoo (CODE:200|SIZE:35223)                                       
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/news/css/ ----
+ http://192.168.56.116/upload/modules/news/css/backend (CODE:200|SIZE:1416)                                       
+ http://192.168.56.116/upload/modules/news/css/frontend (CODE:200|SIZE:1771)                                      
+ http://192.168.56.116/upload/modules/news/css/index (CODE:302|SIZE:0)                                            
+ http://192.168.56.116/upload/modules/news/css/index.php (CODE:302|SIZE:0)                                        
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/news/languages/ ----
+ http://192.168.56.116/upload/modules/news/languages/index (CODE:302|SIZE:0)                                      
+ http://192.168.56.116/upload/modules/news/languages/index.php (CODE:302|SIZE:0)                                  
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/news/templates/ ----
==> DIRECTORY: http://192.168.56.116/upload/modules/news/templates/backend/                                        
+ http://192.168.56.116/upload/modules/news/templates/index (CODE:302|SIZE:0)                                      
+ http://192.168.56.116/upload/modules/news/templates/index.php (CODE:302|SIZE:0)                                  
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/wysiwyg/languages/ ----
+ http://192.168.56.116/upload/modules/wysiwyg/languages/index (CODE:302|SIZE:0)                                   
+ http://192.168.56.116/upload/modules/wysiwyg/languages/index.php (CODE:302|SIZE:0)                               
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/wysiwyg/templates/ ----
+ http://192.168.56.116/upload/modules/wysiwyg/templates/index (CODE:302|SIZE:0)                                   
+ http://192.168.56.116/upload/modules/wysiwyg/templates/index.php (CODE:302|SIZE:0)                               
                                                                                                                   
---- Entering directory: http://192.168.56.116/upload/modules/news/templates/backend/ ----
+ http://192.168.56.116/upload/modules/news/templates/backend/index (CODE:302|SIZE:0)                              
+ http://192.168.56.116/upload/modules/news/templates/backend/index.php (CODE:302|SIZE:0)                          
                                                                                                                   
-----------------
END_TIME: Tue Oct  1 21:28:56 2024
DOWNLOADED: 258272 - FOUND: 252
```
