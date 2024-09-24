- Shell 자동화를 위해 작성하는 Script
> [!자동화가 필요한 이유]
> - 많은 보안 점검 사항, 나아가 Unix, windows 시스템에서 시행하는 반복 작업들을 자동화하여 효율을 높일 수 있다.

- Unix / Windows 모두 Shell 이라는 시스템을 탑재하고 있기 때문에 Shell Script 작성 방법에 익숙해 진다면 더 편리해 질 것이다.
- 인터프리트 언어에 속한다.
- [관련자료](https://m.blog.naver.com/hj_kim97/222586947801)

sh > 초기 unix shell
ksh > '콘쉘'이라고 읽음, sh 확장
csh > 버클리대학에서 개발한 shell
**bash** > 호환성이 뛰어난 shell
zsh 등등 다양한 종류의 shell이 있다.

``` bash
echo $(which bash) #명령어 실행 결과를 텍스트로 출력
# /usr/bin/bash
```

```bash
#!/usr/bin/bash # 셔뱅(해시뱅): 쉘 선언문을 의미한다.

mkdir /shell
touch /shell/testsc.txt
chmod 755 /shell/testsc.txt
ls -l /shell
```

## 변수(variable)
---
- 지역(로컬), 전역(글로벌), 예약, 매개 등등
- `대소문자 구분`, 변수 이름 시작을 숫자로 할 수 없다.
- `자료형`을 지정하지 않는다.
- 사용할 때 `$변수명` 형태로 사용한다.
```bash
#!/usr/bin/bash

str="Hello Global" # 전역변수

function print_str() # 함수선언
{
        local str="Hello local" # 지역변수
        echo ${str} #출력 (c > put(), /n포함)
}

print_str # 함수 호출
echo ${str} # 전역변수 출력

unset str # 메모리 초기화
```

### 환경 변수
export \[변수 이름]=\[값]
```bash
#!/usr/bin/bash

echo ${hello_world}

:wq

export hello_world="Global Export Word" # 환경변수 선언
chmod 755 ./export.sh 

./export.sh
Global Export Word
```

### 매개 변수
`./test a b c d -> $0 $1 $2 $3 $4`로 각각 대입
`$# -> 매개변수 개수`
```bash
vi ./date.sh
########################
#!/usr/bin/bash

echo "${0}: ${1}-${2}-${3}"
########################
chmod 755 ./date.sh
./date.sh 2024 9 23
./date.sh: 2024-9-23
```

### 예약 변수(키워드)
- `HOME` `PATH` `LANG` `UID` `SHELL` `USER` `TERM` 등등
- 이미 예약된 기능이 있는 변수
- 사용 불가능

### 명령어
set: 변수 출력
env: 환경 변수 출력
unset:
export: 매개변수

## 연산
---
### usr 연산자
```bash
#!/usr/bin/bash

# result=num1+num2
plus=`expr ${1} + ${2}`
minus=`expr ${1} - ${2}`
mul=`expr ${1} \* ${2}`
div=`expr ${1} / ${2}`
rem=`expr ${1} % ${2}`

echo "Plus: ${plus}"
echo "Minus: ${minus}"
echo "Mul: ${mul}"
echo "Div: ${div}"
echo "Rem: ${rem}"
```
```
./oper.sh 10 5
Plus: 15
Minus: 5
Mul: 50
Div: 2
Rem: 0
```

### let 연산자
```bash
#!/usr/bin/bash
let result=${1}+${2}
echo "Add : $result"
let result=${1}*${2}
echo "Mul : $result"
```
```bash
echo add:$((${1}+${2}))
```

## 주석
---
```bash
# 한 줄 주석

: << "END"
# 블럭 주석
code 1
code 2
code 3
END 
```

## 조건문
---
```bash
#!/usr/bin/bash

if ((${1}>0)); then
        # any code 1
        echo $((${1}*${2}))
else
        # any code 2
        echo $((${1}*-1*${2}))
fi

./if.sh 3 10 # 30
./if.sh -3 10 # 30
```

```bash
let file1=${1}
let file2=${2}

let size1=$(stat -c%s "$file1")
let size2=$(stat -c%s "$file2")

if [ -f "$file1" ] && [ -f "$file2" ]; then
        echo "file1 equal file2"
        if [[ "$size1" -gt 5 && "$size2" -lt 5 ]]; then
                echo "True"
        else
                echo "False"
        fi
else
        echo "file1 not equal file2"
        if [[ "$size1" -gt 5 || "$size2" -lt 5 ]]; then
                echo "True"
        else
                echo "False"
        fi
fi
```
`-f`: `파일`인지 검사
`-d`: `디렉토리`인지 검사
`-a`: 파일 존재 확인, 논리 AND 비교(&&)
`-gt`: 보다 큰지
`-lt`: 보다 작은지
```bash
if [ ${1} -lt ${2} ]; then
        echo "small"
elif [ ${1} -eq ${2} ]; then
        echo "equal"
else
        echo "big"
fi
```
```
./if.sh 5 4 # big
./if.sh 5 5 # equal
```
`-eq`: 같은지
```bash
case ${1} in
        "Linux") echo "Linux" ;;
        "Windows") echo "Windows" ;;
        "Mac") echo "MacOS" ;;
esac
```
```
./case.sh Mac # MacOS
```

## 반복문
---
```bash
#!/usr/bin/bash

# for
for ((i=0; i<4;i++)); do
        echo $i
done
```
```
./for.sh
0
1
2
3
```
- break, contine 사용 가능
```bash
# num="1 2 3 4 5"

for x in ${num} # 1 2 3 4 5
do
        printf "${x}"
done
# x에 1부터 5까지 순차적으로 대입하며 지정된 코드를 반복하는 방법
# 대입할 값이 없으면 반복 종료
```
```
12345
```
``` bash
num=(1 2 3 4 5)
for x in "${num[0]}"
do
        echo "${x}"
done
```
```
1
```
```bash
for y in `seq 1 5`
do
        printf $y
done
```
```
12345
```
```bash
for z in {1..9}
do
        printf $z
done
```
```
123456789
```
```bash
count=1
while [ ${count} -le 5 ];
do
        printf ${count}
        count=$(( ${count} + 1 ))
done

```
- 조건에 해당하지 않을 때 반복
```bash
until [ ${count} -le 10 ];
do
        echo ${count}
        count=$(( ${count} + 1 ))
done
```

## 배열
---
```bash
#!/usr/bin/bash

function main()
{
        # declare -a array
        array=("Linux" "Windows" "MaxOS")

        echo ${array[1]}
}

main
```
```
Windows
```
- 전체 배열 출력
```bash
echo ${array[*]} # echo ${array[@]}
```
```
Linux Windows MaxOS
```
- 배열 길이 출력
```bash
echo ${#array[*]}
```
```
3
```
- 배열의 일부만 출력
```bash
echo ${array[@]:1:3}
```
```
Windows MaxOS Unix
```
> 1차원 배열만 지원한다.

- 인덱스 값으로 요소 삭제
``` bash
function two()
{
        array=(1 2 3 4 5 6)
        remove=(3)

        array=( "${array[@]/$remove}" )
        echo ${array[@]}
}
# main
two
```
```
1 2 4 5 6
```
- 요소 삭제
```bash
unset array[3]
```
```
1 2 5 6
```
- 전체 삭제
```bash
unset array
```
```
# 깔끔
```
## 연관 배열(딕셔너리)
---
```bash
declare -A map=([hello]='world' [long]='long string')
declare -p map
echo "map[hello]=${map[hello]}"
```
```
./arrh.sh
declare -A map=([long]="long string" [hello]="world" )
map[hello]=world
```
## 함수
---
```bash
#!/usr/bin/bash

function _fun1()
{
        echo "func1"
        echo "${1}. ${2}"
}

function _main()
{
        echo "func_main()"
        _fun1 "hello" "world"
}

_main
```
```
./function.sh
func_main()
func1
hello. world
```

## 쉘 종료 코드
---

| code  | 설명                 |
| :---: | :----------------- |
|   0   | 성공                 |
|   1   | 일반적인 오류            |
|   2   | 쉘 내장 명령어 사용 오류     |
|  126  | 스크립트 실행 x          |
|  127  | 쉘에서 사용한 명령어 찾기 불가능 |
|  128  | 잘못된 인수 사용          |
| 128+n | 치명적인 n 에러          |
|  130  | ctrl+c, 종료         |

## 쉘 명령어
---
```bash
echo `date` # 시간 출력 # echo $(date)
echo "I'm in `pwd`" # echo "I'm in $(pwd)"
```
```
Mon Sep 23 04:31:15 PM KST 2024
I'm in /shell
```

## 연습: 구구단
---
```bash
#!/usr/bin/bash

function dan()
{
        for ((j=1; j<10; j++)); do
                echo "${j}"
                for ((i=1; i<10; i++)); do
                        let result=$j*$i
                        echo "$j x $i = $result"
                done
                echo "--------------"
        done
}

dan
```
```
1
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
--------------
2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
--------------
3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
--------------
4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
--------------
5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
--------------
6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
--------------
7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
--------------
8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
--------------
9
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
--------------
```
## 연습: 자동화
```bash
#!/usr/bin/bash

list=`ls *.txt`

`chmod ${1} ${list}`

echo "Success"
```
```
./Auto.sh 755 # Success
ls -al *.txt
##############
-rwxr-xr-x. 1 root root 0 Sep 23 17:01 test1.txt
-rwxr-xr-x. 1 root root 0 Sep 23 17:01 test2.txt
-rwxr-xr-x. 1 root root 0 Sep 23 17:01 test3.txt
-rwxr-xr-x. 1 root root 0 Sep 23 12:13 testsc.txt
##############
```

## 과제
- /var/log log 파일 중 2일 이상 지난 파일들은 압축 보관
- 3이상 지난 파일들은 삭제
- [find -time](https://inpa.tistory.com/entry/LINUX-%F0%9F%93%9A-find-%EB%AA%85%EB%A0%B9-mtime-ctime-atime-%EC%98%B5%EC%85%98-n-n-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)
- find /var/log -mtime +1 -name *.log
  .log로 끝나는 파일들 중 3일 이상 방치된 파일
```bash
#!/usr/bin/bash

dir=/var/log

rmLog=`find ${dir} -mtime +1 -name *.log`

`rm -rf ${rmLog}`

zipLog=`find ${dir} -mtime 1 -name *.log` # 여긴가?

`gzip -v ${ziplog}` # 여긴가?
```
```bash
# 3일 이상 방치된 .log 파일 삭제
find /var/log -type f -name "*.log" -mtime +1 -exec rm -f {} \; 
# 2일 이상 방치된 .log 파일 압축 
find /var/log -type f -name "*.log" -mtime 1 -exec gzip {} \;
```
- `-type f`: 타입이 파일인 것을 찾는다.
- `-name "*.log"`: 파일 이름이 ".log"로 끝나는 것을 찾는다.
- `-mtime +n`: 파일의 마지막 수정 날짜가 n이상인 파일을 찾는다.
- `-exec`: 찾은 파일들을 대상으로 수행할 작업을 지정한다.
[[find_time]]
## [[서버 점검 스크립트]]
---
