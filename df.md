```bash
df -h
```

```bash
vi ./disk_check.sh
###########################
#!/bin/bash

#Designation of e-mail address
MAIL="<your mailaddress>"

DVAL=`/bin/df / | /usr/bin/tail -1 | /bin/sed 's/^.* \([0-9]*\)%.*$/\1/'`

if [ $DVAL -gt 80 ]; then
        echo "Disk usage alert: $DVAL %" | mail -s "Disk Space Alert in 'hostname'" $MAIL
fi
###########################
chmod 700 disk_check.sh
```

- 테스트를 위한 더미 파일 생성
```shell
dd if=/dev/zero of=dummyfile bs=1M count=7000
## dd: 파일 생성 명령어
```

- 스크립트 실행
```shell
./disk_check.sh
#############################
./disk_check.sh
s-nail: Warning: $LOGNAME (test) not identical to user (root)!
s-nail: Warning: $USER (test) not identical to user (root)!
s-nail: Cannot start /usr/sbin/sendmail: executable not found (adjust *mta* variable)
/root/dead.letter 8/192
s-nail: ... message not sent
#############################
```
