- 윈도우의 스케줄 기능
- **주기적**으로 반복되는 일을 자동으로 실행될 수 있도록 설정하는 기능
- 관련된 데몬(서비스 : crond)

![[Pasted image 20240825141444.png]]

분 시 일 월 요일       계정              명령어
\*    *    *    *    *     user-name    command to be executed

ex)
- 0 0 1 * * root /home/test.sh
	: 모든 요일 1월 1일 3시 5분에 root 계정으로 /home/test.sh 실행
- 5 3 1 1 * root /home/test.sh 
	: 모든 요일 매월 1일 0시 0분에 root 계정으로 /home/test.sh 실행

![[Pasted image 20240825143620.png]]
cron으로 실행할 명령어가 저장될 디렉토리들

run-parts : 뒤의 디렉토리에 있는 모든 명령어를 실행하는 명령어

요일 : 0(일)~6(토)

`systemctl restart crond` : cron 설정 파일 설정 후 적용 명령어
`systemctl status crond` : crond 실행 상태 확인 명령어

```
10 * * * * root run-parts /etc/cron.monthly
20 * * * * root run-parts /etc/cron.monthly
30 * * * * root run-parts /etc/cron.monthly
40 * * * * root run-parts /etc/cron.monthly
50 * * * * root run-parts /etc/cron.monthly
00 * * * * root run-parts /etc/cron.monthly
```
위 cron을 한줄로 축약하는 방법
```
*/10 * * * * root run-parts /etc/cron.monthly
```

at 이라는 명령어도 있다.

- [cron web 자료](https://zerostarting.tistory.com/23)