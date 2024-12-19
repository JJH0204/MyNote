![[Pasted image 20241007123017.png]]
![[Pasted image 20241007123142.png]]a = aad 
i = in

![[Pasted image 20241007124552.png]]
```
	function chk_form(){
		var id = document.web02.id.value ;
		var pw = document.web02.pw.value ;
		if ( id == pw )
		{
			alert("You can't join! Try again");
			document.web02.id.focus();
			document.web02.id.value = "";
			document.web02.pw.value = "";
		}
		else
		{
			document.web02.submit();
		}
	}
```
![[Pasted image 20241007124955.png]]
유저가 입력할 때는 아이디와 패스워드가 같으면 안되는데 결과를 계산할 때는 같아야 한다.
프록시 툴을 이용해 입력은 다르게 결과는 같게 바꾸면 해결된다.
![[Pasted image 20241007140902.png]]

![[Pasted image 20241007142533.png]]
## 4
![[Pasted image 20241007142852.png]]
![[Pasted image 20241007142838.png]]
![[Pasted image 20241007143315.png]]
리피터를 사용해 반복작업을 자동화
![[Pasted image 20241007143450.png]]


## 5
![[Pasted image 20241007144315.png]]
```
eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('g l=m o(\'0\',\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'a\',\'b\',\'c\',\'d\',\'e\',\'f\');p q(n){g h=\'\';g j=r;s(g i=t;i>0;){i-=4;g k=(n>>i)&u;v(!j||k!=0){j=w;h+=l[k]}}x(h==\'\'?\'0\':h)}',34,34,'||||||||||||||||var|result||start|digit|digitArray|new||Array|function|PASS|true|for|32|0xf|if|false|return'.split('|'),0,{}))
```
eval: 자바스크립트 난독화 함수
```
var digitArray=new Array('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f');
function PASS(n)
	{
	var result='';
	var start=true;
	for(var i=32;
	i>0;
	)
		{
		i-=4;
		var digit=(n>>i)&0xf;
		if(!start||digit!=0)
			{
			start=false;
			result+=digitArray[digit]
		}
	}
	return(result==''?'0':result)
}
```
![[Pasted image 20241007145311.png]]
![[Pasted image 20241007145300.png]]

## 6
![[Pasted image 20241007150505.png]]
![[Pasted image 20241007150543.png]]
SQL Injection - 쿼리에 대해 참인 결과 값을 이용해 DB의 응답을 유발하는 공격
': 문자 데이터 구분 기호
;: 쿼리 구분 기호
--, #: 해당 라인 주석 기호
/* */: /*와 */사이 구문 주석 기호

'or 1=1 --
'or 1 like 1 --
'or 1=1 #
'or 2>1 --

![[Pasted image 20241007151153.png]]
- DB에서 잘못된 쿼리에도 반응하는 것을 알 수 있다.

![[Pasted image 20241007151242.png]]
' or 1 like 1
![[Pasted image 20241007151326.png]]
![[Pasted image 20241007151406.png]]
suninatastopofworld!

![[Pasted image 20241007151652.png]]

hash를 md5로 설정하고 해싱
![[Pasted image 20241007152936.png]]
![[Pasted image 20241007153134.png]]
이후 페이지 소스를 보면 다른 힌트를 얻을 수 있다.
![[Pasted image 20241007153535.png]]
![[Pasted image 20241007153657.png]]

## 7
스크롤을 빨리 내려서 yes 를 눌러야 하는 워게임
![[Pasted image 20241007154212.png]]
![[Pasted image 20241007154337.png]]
```

        function noEvent() {
            if (event.keyCode == 116 || event.keyCode == 9) {
                alert('No!');
                return false;
            }
            else if (event.ctrlKey && (event.keyCode = 78 || event.keyCode == 82)) {
                return false;
            }
        }
        document.onkeydown = noEvent;
    
```

9 = tab
116 = f5
78 = n
82 = r

![[Pasted image 20241007154658.png]]
![[Pasted image 20241007154911.png]]
frm의 submit() 을 실행하면 직접 클릭을 하지 않아도 버튼을 누를 수 있다.
![[Pasted image 20241007155422.png]]
![[Pasted image 20241007155759.png]]

## 8
![[Pasted image 20241007160404.png]]![[Pasted image 20241007160418.png]]![[Pasted image 20241007160613.png]]
인트루트 기능을 사용하면 규칙적으로 변경되는 값을 자동으로 넣을 수 있다.
![[Pasted image 20241007160810.png]]페이로드 설정하고 규칙을 설정![[Pasted image 20241007160734.png]]![[Pasted image 20241007160949.png]]
start attack 누르면 동작![[Pasted image 20241007161152.png]]