> 커널에서 동작하는 Linux용 보안 아키텍처
> [관련자료](https://velog.io/@ujeongoh/SELinux-Security-Enhanced-Linux)

**상태 확인**
```sh
sestatus
```
```sh
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing # 적용 중인 모드
Mode from config file:          enforcing # 설정 파일의 모드
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      33
```

**상태값**
- Enforcing: 활성화, 기록, 적용 상태
- Permissive: 활성화, 기록은 하지만 적용은 하지 않는 상태
- Disabled: 비활성화

**SELinux log**
```sh
/var/log/audit/audit.log
```
```sh
type=SYSCALL msg=audit(1727053795.603:148): arch=c000003e syscall=46 success=yes exit=384 a0=6 a1=7ffca00d4940 a2=0 a3=7ffca00c37ec items=0 ppid=1 pid=674 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm="firewalld" exe="/usr/bin/python3.9" subj=system_u:system_r:firewalld_t:s0 key=(null)ARCH=x86_64 SYSCALL=sendmsg AUID="unset" UID="root" GID="root" EUID="root" SUID="root" FSUID="root" EGID="root" SGID="root" FSGID="root"
type=PROCTITLE msg=audit(1727053795.603:148): proctitle=2F7573722F62696E2F707974686F6E33002D73002F7573722F7362696E2F6669726577616C6C64002D2D6E6F666F726B002D2D6E6F706964
```

**현재 동작 상태**
```sh
getenforce
```

**모드 변경**
```sh
setenforce 0 # Permissive
# usage:  setenforce [ Enforcing | Permissive | 1 | 0 ]
```
- 설정 파일을 변경하는 것은 아님으로 영구 적용을 하려면 설정 파일을 수정해야 한다.
- 설정 파일 적용 후 reboot 해야 적용이 된다. 
- disabled 로 변경하려면 설정 파일을 수정하는 방법 밖에 없다.

**설정 파일**
```sh
/etc/sysconfig/selinux
```
```sh
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
# See also:
# https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/changing-selinux-states-and-modes_using-selinux#changing-selinux-modes-at-boot-time_changing-selinux-states-and-modes
#
# NOTE: Up to RHEL 8 release included, SELINUX=disabled would also
# fully disable SELinux during boot. If you need a system with SELinux
# fully disabled instead of SELinux running with no policy loaded, you
# need to pass selinux=0 to the kernel command line. You can use grubby
# to persistently set the bootloader to boot with selinux=0:
#
#    grubby --update-kernel ALL --args selinux=0
#
# To revert back to SELinux enabled:
#
#    grubby --update-kernel ALL --remove-args selinux
#
SELINUX=enforcing # 이 값을 disabled로 바꿔야 적용된다.
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

**명령어로 설정 끄기**
`grubby --update-kernel ALL --args selinux=0`

**명령어로 설정 켜기**
`grubby --update-kernel ALL --remove-args selinux`

**정책 세부 설정 파일**
```sh
/etc/selinux/targeted/policy/policy.33
# 바이너리 파일이기 때문에 읽을 수는 없다.
```

**Label(Context)정보 보기**
- **Security Policy가 접근 제어 Policy를 적용하는데 사용**되는 **Label**이라는 것을 SELinux가 각 파일에 할당한다.
```
 ls -Zl /etc/selinux/targeted/policy/
total 3384
-rw-r--r--. 1 root root unconfined_u:object_r:semanage_store_t:s0 3462772 Aug 30 09:01 policy.33
```
- unconfined_u: selinux의 사용자 **User**
  (policy.33에 정의되어 있음, shell에서 생성 불가능)
- object_r: 사용자가 수행할 수 있는 역할 **Roles**
- semanage_store_t: 객체 유형
  (httpd_sys_connect_t: httpd 접근 허용)
- s0: 보안 레벨
  (default = 0, 

```sh
touch test.html
chcon -t admin_home_t test.html # 타입을 지정해서 파일 생성
```
```sh
-rw-r--r--. 1 root root unconfined_u:object_r:admin_home_t:s0   0 Sep 23 10:46 test.html
```
```sh
restorecon test.html # 타입 초기화
```

Roles 관리
```
semanage
```
```
semanage fcontext -a -t httpd_sys_content_t "/test(/.*)?"
```
```
cat /etc/selinux/semanage.conf
```
```
# Authors: Jason Tang <jtang@tresys.com>
#
# Copyright (C) 2004-2005 Tresys Technology, LLC
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# Specify how libsemanage will interact with a SELinux policy manager.
# The four options are:
#
#  "source"     - libsemanage manipulates a source SELinux policy
#  "direct"     - libsemanage will write directly to a module store.
#  /foo/bar     - Write by way of a policy management server, whose
#                 named socket is at /foo/bar.  The path must begin
#                 with a '/'.
#  foo.com:4242 - Establish a TCP connection to a remote policy
#                 management server at foo.com.  If there is a colon
#                 then the remainder is interpreted as a port number;
#                 otherwise default to port 4242.
module-store = direct

# When generating the final linked and expanded policy, by default
# semanage will set the policy version to POLICYDB_VERSION_MAX, as
# given in <sepol/policydb.h>.  Change this setting if a different
# version is necessary.
#policy-version = 19

# expand-check check neverallow rules when executing all semanage
# commands. There might be a penalty in execution time if this
# option is enabled.
expand-check=0

# usepasswd check tells semanage to scan all pass word records for home directories
# and setup the labeling correctly. If this is turned off, SELinux will label only /home
# and home directories of users with SELinux login mappings defined, see
# semanage login -l for the list of such users.
# If you want to use a different home directory, you will need to use semanage fcontext command.
# For example, if you had home dirs in /althome directory you would have to execute
# semanage fcontext -a -e /home /althome
usepasswd=False
bzip-small=true
bzip-blocksize=5
ignoredirs=/root;/bin;/boot;/dev;/etc;/lib;/lib64;/proc;/run;/sbin;/sys;/tmp;/usr;/var
optimize-policy=true

[sefcontext_compile]
path = /usr/sbin/sefcontext_compile
args = -r $@
[end]
```