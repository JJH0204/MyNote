![[Pasted image 20241023094333.png]]
```php
<?php  
include "../../config.php";  
if($_GET['view_source']) view_source();  
if(!$_COOKIE['user']){  $val_id="guest";  $val_pw="123qwe";  
  for($i=0;$i<20;$i++){    $val_id=base64_encode($val_id);    $val_pw=base64_encode($val_pw);  
  }  $val_id=str_replace("1","!",$val_id);  $val_id=str_replace("2","@",$val_id);  $val_id=str_replace("3","$",$val_id);  $val_id=str_replace("4","^",$val_id);  $val_id=str_replace("5","&",$val_id);  $val_id=str_replace("6","*",$val_id);  $val_id=str_replace("7","(",$val_id);  $val_id=str_replace("8",")",$val_id);  $val_pw=str_replace("1","!",$val_pw);  $val_pw=str_replace("2","@",$val_pw);  $val_pw=str_replace("3","$",$val_pw);  $val_pw=str_replace("4","^",$val_pw);  $val_pw=str_replace("5","&",$val_pw);  $val_pw=str_replace("6","*",$val_pw);  $val_pw=str_replace("7","(",$val_pw);  $val_pw=str_replace("8",")",$val_pw);  Setcookie("user",$val_id,time()+86400,"/challenge/web-06/");  Setcookie("password",$val_pw,time()+86400,"/challenge/web-06/");  
  echo("<meta http-equiv=refresh content=0>");  
  exit;  
}  
?>  
<html>  
<head>  
<title>Challenge 6</title>  
<style type="text/css">  
body { background:black; color:white; font-size:10pt; }  
</style>  
</head>  
<body>  
<?php  
$decode_id=$_COOKIE['user'];  
$decode_pw=$_COOKIE['password'];  
  
$decode_id=str_replace("!","1",$decode_id);  
$decode_id=str_replace("@","2",$decode_id);  
$decode_id=str_replace("$","3",$decode_id);  
$decode_id=str_replace("^","4",$decode_id);  
$decode_id=str_replace("&","5",$decode_id);  
$decode_id=str_replace("*","6",$decode_id);  
$decode_id=str_replace("(","7",$decode_id);  
$decode_id=str_replace(")","8",$decode_id);  
  
$decode_pw=str_replace("!","1",$decode_pw);  
$decode_pw=str_replace("@","2",$decode_pw);  
$decode_pw=str_replace("$","3",$decode_pw);  
$decode_pw=str_replace("^","4",$decode_pw);  
$decode_pw=str_replace("&","5",$decode_pw);  
$decode_pw=str_replace("*","6",$decode_pw);  
$decode_pw=str_replace("(","7",$decode_pw);  
$decode_pw=str_replace(")","8",$decode_pw);  
  
for($i=0;$i<20;$i++){  $decode_id=base64_decode($decode_id);  $decode_pw=base64_decode($decode_pw);  
}  
  
echo("<hr><a href=./?view_source=1 style=color:yellow;>view-source</a><br><br>");  
echo("ID : $decode_id<br>PW : $decode_pw<hr>");  
  
if($decode_id=="admin" && $decode_pw=="nimda"){  solve(6);  
}  
?>  
</body>  
</html>
```

![[Pasted image 20241023100013.png]]![[Pasted image 20241023100317.png]]
```python
import base64

  

def multi_base64_encode(input_string, times=20):

    encoded = input_string.encode()

    for _ in range(times):

        encoded = base64.b64encode(encoded)

    return encoded.decode()

  

def replace_special_characters(encoded_string):

    replacements = {

        "1": "!",

        "2": "@",

        "3": "$",

        "4": "^",

        "5": "&",

        "6": "*",

        "7": "(",

        "8": ")"

    }

    for key, value in replacements.items():

        encoded_string = encoded_string.replace(key, value)

    return encoded_string

  

# 입력 받기

input_string = input()

  

# 20번 base64 인코딩하기

result = multi_base64_encode(input_string)

  

# 특수문자로 치환하기

result = replace_special_characters(result)

  

# 결과 출력

print("20번 인코딩된 결과:")

print(result)
```
- admin:nimda를 위 파이썬 코드로 인코딩 후 쿠키 값에 등록
![[Pasted image 20241023100418.png]]
- 새로고침 하면 끝