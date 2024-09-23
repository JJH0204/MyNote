- 서비스 활성 여부
```sh
firewall-cmd --state
systemctl status firewalld
```

- 서비스 정책 확인
```sh
firewall-cmd --list-all
```

![[Pasted image 20240923091158.png]]


- default zone 확인
```sh
firewall-cmd --get-default-zone
```
	- public으로 설정되어 있을 것이다.

- active zone 확인
```sh
firewall-cmd --get-active-zone
```

- all zone 확인
```sh
firewall-cmd --get-zones
```

- 특정 zone 정책 확인
```sh
firewall-cmd --zone=home --list-all
```

- 인터페이스에 zone 할당
```sh
firewall-cmd --zone=home --change-interface=enp0s3
```
	- zone을 할당하면 자동으로 활성 상태가 된다.

- default zone 변경
```sh
firewall-cmd --set-default-zone=home
```

- 서비스 목록 보기
```sh
firewall-cmd --get-services
```

- 서비스 방화벽 설정 파일 경로
```sh
/usr/lib/firewalld/services/
```
```sh
cat /usr/lib/firewalld/services/ssh.xml
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>SSH</short>
  <description>Secure Shell (SSH) is a protocol for logging into and executing commands on remote machines. It provides secure encrypted communications. If you plan on accessing your machine remotely via SSH over a firewalled interface, enable this option. You need the openssh-server package installed for this option to be useful.</description>
  <port protocol="tcp" port="22"/>
</service>
```

- zone 설정 파일 경로
```sh
/usr/lib/firewalld/zones/
```
```sh
block.xml      drop.xml       home.xml       nm-shared.xml  trusted.xml
dmz.xml        external.xml   internal.xml   public.xml     work.xml
```
```
cat /usr/lib/firewalld/zones/public.xml
```
```xml
<?xml version="1.0" encoding="utf-8"?>
<zone>
  <short>Public</short>
  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
  <service name="ssh"/>
  <service name="dhcpv6-client"/>
  <service name="cockpit"/>
  <forward/>
</zone>
```