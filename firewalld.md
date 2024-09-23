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
	- public으로 설정되어 있을 것이다.

- active zone 확인
```
firewall-cmd --get-active-zone
```

- all zone 확인
```
firewall-cmd --get-zones
```

- 특정 zone 정책 확인
```
firewall-cmd --zone=home --list-all
```

- 인터페이스에 zone 할당
```
firewall-cmd --zone=home --change-interface=enp0s3
```
	- zone을 할당하면 자동으로 활성 상태가 된다.

- default zone 변경
```
firewall-cmd --set-default-zone=home
```

- 서비스 목록 보기
```
firewall-cmd --get-services
```