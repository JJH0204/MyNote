```bash
df -h
```

```bash
vi ./disk_check.sh
###########################
#!/bin/bash

#Designation of e-mail address
MAIL="jaeho6627@kakao.com"

DVAL=`/bin/df | /usr/bin/tail -l | /bin/sed 's/^.*\([0-9]*\)%.*$/\1/'`

if [$DVAL -gt 80]; then
        echo "Disk usage alert: $DVAL %" | mail -s "Disk Space Alert in 'hostname'" $M
AIL
fi
###########################
chmod 700 disk_check.sh
```

- 테스트를 위한 더미 파일 생성
```
dd if=/dev/zero of=dummyfile bs=1M count=7000
```
```
```