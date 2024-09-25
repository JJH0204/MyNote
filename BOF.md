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
dnf install -y gdb

gdb SBOF
```
