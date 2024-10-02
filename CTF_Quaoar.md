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

### http://192.168.56.116/robots
![[Pasted image 20241002103414.png]]

### DIRECTORY: http://192.168.56.116/upload/
#### DIRECTORY: http://192.168.56.116/upload/account/
##### http://192.168.56.116/upload/account/index.php
![[Pasted image 20241002110039.png]]
##### DIRECTORY: http://192.168.56.116/upload/account/templates/           

#### DIRECTORY: http://192.168.56.116/upload/admins/
                                              
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
#### DIRECTORY: http://192.168.56.116/upload/framework/  

#### DIRECTORY: http://192.168.56.116/upload/include/

#### DIRECTORY: http://192.168.56.116/upload/languages/

#### DIRECTORY: http://192.168.56.116/upload/media/

#### DIRECTORY: http://192.168.56.116/upload/modules/

#### DIRECTORY: http://192.168.56.116/upload/page/

#### DIRECTORY: http://192.168.56.116/upload/search/

#### DIRECTORY: http://192.168.56.116/upload/temp/

#### DIRECTORY: http://192.168.56.116/upload/templates/

### DIRECTORY: http://192.168.56.116/wordpress/
#### http://192.168.56.116/wordpress/index.php
![[Pasted image 20241002105038.png]]

#### DIRECTORY: http://192.168.56.116/wordpress/index/

#### http://192.168.56.116/wordpress/license
```
WordPress - Web publishing software

Copyright 2015 by the contributors

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

This program incorporates work covered by the following copyright and
permission notices:

  b2 is (c) 2001, 2002 Michel Valdrighi - m@tidakada.com -
  http://tidakada.com

  Wherever third party code has been used, credit has been given in the code's
  comments.

  b2 is released under the GPL

and

  WordPress - Web publishing software

  Copyright 2003-2010 by the contributors

  WordPress is released under the GPL

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.

WRITTEN OFFER

The source code for any program binaries or compressed scripts that are
included with WordPress can be freely obtained at the following URL:

	https://wordpress.org/download/source/
```

#### http://192.168.56.116/wordpress/readme
![[Pasted image 20241002105126.png]]

#### DIRECTORY: http://192.168.56.116/wordpress/wp-admin/

#### DIRECTORY: http://192.168.56.116/wordpress/wp-content/ 

#### DIRECTORY: http://192.168.56.116/wordpress/wp-includes/
#### http://192.168.56.116/wordpress/wp-links-opml
```
This XML file does not appear to have any style information associated with it. The document tree is shown below.  

<opml version="1.0">

<head>

<title>Links for Quaoar</title>

<dateCreated>Wed, 02 Oct 2024 10:52:13 GMT</dateCreated>

<!-- generator="WordPress/3.9.14" -->

</head>

<body> </body>

</opml>
```
                                            
#### http://192.168.56.116/wordpress/wp-login
![[Pasted image 20241002105350.png]]
#### http://192.168.56.116/wordpress/wp-mail
![[Pasted image 20241002105442.png]]

#### http://192.168.56.116/wordpress/wp-signup
- 관리자 페이지에 로그인 할 수 있으면 접속 가능한 페이지 인 것 같다.
#### http://192.168.56.116/wordpress/wp-trackback
```
This XML file does not appear to have any style information associated with it. The document tree is shown below.  

<response>

<error>1</error>

<message>I really need an ID for this to work.</message>

</response>
```

#### http://192.168.56.116/wordpress/xmlrpc
![[Pasted image 20241002105610.png]]

# ㅁㄴㅇㄹ


```
---- Entering directory: http://192.168.56.116/upload/framework/ ----
==> DIRECTORY: http://192.168.56.116/upload/framework/functions/                                                   
+ http://192.168.56.116/upload/framework/index (CODE:302|SIZE:0)                                                   
+ http://192.168.56.116/upload/framework/index.php (CODE:302|SIZE:0)                                               
+ http://192.168.56.116/upload/framework/summary (CODE:403|SIZE:88)          

```

```
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
