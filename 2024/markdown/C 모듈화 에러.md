---
sticker: lucide//text-selection
---
#개발 #개발환경
VScode 로 스택을 구현한 후 모듈화를 위해 파일을 나눠서 저장했다.
- [[MyStack.h]]
- [[MyStack.c]]
- [[Main.c]]

VS Code 에서는 다음과 같은 에러가 발생했다.

```
admin@adminui-MacBookAir 6_usingStack % cd "/Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/" && gcc reverseString.c -o reverseString &&
 "/Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/"reverseString
ld: Undefined symbols:
  _createStack, referenced from:
      _reverseString in reverseString-42ca62.o
  _pop, referenced from:
      _reverseString in reverseString-42ca62.o
  _push, referenced from:
      _reverseString in reverseString-42ca62.o
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

반면 Xcode 에서 컴파일 시 정상적으로 작동했다.

```
current stack: 7 number

[7]-[U]

[6]-[O]

[5]-[Y]

[4]-[E]

[3]-[V]

[2]-[O]

[1]-[L]

Pop - [U]

current stack: 6 number

[6]-[O]

[5]-[Y]

[4]-[E]

[3]-[V]

[2]-[O]

[1]-[L]

Peek - [O]

current stack: 6 number

[6]-[O]

[5]-[Y]

[4]-[E]

[3]-[V]

[2]-[O]

[1]-[L]

Program ended with exit code: 0
```

무엇이 이 둘의 차이를 만들었을까?

### 1. 작성 IDE 차이?
> 만약에, 코드를 작성했던 IDE의 파일 생성 방식의 차이 때문이라면 Xcode에서 정상 작동했던 코드를 VSCode에서 프로젝트 파일 통째로 불러와서 실행하면 실행되지 않을까?  

#### <결과>

```
cd "/Users/admin/Documents/C_test/C_test/" && gcc main.c -o main && "/Users/admin/Documents/C_test/C_test/"main
admin@adminui-MacBookAir C_test % cd "/Users/admin/Documents/C_test/C_test/" && gcc main.c -o main && "/Users/admin/Documents/C_test/C_test/"main
ld: Undefined symbols:
  _createStack, referenced from:
      _main in main-c2b05d.o
  _deleteStack, referenced from:
      _main in main-c2b05d.o
  _displayStack, referenced from:
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      _main in main-c2b05d.o
  _peek, referenced from:
      _main in main-c2b05d.o
  _pop, referenced from:
      _main in main-c2b05d.o
  _push, referenced from:
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      _main in main-c2b05d.o
      ...
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```
> 덕분에 VSCode 자체의 문제인 점은 확인했다.
> 문제 해결을 위해 VSCode의 세팅 부분을 확인해야 겠다.

### 2. [clang](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9E%AD): 의 의미
> c, c++ 등 c 관련 프로그래밍 언어를 위한 [컴파일러](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC "컴파일러") [프론트엔드](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C "프론트엔드")이다.
> 목표는 [GNU 컴파일러 모음](https://ko.wikipedia.org/wiki/GNU_%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC_%EB%AA%A8%EC%9D%8C "GNU 컴파일러 모음") (GCC)를 대체하는 것이다.
> [LLVM](https://ko.wikipedia.org/wiki/LLVM "LLVM")을 백엔드로 사용하며 [LLVM](https://ko.wikipedia.org/wiki/LLVM "LLVM") 2.6 이후로 릴리즈의 일부로 자리잡았다.

#### **[GCC와 Clang의 차이점](https://growingdev.blog/entry/%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-LLVM%EA%B3%BC-Clang%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C)**
> 위 설명을 참고해 문제점을 점검해 본다면 Clang의 불안정성 때문에 오류가 발생했을 수도 있다고 본다.
> 오류가 잦은 Clang 보다 GCC를 컴파일러로 사용할 수 있도록 환경 변수를 변경해야 할 것 같다.

1. gcc 설치 여부 확인
```
gcc -v
```

```
Apple clang version 15.0.0 (clang-1500.0.40.1)

Target: arm64-apple-darwin23.4.0

Thread model: posix

InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```
Apple clang version ~ 이라고 출력되는데 이러면 GCC가 설치가 안된 걸까?
설치 경로로 들어가보자
![clang 설치 경로](obsidian://open?vault=MyNote&file=%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-03-16%2015.12.46.png)
GCC가 설치된적 없는 것 같다.
그런데 블로그에 어떤 글에서는 다른 경로에 GCC가 이미 설치되어 있을 수도 있다고 한다.

```
라이브러리/Developer/CommandLineTools/usr/bin/
```
위 경로에 이미 GCC 가 설치되어 있었으며 동시에 clang 또한 있는 것을 확인했다.
환경 변수를 변경하기만하면 될 것 같은데...
windows 와 환경이 달라 조금 복잡해 보인다.
집중해서 바꿔보자.

[[Mac OS 환경변수 설정방법

[[XCode 삭제방법]]

2. XCode.app 삭제 후 버전(설치여부) 확인

```
gcc -v

Apple clang version 15.0.0 (clang-1500.3.9.4)

Target: arm64-apple-darwin23.4.0

Thread model: posix

InstalledDir: /Library/Developer/CommandLineTools/usr/bin
```
이전에 확인했던 설치 경로로 설정이 바꼈다.
만약 위 경로에 파일이 없다면 XCode를 다시 설치해야 함[XCode 설치](https://somjang.tistory.com/entry/GCC-macOS-%EC%97%90-gcc-%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC-%EC%84%A4%EC%B9%98%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

vscode 에서 GCC 로 빌드하면 또 에러가 발생함

```
 *  작업 실행 중: C/C++: gcc 활성 파일 빌드 

빌드를 시작하는 중...
/usr/bin/gcc -fdiagnostics-color=always -g /Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/reverseString.c -o /Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/reverseString
Undefined symbols for architecture arm64:
  "_createStack", referenced from:
      _reverseString in reverseString-fede55.o
  "_pop", referenced from:
      _reverseString in reverseString-fede55.o
  "_push", referenced from:
      _reverseString in reverseString-fede55.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

빌드가 완료되었지만, 오류가 발생했습니다.

 *  터미널 프로세스를 시작하지 못했습니다(종료 코드: -1). 
 *  터미널이 작업에서 다시 사용됩니다. 닫으려면 아무 키나 누르세요. 
```

에러와 동시에 두 알림이 등장했다.
*tasks.json 파일에서 컴파일 패치 경로 바꾸는 것과 
CMake 에 대한 알람
> 항상 프로젝트를 열 때 구성하시겠습니까?
> 소스: CMake Tools(확장)*

무슨 의미인지 모르지만 확인을 누르니 두 json 파일이 열렸다.
[[tasks.json]]
[[launch.json]]
그리고 자료를 좀 더 조사해보니 [[c_cpp_properties.json]]과 함께 c 개발환경 세팅에 필요한 파일이었다.
> 한번도 저 3 파일을 세팅한 경험이 없으니 이것 때문에 에러가 발생했을 수도 있다 생각이 든다.

# 중간 정리
> VSCode를 처음 설정할 때 좀 더 상세하게 설정했다면 이런 고생하지 않았을 텐데 라는 생각을 했지만 이미 지난 일이고 지금이라도 설정 방법을 공부할 수 있어서 다행이라 생각한다.
> 그리고, 초기 설정 차이로 헤더 파일 링크가 작동하고 안하고가 결정될 줄 몰랐기에 앞으로 세팅할때 좀 더 꼼꼼하게 설정을 할 것 같다.
> 일단 지금은 VSCode 의 설정 방법을 다시 공부해야겠다.


## C/C++ 컴파일러 초기값
[Mac Clang C++17 컴파일러 환경 설정](https://headf1rst.github.io/c++/clang-c++17/)
[[vscode for mac]]
[[settings.json]]
[windows c/c++ 개발환경 설정](https://blog.amylo.diskstation.me/algorithm/Starting_Algorithm_with_VSCode_C++/)
### [[DLL]]??

### [[CMake]]?

<details>
<summary>터미널을 이용해 강제로 컴파일러에 파일들을 전달하는 방식을 사용</summary>
```
PS E:\Document\DevBasics> cd "DSNA"
PS E:\Document\DevBasics\DSNA> cd "6_usingStack"
PS E:\Document\DevBasics\DSNA\6_usingStack> gcc reverseString.c Stack.c Stack.h -o reverseString
PS E:\Document\DevBasics\DSNA\6_usingStack> reverseString
reverseString : 'reverseString' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경로가 포
함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1
+ reverseString
+ ~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (reverseString:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: reverseString 명령이 현재 위치에 있지만 이 명령을 찾을 수 없습니다. Windows PowerShell은 기본적으로 현재 위치에서 명령을 로드하지 않습니다. 이 명령을 신뢰하는 경우 대신 ".\reverseString"을(를) 입력하십시오. 자세한 내용은 "get-help about_Command_Precedence"를 참조하십시오.
PS E:\Document\DevBasics\DSNA\6_usingStack> reverseString.exe
reverseString.exe : 'reverseString.exe' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정확한지 확인하고 경 
로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1
+ reverseString.exe
+ ~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (reverseString.exe:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: reverseString.exe 명령이 현재 위치에 있지만 이 명령을 찾을 수 없습니다. Windows PowerShell은 기본적으로 현재 위치에서 명령을 로드하지 않습니다. 이 명령을 신뢰하는 경우 대신 ".\reverseString.exe"을(를) 입력하십시오. 자세한 내용은 "get-help about_Command_Precedence"를 참조하십시오.
PS E:\Document\DevBasics\DSNA\6_usingStack> .\reverseString
PS E:\Document\DevBasics\DSNA\6_usingStack> 
```
</details>

> 강제로 컴파일 링크 값 전달

강제로 링크 값 전달하여 빌드한 생성파일을 터미널에서 실행

```
/Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/reverseString ; exit;

admin@adminui-MacBookAir ~ % /Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/reverseString ; exit;

zsh: segmentation fault  /Users/admin/Documents/GitHub/DevBasics/DSNA/6_usingStack/reverseString

  

Saving session...

...copying shared history...

...saving history...truncating history files...

...completed.

  

[프로세스 완료됨]
```
실행 됐다. 허나 또 다른 에러가 발생했을 뿐... (무한루프...)

# 결론
1. VSCode 는 자체적으로 링크를 관리하는 기능이 없다.
2. gcc 등 컴파일 명령어를 이용해 링크에 포함할 파일을 한번에 묶어서 컴파일 할 수 있다.
3. [[CMake]] 을 이용해 위 작업을 관리할 수 있고 파일 단위 소스코드 관리가 가능하다.