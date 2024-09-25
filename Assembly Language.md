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
