```
○ logrotate.service - Rotate log files
     Loaded: loaded (/usr/lib/systemd/system/logrotate.service; static)
     Active: inactive (dead) since Fri 2024-09-20 09:22:01 KST; 5h 12min ago
TriggeredBy: ● logrotate.timer  # <- 동작 중임을 알 수 있다.
       Docs: man:logrotate(8)
             man:logrotate.conf(5)
    Process: 678 ExecStart=/usr/sbin/logrotate(실행 파일) 
							/etc/logrotate.conf(설정 파일) (code=exited, stat>
   Main PID: 678 (code=exited, status=0/SUCCESS)
        CPU: 46ms

Sep 20 09:22:01 Linux1 systemd[1]: Starting Rotate log files...
Sep 20 09:22:01 Linux1 systemd[1]: logrotate.service: Deactivated successfully.
Sep 20 09:22:01 Linux1 systemd[1]: Finished Rotate log files.
```
```
● logrotate.timer - Daily rotation of log files
     Loaded: loaded (/usr/lib/systemd/system/logrotate.timer; enabled; preset: enable>
     Active: active (waiting) since Fri 2024-09-20 09:22:00 KST; 5h 14min ago
      Until: Fri 2024-09-20 09:22:00 KST; 5h 14min ago
    Trigger: Sat 2024-09-21 00:00:00 KST; 9h left
   Triggers: ● logrotate.service
       Docs: man:logrotate(8)
             man:logrotate.conf(5)

Sep 20 09:22:00 Linux1 systemd[1]: Started Daily rotation of log files.
```

> [!왜 logrotate?]
> 시스템에 적재되는 log 파일의 회전률을 위해 관리를 대신 해주는 서비스

## /etc/logrotate.conf
---
```
# see "man logrotate" for details

# global options do not affect preceding include directives

# rotate log files weekly(로그의 회전 주기)
weekly # yearly, monthry, daily

# keep 4 weeks worth of backlogs(로그 파일 개수)
rotate 4 # 개수를 초과하면 기존의 파일 삭제

# create new (empty) log files after rotating old ones
create # 새로운 로그 파일 생성 여부
# empty (빈 로그 파일로 변경)

# use date as a suffix of the rotated file
dateext # 로그 파일을 날짜별로 관리

# uncomment this if you want your log files compressed
#compress # 로그 파일 압축 여부

# packages drop log rotation information into this directory
include /etc/logrotate.d # 환경 설정에 따라 실행할 때 포함할 파일

# system-specific logs may be also be configured here.

```

## /etc/logrotate.d
---
```

```