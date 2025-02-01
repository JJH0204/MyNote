## [[Remote Access Management]]
---

# Service Management
---
- 내가 사용하지 않는 서비스, 프로토콜 삭제하는 것이 기본
	- nfs-server, tftp, telnet

ls -l /etc/exports
- 파일 자체 접근 권한 확인
- 자체 설정 관리

`ps -ef`를 사용해 실행 중인 서비스 확인 > 삭제 진행


## Auto Mount / print
---
- auto mount d 는 언제든지 로컬에서 공격자가 원하는 서비스 장비를 연결할 수 있기취약한 서버가 된다. 
- `rpm -qa | grep autofs` 관련 패키지 검사
- 설치 되어 있다면 삭제 또는 비활성화 시킨다

## [[cron]]
---
- 해당 파일을 수정할 수 있는 권한을 가진 경우 취약해짐으로 확인 필요
- 일반 사용자도 crontab 을 사용할 수 있다.(내부의 권한을 확인)
```
chmod o-x '/usr/bin/crontab' # other에서 실행 권한을 제거 (+는 추가)
# 기타 사용자의 cron 사용 권한 제거
```
### cron.deny
- 기타 사용자라 crontab을 사용할 수 있는 상황에서 특정 사용자의 권한을 제거할 때 사용

## at
---
- (1 회성) 예약된 작업 실행
- cron 과 같이 관리자 권한을 조절하거나 내부 권한을 조정해 관리
```
ls -l /etc/at.deny # at 차단 사용자 등록
```