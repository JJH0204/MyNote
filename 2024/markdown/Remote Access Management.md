/etc/ssh/sshd_config
```
40 PermitRootLogin no # 원격 접속 시 root 계정 사용 불가능하게 변경
```

telnet, rsh 시스템 삭제
```
dnf remove -y telnet-server
```
