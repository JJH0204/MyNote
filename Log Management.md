# [[Log_File]]
---

# Logrotate
---
```
○ logrotate.service - Rotate log files
     Loaded: loaded (/usr/lib/systemd/system/logrotate.service; static)
     Active: inactive (dead) since Fri 2024-09-20 09:22:01 KST; 5h 12min ago
TriggeredBy: ● logrotate.timer  # <- 동작 중임을 알 수 있다.
       Docs: man:logrotate(8)
             man:logrotate.conf(5)
    Process: 678 ExecStart=/usr/sbin/logrotate /etc/logrotate.conf (code=exited, stat>
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