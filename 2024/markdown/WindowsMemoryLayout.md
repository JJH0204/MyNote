# 섹션
---
윈도우의 PE 파일은 PE 헤더와 1개 이상의 섹션으로 구성되어 있다.

> [!섹션이란]
> 유사한 용도로 사용되는 데이터가 모여있는 영역
> 예) ".text"섹션에는 PE의 코드가 적혀있고, ".data"에는 PE가 실행중에 참조하는 데이터가 적혀있다.

섹션에 대한 정보는 PE 헤더에 적혀있다.
PE 헤더에 저장되는 섹션과 관련된 데이터 중, 중요한 것은 아래와 같다.
- 섹션의 이름
- 섹션의 크기
- 섹션이 로드 될 주소의 오프셋
- 섹션의 속성과 권한
이 정보를 참조하여 윈도우에서 PE를 실행할 때 각 섹션들을 가상 메모리의 적절한 [세그먼트](MemorySegment.md)에 매핑 한다.
PE에 필수로 존재해야 하는 섹션이 정해진 것은 아니다.
일반적으로 ".text", ".data", ".rdata" 섹션이 사용된다.

## .text
---
실행 가능한 기계 코드가 위치하는 영역

프로그램이 동작하려면 코드를 실행할 수 있어야 한다.
이 [세그먼트](MemorySegment.md)에는 읽기 권한과 실행 권한이 부여된다.

쓰기 권한은 공격자가 악의적인 코드를 삽입하기 쉬워짐으로,
대부분의 현대 운영체제는 쓰기 권한을 제거한다.

아래 정수 31337을 반환하는 main 함수가 컴파일 되면 554889e5b8697a00005dc3 라는 기계 코드로 변환
이 기계 코드가 코드 [세그먼트](MemorySegment.md)에 위치하게 된다.

```c
int main() { return 31337; }
```

## .data
---
컴파일 시점에 값이 정해진 전역 변수들이 위치한다.
CPU가 이 섹션의 데이터를 읽고 쓸 수 있어야 함으로, 읽기/쓰기 권한이 부여된다.

아래는 .data 섹션에 포함되는 여러 데이터의 유형이다.

```c
int data_num = 31337;
char data_rwstr[] = "writable_data";        // data

int main() { ... }
```

## .rdata
---
컴파일 시점에 값이 정해진 전역 상수와 참조할 [[DLL]] 및 외부 함수들의 정보가 저장된다.
CPU가 이 섹션의 데이터를 읽을 수 있어야 함으로, 읽기 권한이 부여되지만, 쓰기는 불가능하다.

아래는 .rdata 섹션에 포함되는 여러 데이터의 유형이다.
str_ptr 변수를 주의 깊게 관찰하면 아래와 같다.
- str_ptr은 "readonly"라는 문자열을 가리키고 있다.
- str_ptr은 전역 변수로서 .data에 위치 
- but. "readonly"는 상수 문자열로 취급되어 .rdata에 위치

```c
const char data_rostr[] = "readonly_data";
char *str_ptr = "readonly";  // str_ptr은 .data, 문자열은 .rdata

int main() { ... }
```

과거 참조할 [[DLL]]과 외부 함수들의 정보를 .idata 섹션에 저장했으나, 최근 대부분 .rdata에 저장한다.

# 섹션이 아닌 메모리
---
윈도우의 가상 메모리 공간에는 섹션 외에도 프로그램 실행에 있어 필요한 스택과 힙 역시 가상 메모리 공간에 적재된다.

## 스택
windows 프로세스의 각 쓰레드는 자신만의 스택 공간을 가지고 있다.
보통 지역 변수나 함수의 리턴 주소가 저장된다.
자유롭게 읽고 쓸수 있어야 하기 때문에 읽기/쓰기 권한이 부여된다.
스택이 확장될 때 기존 주소보다 낮은 주소로 확장되기에 '아래로 자란다'는 표현을 사용한다.

아래 코드에서는 지역변수 choice가 스택에 저장된다.
```c
void func() {
  int choice = 0;
  
  scanf("%d", &choice);
  
  if (choice)
    call_true();
  else
    call_false();
    
  return 0;
}
```

## 힙
프로그램이 여러 용도로 사용하기 위해 할당받은 공간
모든 종류의 데이터가 저장될 수 있다.
스택보다 비교적 큰 데이터도 저장할 수 있고, 전역으로 접근이 가능하도록 설계되어 있다.
스택과 달리 프로그램 실행 중 동적으로 할당 받는 점이 큰 특징이다.

읽기/쓰기 권한 외 상황에 따라 실행 권한을 가질 수도 있다.

아래 코드는 malloc()을 통해 동적으로 할당한 영역의 주소를 대입하고 값을 쓴다.
heap_data_ptr은 지역변수 > 스택에 위치
malloc으로 할당 받은 힙 세그먼트의 주소를 가리킨다.
```c
int main() {
  int *heap_data_ptr =
      malloc(sizeof(*heap_data_ptr));  // 동적 할당한 힙 영역의 주소를 가리킴
  *heap_data_ptr = 31337;              // 힙 영역에 값을 씀
  printf("%d\n", *heap_data_ptr);  // 힙 영역의 값을 사용함
  return 0;
}
```