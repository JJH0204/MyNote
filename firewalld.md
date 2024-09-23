- 서비스 활성 여부
```
firewall-cmd --state
systemctl status firewalld
```

- 서비스 정책 확인
```
firewall-cmd --list-all
```

![[Pasted image 20240923091158.png]]


- default zone 확인
```
firewall-cmd --get-default-zone
```

- active zone 확인
```
firewall-cmd --get-active-zone
```

- all zone 확인
```
firewall-cmd --get-zones
```