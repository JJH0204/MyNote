# 컴파일 (Compile)
---
- C 로 작성된 소스 코드를 어셈블리어로 번역
- 이 과정에서 컴파일러는 소스 코드의 문법을 검사
- 문법적 오류가 있다면 컴파일을 멈추고 에러를 출력
- 몇몇 조검을 만족하면 최적화 기술을 적용해 효율적인 어셈블리 코드를 생성한다.
	  gcc 에서는 `-O -O0 -O1 -O2 -O3 -Os -Ofast -Og` 등의 옵션을 사용하여 최적화를 적용 할 수 있다.
- 컴파일 예시
```
// Name: opt.c
// Compile: gcc -o opt opt.c -O2

#include <stdio.h>

int main() {
  int x = 0;
  for (int i = 0; i < 100; i++) x += i; // x에 0부터 99까지의 값 더하기
  printf("%d", x);
}
```