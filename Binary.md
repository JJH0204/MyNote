## 키워드
---
- 기계어(Machine Language)
- 어셈블리어(Assembly Language)
- 어셈블러(Assembler)
- 컴파일러(Compiler)
- 고급 언어(High-Level Language)
- 저급 언어(Low-Level Language)

# 프로그램과 컴파일

## 프로그램(Program)
---
- 연산 장치가 수행해야 할 동작을 정의한 일종의 문서
- 사용자가 정의한 프로그램을 해석하여 명령어를 처리할 수 있는 연산 장치를 programmable
	  그렇지 않은 연산 장치를 non-programmable라고 한다.
- 과거에 내부 저장 장치가 없어 직접 전선을 연결하거나 천공 카드(punched card)에 기록해 사용하는 방법을 사용했다.
- 기존의 컴퓨터의 단점을 개선한 Stored-Program Computer가 상용화되고 프로그램이 저장 장치에 이진(Binary) 형태로 저장되었다.
- 이후 프로그램을 바이너리(Binary)라고 부르기도 한다.

## 컴파일러와 인터프리터
---
- **프로그래밍 언어(Programming Language)**: 프로그램을 개발하기 위해 사용하는 언어
- **소스 코드(Source Code)**: CPU가 수행해야 할 명령들을 프로그래밍 언어로 작성한 것
- **컴파일(Compile)**: 소스 코드를 기계어 형식으로 번역하는 행위
- **컴파일러(Compiler)**: 컴파일을 하는 소프트웨어 (GCC, Clang, MSVC 등)

- Python, Javascript 등 언어는 컴파일을 필요로 하지 않는다.
	- 사용자의 입력, 작성한 스크립트를 그때 그때 번역하는 **인터프리팅(Interpreting)** 방식으로 실행
	- 인터프리팅을 수행하는 소프트웨어를 **인터프리터(Interpreter)** 라고 한다.

## 컴파일 과정
---
- [[C 언어]]로 작성된 코드는 일반적으로 전처리(Preprocess) > 컴파일(Compile) > 어셈블(Assemble) > 링크(Link)의 과정을 거쳐 바이너리로 번역된다.
- 예제 코드
```c
// Name: add.c

#include "add.h"

#define HI 3

int add(int a, int b) { return a + b + HI; }  // return a+b

```
```c
// Name: add.h

int add(int a, int b);

```
> [!컴파일 과정 속 컴파일]
> 컴파일의 정확한 의미는 어떤 언어로 작성된 소스 코드를 다른 언어의 목적 코드(Object Code)로 번역하는 것이다.
> 이 맥락에서, 소스 코드를 어셈블리어로, 또는 소스코드를 기계어로 번역하는 것 모두 컴파일이라 볼 수 있다.

### 전처리 (Preprocessing)
---
> 컴파일러가 소스 코드를 어셈블리어로 컴파일하기 전에, 필요한 형식으로 가공하는 과정
> (언어마다 조금 다름)

**1.주석 제거**
**2.매크로 치환**
- `#define`으로 정의한 매크로를 정의된 코드 또는 값으로 치환한다.
**3.파일 병합**
- 여러 개의 소스 코드와 헤더 파일을 따로 컴파일해 합치기도, 합치고 컴파일 하기도 한다.

gcc에서는 -E 옵션을 사용하여 소스 코드의 전처리 결과를 확인할 수 있다.
```sh
$ gcc -E add.c > add.i
$ cat add.i
```
add.c를 add.i로 전처리한 결과
```
# 1 "add.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 31 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 32 "<command-line>" 2
# 1 "add.c"
# 1 "add.h" 1
int add(int a, int b);
# 2 "add.c" 2



int add(int a, int b) { return a + b + 3; }
```
- 주석이 사라지고 매크로가 값으로 치환되었다.
- add.h의 내용이 `#include`에 의해 병합되었다.

### 컴파일 (Compile)
---
