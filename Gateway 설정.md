# [[Gateway]]란?
---

# 라우터 설치
---
![[Pasted image 20240819215420.png]]
외부 네트워크와 통신을 위해서는 우선 라우터 설치가 필요하다.
라우터를 설치하는 과정에서 Gateway 설정은 진행하게 된다.
원하는 라우터 모델에 스위치를 연결한다.

# 라우터 확장
---
일부 장치는 모듈화를 통해 슬롯 확장이 가능하다.
이번에는 미리 확장을 시켜 놓으려 한다.
![[Pasted image 20240819215635.png]]
모듈을 설치할 때는 꼭 전원을 끈 상태에서 진행한다.

# Gateway IP 설정
---
스위치와 달리 라우터는 연결된 것 만으로 바로 외부 네트워크와 통신할 수는 없다.
LAN 네트워크에서 라우터를 통해 외부로 나갈 수 있는 통로를 열어주어야 한다.
그것이 Gateway에 IP를 부여하는 과정이다.

전원이 켜진 라우터에 아래 명령어를 순서대로 입력한다.
![[Pasted image 20240819220045.png]]
요약) 
라우터의 Gig0/0 인터페이스에 192.168.10.254/24 IP를 할당하고 꺼지지 않도록 설정

일정 시간이 지나면 연결되었음을 알 수 있는 초록불을 볼 수 있다.

![[Pasted image 20240819220251.png]]
