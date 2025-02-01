```
# 프로젝트 정보
project(
	ProjectName
	VERSION 0.1
	DESCRIPTION "예제 프로젝트"
	LANGUAGES CXX
)
```
- ProjectName: 프로젝트 이름, 임의의 이름을 설정할 수 있다.
- LANGUAGES: 프로젝트에서 사용하는 언어 설정 (C = C, C++ = CXX)
	- 값을 설정하지 않으면 디폴트로 C와 CXX로 설정됨
	- 그 외 언어 [참고자료](https://cmake.org/cmake/help/latest/command/project.html)
- 