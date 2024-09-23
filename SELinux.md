> 커널에서 동작하는 Linux용 보안 아키텍처

**상태 확인**
```sh
sestatus
```
```
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      33
```

**상태값**
- Enforcing: 활성화, 기록, 적용 상태
- Permissive: 활성화, 기록은 하지만 적용은 하지 않는 상태
- Disabled: 비활성화

/var/log/audit/audit.log