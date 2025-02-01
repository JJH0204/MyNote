CMake 가 빌드 파일을 생성하는데 필요한 정보들이 들어있어야 한다.

## 초 간단 설정
CMakeLists.txt
```
// 예시
cmake_minimum_required(VERSION 3.10)
project(UsingStack)
add_executable(checkBracketMatch checkBracketMatch.c Stack.c)
```

```
// 설명
cmake_minimum_required(VERSION 0.00)
project(프로젝트 이름)
add_executable(실행파일이름 실행파일.c 추가소스파일.c ...)
```

이후 F1 > CMake: quickStart 선택 > 빌드 진행 > 실행 (맥에서 안됨...)

# Cpp 프로젝트 용 CMakeLists.txt
```cmake
# CMake 최소 버전 설정
cmake_minimum_required(VERSION 3.11)

# 프로젝트 설정
project(CppProject VERSION 0.1 LANGUAGES CXX)

#c++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# UTF-8 인코딩을 위한 컴파일러 옵션 설정
add_compile_options(
    $<$<CXX_COMPILER_ID:GNU>:-finput-charset=UTF-8>
    $<$<CXX_COMPILER_ID:Clang>:-finput-charset=UTF-8>
)

# 디버그 모드 설정
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG -g")

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()


if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    # macOS-specific settings
    message(STATUS "Configuring for macOS")
    
    # 서브 프로젝트 추가: project_Basics
    add_subdirectory(Basics)
    add_subdirectory(OOP)
    add_subdirectory(Tetris)
elseif(CMAKE_SYSTEM_NAME STREQUAL "Windows")
    # Windows-specific settings
    message(STATUS "Configuring for Windows")
    # 서브 프로젝트 추가: project_Basics
    add_subdirectory(Basics)
    add_subdirectory(OOP)
    add_subdirectory(Tetris)
else()
    message(STATUS "Configuring for Other OS")
    # 서브 프로젝트 추가: project_Basics
    add_subdirectory(Basics)
    add_subdirectory(OOP)
    add_subdirectory(Tetris)
endif()
```

- 총 3개의 서브 프로젝트를 관리하는 루트 디렉토리에 저장된 CMakeLists.txt 의 데이터
- 각 서브 프로젝트 중 가장 최신 [[C++ 프로젝트]]인 Tetris의 CMakeLists.txt 데이터는 아래와 같다.

```cmake
cmake_minimum_required(VERSION 3.10)
project(Tetris)

# ncurses 라이브러리 찾기
find_package(Curses REQUIRED)

# src 디렉토리 내의 모든 소스 파일 수집
file(GLOB SOURCES "source/*.cpp")

# 실행 파일 생성 및 소스 파일 지정
add_executable(Tetris main.cpp ${SOURCES})

# ncurses 라이브러리 링크
target_link_libraries(Tetris PRIVATE ${CURSES_LIBRARIES})

# 추가 라이브러리 링크 혹은 옵션 지정
target_include_directories(Tetris PRIVATE ${CURSES_INCLUDE_DIR} include)
```