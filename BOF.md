# Stack Buffer Overflow
---
- buffer: 데이터 입출력을 위해 사용되는 임시 저장소, 시스템 마다 크기는 다름
- 악의 적으로 shell 코드를 삽입 > buffer를 초과하는 데이터를 입력 > 다른 메모리를 침범(Over ride)하며 shell code를 실행하도록 만듬(악성 코드)
- stack overflow, hip overflow 
## 메모리 형태
---
- kernel memory: 운영체제
- stack memory: 지역, 매개 변수 / 함수
- 라이브러리 memory: 
- hip memory: 동적 변수
- bata memory: 전역, 정적 변수
- code memory: 기계어/어셈블리어
