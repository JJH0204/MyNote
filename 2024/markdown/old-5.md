![[Pasted image 20241023093420.png]]
```html
<html>
<head>
<title>Challenge 5</title>
</head>
<body bgcolor=black>
<center>
<font color=black>
.<p>
.<p>
.<p>
.<p>
.<p>
.<p>
.<p>
</font>
<input type=button value='Login' style=border:0;width:100;background=black;color=green onmouseover=this.focus(); onclick=move('login');>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<input type=button value='Join' style=border:0;width:100;background=black;color=blue onmouseover=this.focus(); onclick=no();>

<script>
function no()
{
alert('Access_Denied');
}

function move(page)
{
if(page=='login') { location.href='mem/login.php'; }

}

</script>
</center>
</body>
</html>

```
mem/login.php
![[Pasted image 20241023093617.png]]
```html
<html>
<head>
<title>Challenge 5</title>
</head>
<body bgcolor=black>
<center><font color=white>
</font>
<font color=black>
.<p>
.<p>
.<p>
.<p>
.<p>
.<p>
.<p>
</font>
<form method=post action=login.php>
<input type=text name=id onmouseover=this.focus();><br>
<input type=password name=pw onmouseover=this.focus();><p>
<input type=submit style=border:0;background=gray;width:150 value='login' onmouseover=this.focus();>
</form>
</center>
</body>
</html>

```

mem/join.php
![[Pasted image 20241023093747.png]]
```html
<html>
    <title>Challenge 5</title>
</head>
<body bgcolor=black>
    <center>
        <script>
            l = 'a';
            ll = 'b';
            lll = 'c';
            llll = 'd';
            lllll = 'e';
            llllll = 'f';
            lllllll = 'g';
            llllllll = 'h';
            lllllllll = 'i';
            llllllllll = 'j';
            lllllllllll = 'k';
            llllllllllll = 'l';
            lllllllllllll = 'm';
            llllllllllllll = 'n';
            lllllllllllllll = 'o';
            llllllllllllllll = 'p';
            lllllllllllllllll = 'q';
            llllllllllllllllll = 'r';
            lllllllllllllllllll = 's';
            llllllllllllllllllll = 't';
            lllllllllllllllllllll = 'u';
            llllllllllllllllllllll = 'v';
            lllllllllllllllllllllll = 'w';
            llllllllllllllllllllllll = 'x';
            lllllllllllllllllllllllll = 'y';
            llllllllllllllllllllllllll = 'z';
            I = '1';
            II = '2';
            III = '3';
            IIII = '4';
            IIIII = '5';
            IIIIII = '6';
            IIIIIII = '7';
            IIIIIIII = '8';
            IIIIIIIII = '9';
            IIIIIIIIII = '0';
            li = '.';
            ii = '<';
            iii = '>';
            lIllIllIllIllIllIllIllIllIllIl = lllllllllllllll + llllllllllll + llll + llllllllllllllllllllllllll + lllllllllllllll + lllllllllllll + ll + lllllllll + lllll;
            lIIIIIIIIIIIIIIIIIIl = llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + lll + lllllllllllllll + lllllllllllllll + lllllllllll + lllllllll + lllll;
            if (eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl) == -1) {
                alert('bye');
                throw "stop";
            }
            if (eval(llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + 'U' + 'R' + 'L').indexOf(lllllllllllll + lllllllllllllll + llll + lllll + '=' + I) == -1) {
                alert('access_denied');
                throw "stop";
            } else {
                document.write('<font size=2 color=white>Join</font><p>');
                document.write('.<p>.<p>.<p>.<p>.<p>');
                document.write('<form method=post action=' + llllllllll + lllllllllllllll + lllllllll + llllllllllllll + li + llllllllllllllll + llllllll + llllllllllllllll + '>');
                document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=' + lllllllll + llll + ' maxlength=20></td></tr>');
                document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=' + llllllllllllllll + lllllllllllllllllllllll + '></td></tr>');
                document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
            }
        </script>
</body>
</html>

```
- 난독화 해제 후 풀이 진행