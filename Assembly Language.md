- https://velog.io/@hey-chocopie/Libasm-2.-%EC%96%B4%EC%85%88%EB%B8%94%EB%A6%AC%EC%96%B4%EB%9E%80-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8A%B9%EC%A7%95-%EC%A0%95%EB%A6%AC-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC
- https://velog.io/@msung99/%EC%8B%9C%EC%8A%A4%ED%85%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-4-1%EC%A3%BC%EC%B0%A8

# 어셈블리어
- 기계어(0,1)에 가까운 언어(임베디드 시스템, 커널 프로그래밍 등에 사용)
- `intel` / AT&T 문법으로 나뉜다.(1234 / %1%2%3%4)
- Opcode Operand1 Operand2로 구성된다.
	ADD EAX(Des) EBX(Src) <- 레지스터의 종류
	명령어 목적지  출발지
	Add 1        2 -> 2 + 1
	SUB 1        2 -> 2 - 1

## Register
---
- CPU의 명령을 받아 임시로 공간을 저장하는 장치
- `범용` / `인덱스` / `포인터` 로 구분
### 범용 레지스터
- EAX, EBX (Accumulator), (Base)
  : 사칙 연산에 자동으로 할당되는 레지스터
  : 또는, 지정된 변수 값을 저장할 때 사용
- ECX (Counter)
  : 반복 레지스터
- EDX (Data)
  : 보조 레지스터

### 인덱스 레지스터
- ESI(Source), EDI(Destination)
  : 데이터의 복사 / 이동 / 비교 사용되는 레지스터
  : 원본과 대상이 된다.

### 포인터 레지스터
- EIP(Instruction)
  : 다음에 실행할 명령어를 가지는 레지스터
- ESP(Stack)
  : 가장 최근에 저장된 메모리의 주소를 가지는 레지스터
- EBP(Base)
  : 가장 마지막 바닥 메모리의 주소를 가지는 레지스터

## Assembly
---
![[Pasted image 20240925110748.png]]
```c
#include <stdio.h>

int main(int argc, char* argv[])
{
    int a = 1;
    int b = 2;
    int c = a + b;

    printf("a: %d, b: %d, c: %d\n", a, b, c);

    return 0;
}
```
```bash
[root@Linux1 tmp]# vi ./addtest.c
[root@Linux1 tmp]# gcc -o addtest addtest.c
[root@Linux1 tmp]# ./addtest
a: 1, b: 2, c: 3
```
### 어셈블리어 예제
```assembly
push        ebp  
mov         ebp,esp  
sub         esp,0E4h  
push        ebx  
push        esi  
push        edi  
lea         edi,[ebp+FFFFFF1Ch]  
mov         ecx,39h  
mov         eax,0CCCCCCCCh  
rep stos    dword ptr es:[edi]  
mov         ecx,9AC003h  
call        009A1316  
mov         dword ptr [ebp-8],1  
mov         dword ptr [ebp-14h],2  
mov         eax,dword ptr [ebp-8]  
add         eax,dword ptr [ebp-14h]  
mov         dword ptr [ebp-20h],eax  
mov         eax,dword ptr [ebp-20h]  
push        eax  
push        9A7D08h  
call        009A10CD  
add         esp,8  
xor         eax,eax  
pop         edi  
pop         esi  
pop         ebx  
add         esp,0E4h  
cmp         ebp,esp  
call        009A123F  
mov         esp,ebp  
pop         ebp  
ret
```