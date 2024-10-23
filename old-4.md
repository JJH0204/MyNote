![[Pasted image 20241023092610.png]]
```php
<?php  include "../../config.php";  
  if($_GET['view-source'] == 1) view_source();  
?><html>  
<head>  
<title>Challenge 4</title>  
<style type="text/css">  
body { background:black; color:white; font-size:9pt; }  
table { color:white; font-size:10pt; }  
</style>  
</head>  
<body><br><br>  
<center>  
<?php  
  sleep(1); // anti brute force
  if((isset($_SESSION['chall4'])) && ($_POST['key'] == $_SESSION['chall4'])) solve(4);  $hash = rand(10000000,99999999)."salt_for_you";  $_SESSION['chall4'] = $hash;  
  for($i=0;$i<500;$i++) $hash = sha1($hash);  
?><br>  
<form method=post>  
<table border=0 align=center cellpadding=10>  
<tr><td colspan=3 style=background:silver;color:green;><b><?=$hash?></b></td></tr>  
<tr align=center><td>Password</td><td><input name=key type=text size=30></td><td><input type=submit></td></tr>  
</table>  
</form>  
<a href=?view-source=1>[view-source]</a>  
</center>  
</body>  
</html>
```
- 레인보우 테이블?