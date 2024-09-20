```bash
df -h
```

```baSH
vi ./disk_check.sh
###########################
#!/bin/bash

#Designation of e-mail address
MAIL="jaeho6627@kakao.com"

DVAL=`/bin/df/ | /usr/bin/tail -l | /bin/sed 's/^.*\([0-9]*\)%.*$/\1/'`

if [$DVAL -gt 80]; then
        echo "Disk usage alert: $DVAL %" | mail -s "Disk Space Alert in 'hostname'" $M
AIL
fi
###########################
```
