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