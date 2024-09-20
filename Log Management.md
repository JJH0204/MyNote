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

# btmp
- binary file
- `lastb` 또는 `last -f /var/log/btmp` 명령어로 확인
- 접속 실패 기록 저장

# utmp
- 사용자 기록
- 현재 시스템에 접속한 사용자 로그
- `who`, `who am i` 명령어로 확인 가능

# wtmp
