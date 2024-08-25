- 윈도우의 스케줄 기능
- 주기적으로 반복되는 일을 자동으로 실행될 수 있도록 설정하는 기능
- 관련된 데몬(서비스 : crond)

![[Pasted image 20240825141444.png]]

분 시 일 월 요일       계정              명령어
\*    *    *    *    *     user-name    command to be executed

ex)
- 0 0 1 * * root /home/test.sh
	: 모든 요일 1월 1일 3시 5분에 root 계정으로 /home/test.sh 실행
- 5 3 1 1 * root /home/test.sh : 