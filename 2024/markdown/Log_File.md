```
cd /var/log && ls

anaconda           cron-20240920        kdump.log          README            tallylog
audit              dnf.librepo.log      lastlog            samba             tuned
boot.log           dnf.log              maillog            secure            wtmp
boot.log-20240920  dnf.rpm.log          maillog-20240920   secure-20240920
btmp               firewalld            messages           spooler
chrony             hawkey.log           messages-20240920  spooler-20240920
cron               hawkey.log-20240920  private            sssd

```

## **btmp**
---
- 접속 실패 기록 저장
- `lastb` 또는 `last -f /var/log/btmp` 명령어로 확인

## **utmp**
---
- 사용자 기록
- 현재 시스템에 접속한 사용자 로그
- `who`, `who am i` 명령어로 확인 가능

## **wtmp**
---
- 로그인 성공한 기록
- `last`, `last -f /var/log/wtmp` 명령어로 확인

## **lastlog**
---
- 전체 사용자의 마지막 로그인 기록
- `lastlog` 명령어로 확인
- `lastlog -u root` 지정한 사용자의 로그인 기록 출력
- `lastlog -t 5`: 기간 동안 로그인한 기록
- `lastlog -b 19`: 지정한 날짜 이전 로그 기록 출력

## messages
---
- Linux 시스템 로그
## secure
---
- 인증 관련 로그

## [[cron]]
---
- 시스템 자동화(스케쥴러)