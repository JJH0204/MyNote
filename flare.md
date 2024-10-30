![[Pasted image 20241028092753.png]]
- 실시간 보안 끄기

![[Pasted image 20241028092912.png]]![[Pasted image 20241028092943.png]]
![[Pasted image 20241028093028.png]]
설치받고 압축풀고 intall 파일 확인
![[Pasted image 20241028093222.png]]
관리자 권한으로 실행
![[Pasted image 20241028093253.png]]
![[Pasted image 20241028093339.png]]![[Pasted image 20241028093541.png]]

![[Pasted image 20241028093602.png]]

![[Pasted image 20241028104227.png]]
gpedit.msc 에서 안되면 아래 사이트에서 파일 설치

Bitdefender 설치
https://www.bitdefender.com/

y

암호 설정

ollydbg.vm 추가

PracticalMalwareAnalysis-Labs git 설치

윈도우 자동 업데이트 끄기

정적 분석 도구: PEID/EXEINFO PE/BinText/PEView/Strings/Dependency Walker
동적 분석 도구: Process Explorer/Process Monitor/Autoruns/Wireshark/IDA DisAssembler/ollyDBG (Sysinternals 로 한번에 설치 가능)
/ HxD
- git 에서 설치하면 됨

- 컴파일 시점 / 패킹 여부 / 코드 내 함수 실행(Import) / 호스트 기반 증거 / 네트워크 기반 증거 / 목적 / 대응방안
virustotal.com

# 정적
패킹(Packing) - 언패킹(Unpacking)
패커(Packer-패킹 툴)

난독화/압축/암호화 가 해당

UPS

pe - 실행파일

![[Pasted image 20241028140438.png]]![[Pasted image 20241028140706.png]]= PE Header
![[Pasted image 20241028140726.png]]= PE Body

![[Pasted image 20241028140837.png]]: 도스 호환을 위해 현재까지 사용 중인 해더
![[Pasted image 20241028140911.png]], mz = 실행파일이다
시그니처 = [매직넘버](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5) 

![[Pasted image 20241028141057.png]]
Signature는 위와 다름
![[Pasted image 20241028141144.png]] (파일의 속성값)컴파일 시간을 알 수 있다.
![[Pasted image 20241028141200.png]]


PEID
![[Pasted image 20241028141820.png]]
- 패킹 여부 확인이 안됨

EXEINFO PE
![[Pasted image 20241028142259.png]]
- 편집기 / 컴파일 시간 확인가능
- 패킹 여부를 확인할 수 있다.

OLLYDBG
![[Pasted image 20241028142531.png]]
- 실행파일의 어셀블리 코드를 확인할 수 있다
- 악성코드의 공격방식을 대략적으로 확인할 수 있다.
![[Pasted image 20241028143045.png]]
- 함수의 내용이 중요

HxD
![[Pasted image 20241028143358.png]]
- 상세한 헥사 코드 분석
- kernel32.dll의 영향으로 시간 값이 바뀌는 것을 예상할 수 있다

BINTEXT
![[Pasted image 20241028144304.png]]
- 모든 텍스트 문자열을 읽기 쉽게 정리

동적 분석은 스냅샷을 찍어서 프로그램의 실행 전과 후를 비교할 수 있도록 한다.
![[Pasted image 20241028150558.png]]

- 스크린샷 찍어두고 악성코드 실행
![[Pasted image 20241028151634.png]]



컴파일 시점: 10년10월4일
/ 패킹 여부: 안함
/ 코드 내 함수 실행(Import): Kernel32.dll -> Kerne132.dll로 복제
/ 호스트 기반 증거: Kerne132.dll
/ 네트워크 기반 증거: Lab01-01.dll(WS2_32.dll 실행/127.26.152.13)
/ 목적: Kerne132.dll를 생성>시스템을 지연>악성프로그램 탐지 방지>공격자 시스템으로 백도어 설정
/ 대응방안: 불필요한 프로세스 중지 및 기존 서비스 내용 확인, 백신 프로그램 설치

[dll](https://learn.microsoft.com/ko-kr/cpp/build/kinds-of-dlls?view=msvc-170) 파일에 대한 사전 정보를 학습할 필요가 있다.

[[Lab03-01]]
[[Lab05]]
[[Lab06]]
[[Lab07]]
[[Lab09]]
