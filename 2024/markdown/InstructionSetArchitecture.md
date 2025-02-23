> [!명령어 집합 구조란?]
> - CPU가 해석하는 명령어의 집합을 의미한다.
> - 프로그램의 코드는 기계어로 작성되어 있는데
>   프로그램을 실행하면 이 명령어들을 CPU가 읽고 처리한다.
> - ISA는 IA-32, x86-64(x64), MIPS, AVR 등 다양하게 존재한다.
> - 모든 컴퓨터가 동일한 수준의 연산 능력을 요구하지 않으며,
>   컴퓨팅 환경도 다양하기 때문에 다양한 ISA가 개발되고 사용된다.
![[Pasted image 20240809143027.png]]

#### n 비트 아키텍처
- '64비트 아키텍처', '32비트 아키텍처'에서 64와 32는 CPU가 한번에 처리할 수 있는 데이터의 크기를 의미
- 컴퓨터과학에서는 이를 *CPU가 이해할 수 있는 데이터의 단위*라는 의미에서 **WORD** 라 부른다.
- WORD의 크기는 CPU가 어떻게 설계됐느냐에 따라 달라진다.

#### WORD가 크면 유리한 점
- 현대 PC의 대부분은 64비트 아키텍처의 CPU를 사용하는데, 그 이유 중 하나는 32비트 아키텍처의 CPU가 제공할 수 있는 [가상 메모리](VirtualMemory.md)의 크기가 작기 때문이다.
- 32비트 아키텍처에서는 4기가 바이트가 최대로 제공할 수 있어 일반적으로 사용에 문제는 없지만, 많은 메모리 자원을 요구하는 소프트웨어나 고사양 게임 등을 실행하면 부족할 수 있다.
- 반면 64비트 아키텍처는 이론상 16엑사 바이트의 가상 메모리를 제공할 수 있어 웬만한 상황에서는 메모리 자원 부족으로 인한 프로그램 성능 저하는 발생할 일이 없다. 

# x86, [x86-64](x86-64아키텍처.md)
---

# ARM
---

# MIPS
---

# AVR
---
