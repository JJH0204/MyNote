# Stack Buffer Overflow
- buffer: 데이터 입출력을 위해 사용되는 임시 저장소, 시스템 마다 크기는 다름
- 악의 적으로 shell 코드를 삽입 > buffer를 초과하는 데이터를 입력 > 다른 메모리를 침범(Over ride)하며 shell code를 실행하도록 만듬(악성 코드)
- stack overflow, heap overflow 
## 메모리 형태
---
https://st-lab.tistory.com/198
- kernel memory: 운영체제
- stack memory: 지역, 매개 변수 / 함수
- 라이브러리 memory: 
- heap memory: 동적 변수
- bata memory: 전역, 정적 변수
- code memory: 기계어/어셈블리어

## Stack Buffer Overflow
---
### \[원리]
- 지정된 버퍼 사이즈를 넘기는 큰 크기의 데이터를 강제로 입력하여 다른 메모리 영역 침범하는 공격 방식
- RET/EBP/Buffer[8] > 임의의코드/tttt/aaaaaaaaaaaaaa
- RET(리턴 함수 주소) 대신 임의의 코드를 실행하게 되어 악영향을 주게됨
### \[원인]
- 문자열 처리함수에서 입력값에 대한 길이 체크를 하지 않아 발생하는 취약점
	- strcpy strcat gets fscanf scanf sprintf sscanf vfscanf vsprintf vscanf vsscanf streadd strecpy strtrns / 취약한 함수 들
### \[방안]
- 안전한 함수를 사용
- 값을 입력 받을 때 길이를 검사
- **ASLR**(Address Space Layout Randomization)
  : 메모리를 참조할 때마다 랜덤으로 주소를 할당해 BOF 공격을 힘들게 한다.
- **Stack Guard**
  : **Canary**
  : 메모리에 위/변조가 발생했는지 함께 식별할 수 있는 값을 저장해 확인하는 방법
- **NX**(Node eXecute) bit
  : 스텍/힙에서 스크립트(또는 명령어, 함수)를 실행하는 권한을 비활성화 하는 방법
  : 우회 공격 기법 
	  -> RTL(Return To Library)/ROP(Return Oriented Programming)

### \[검사]
#### NX
```bash
dmesg | grep NX
[    0.000000] NX (Execute Disable) protection: active
[    0.262920] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
[    0.263003] input: Sleep Button as /devices/LNXSYSTM:00/LNXSLPBN:00/input/input1
[    1.447050] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/LNXVID/input5
```
- NX 동작 여부 확인

#### ASLR
```bash
cat /proc/sys/kernel/randomize_va_space
2
```
- ASLR 실행 여부 확인
	- 0(비활성화)
	- 1(stack 만)
	- 2(stack, heap 모두 검사)

### \[실습]
#### 취약한 c 예제 코드
```c
# SBOF.c
# include <stdio.h>
int main(int argc, char* argv[])
{
    char cBuf[0x100] = {0, };   # 버퍼 역할을 할 배열 할당(인덱스 값 8)
    printf("Input: ");
    gets(cBuf);                  # BOF Attack에 취약한 함수 사용

    return 0;
}
```

#### 빌드 명령어
```
gcc -o SBOF SBOF.c -z execstack -z morelro -fno-stack-protector -no-pie
```
- execstack: 스택에서 쉘 실행 권한 제공
- morelro: 방해 받지 않도록 설정
- -fno-stack-protector: stack 보호 기능 해제

#### 스택 보호 기능 비활성화
```
 echo 0 > /proc/sys/kernel/randomize_va_space
```

#### 실행 결과 확인
```
./SBOF
Input: 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
Segmentation fault (core dumped)
```

#### 디버깅 도구를 활용
- [[gdb]]
```
## 설치
dnf install -y gdb

## 디버깅 실행
gdb SBOF
############################
GNU gdb (GDB) Rocky Linux 10.2-13.el9
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from sbop...
(No debugging symbols found in sbop)
##############################
(gdb)
```
```
## 함수 디버깅
disas main # disas 함수이름
Dump of assembler code for function main:
   0x0000000000401136 <+0>:     push   %rbp
   0x0000000000401137 <+1>:     mov    %rsp,%rbp
   0x000000000040113a <+4>:     sub    $0x110,%rsp
   0x0000000000401141 <+11>:    mov    %edi,-0x104(%rbp)
   0x0000000000401147 <+17>:    mov    %rsi,-0x110(%rbp)
   0x000000000040114e <+24>:    movq   $0x0,-0x100(%rbp)
   0x0000000000401159 <+35>:    movq   $0x0,-0xf8(%rbp)
   0x0000000000401164 <+46>:    movq   $0x0,-0xf0(%rbp)
   0x000000000040116f <+57>:    movq   $0x0,-0xe8(%rbp)
   0x000000000040117a <+68>:    movq   $0x0,-0xe0(%rbp)
   0x0000000000401185 <+79>:    movq   $0x0,-0xd8(%rbp)
   0x0000000000401190 <+90>:    movq   $0x0,-0xd0(%rbp)
   0x000000000040119b <+101>:   movq   $0x0,-0xc8(%rbp)
   0x00000000004011a6 <+112>:   movq   $0x0,-0xc0(%rbp)
   0x00000000004011b1 <+123>:   movq   $0x0,-0xb8(%rbp)
   0x00000000004011bc <+134>:   movq   $0x0,-0xb0(%rbp)
   0x00000000004011c7 <+145>:   movq   $0x0,-0xa8(%rbp)
   0x00000000004011d2 <+156>:   movq   $0x0,-0xa0(%rbp)
   0x00000000004011dd <+167>:   movq   $0x0,-0x98(%rbp)
   0x00000000004011e8 <+178>:   movq   $0x0,-0x90(%rbp)
   0x00000000004011f3 <+189>:   movq   $0x0,-0x88(%rbp)
   0x00000000004011fe <+200>:   movq   $0x0,-0x80(%rbp)
   0x0000000000401206 <+208>:   movq   $0x0,-0x78(%rbp)
   0x000000000040120e <+216>:   movq   $0x0,-0x70(%rbp)
   0x0000000000401216 <+224>:   movq   $0x0,-0x68(%rbp)
   0x000000000040121e <+232>:   movq   $0x0,-0x60(%rbp)
   0x0000000000401226 <+240>:   movq   $0x0,-0x58(%rbp)
   0x000000000040122e <+248>:   movq   $0x0,-0x50(%rbp)
   0x0000000000401236 <+256>:   movq   $0x0,-0x48(%rbp)
   0x000000000040123e <+264>:   movq   $0x0,-0x40(%rbp)
   0x0000000000401246 <+272>:   movq   $0x0,-0x38(%rbp)
   0x000000000040124e <+280>:   movq   $0x0,-0x30(%rbp)
   0x0000000000401256 <+288>:   movq   $0x0,-0x28(%rbp)
   0x000000000040125e <+296>:   movq   $0x0,-0x20(%rbp)
   0x0000000000401266 <+304>:   movq   $0x0,-0x18(%rbp)
   0x000000000040126e <+312>:   movq   $0x0,-0x10(%rbp)
   0x0000000000401276 <+320>:   movq   $0x0,-0x8(%rbp)
   0x000000000040127e <+328>:   mov    $0x402010,%edi
   0x0000000000401283 <+333>:   mov    $0x0,%eax
   0x0000000000401288 <+338>:   call   0x401030 <printf@plt> # 함수를 호출하는 명령어를 저장한 메모리 주소
   0x000000000040128d <+343>:   lea    -0x100(%rbp),%rax # 함수 존재
   0x0000000000401294 <+350>:   mov    %rax,%rdi
   0x0000000000401297 <+353>:   mov    $0x0,%eax
   0x000000000040129c <+358>:   call   0x401040 <gets@plt> # 함수 호출 명령어
   0x00000000004012a1 <+363>:   mov    $0x0,%eax
   0x00000000004012a6 <+368>:   leave
   0x00000000004012a7 <+369>:   ret
End of assembler dump.

```
- 어셈블리 언어를 알아야 해석할 수 있다.
- 메모리 주소를 호출해서 디버깅 가능
```
(gdb) x/s 0x401288 # call 메모리
0x401288 <main+338>:    "\350\243\375\377\377H\215\205"
```