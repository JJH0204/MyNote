- Shell 자동화를 위해 작성하는 Script
> [!자동화가 필요한 이유]
> - 많은 보안 점검 사항, 나아가 Unix, windows 시스템에서 시행하는 반복 작업들을 자동화하여 효율을 높일 수 있다.

- Unix / Windows 모두 Shell 이라는 시스템을 탑재하고 있기 때문에 Shell Script 작성 방법에 익숙해 진다면 더 편리해 질 것이다.
- 인터프리트 언어에 속한다.
- [관련자료](https://m.blog.naver.com/hj_kim97/222586947801)

sh > 초기 unix shell
ksh > '콘쉘'이라고 읽음, sh 확장
csh > 버클리대학에서 개발한 shell
**bash** > 호환성이 뛰어난 shell
zsh 등등 다양한 종류의 shell이 있다.

출력 함수
``` bash
echo $(which bash) #명령어 실행 결과를 텍스트로 출력
# /usr/bin/bash
```

씨방: 쉘 선언문을 의미한다.
```bash
#!/usr/bin/bash # 씨방이라 한다.

echo $(which bash)
```

