[swap?](https://it-serial.tistory.com/entry/Linux-Swap-%ED%8C%8C%ED%8B%B0%EC%85%98%EC%9D%B4%EB%9E%80-CPU-RAM-%ED%95%98%EB%93%9C-%EB%94%94%EC%8A%A4%ED%81%AC-%E2%91%A0)
- 비상용 메모리(하드웨어에 할당한)
- 통상 메모리의 1.5~2배를 swap 파티션으로 할당

```sh
free
```
![[Pasted image 20241016104610.png]]
-m, -h
![[Pasted image 20241016104716.png]]

```sh
sysctl # 커널 옵션 설정
```
-a
![[Pasted image 20241016104813.png]]

swap 메모리 설정 변경
```sh
sysctl -w vm.swappiness=40
```
![[Pasted image 20241016105000.png]]

- 설정 영구 적용
```sh
vi /etc/sysctl.conf
```
![[Pasted image 20241016105053.png]]
- 통상 40~60 사이 값을 설정
# 메모리 정보
![[Pasted image 20241016110355.png]]
```sh
grep MemTotal /proc/meminfo
grep SwapTotal /proc/meminfo
```

# CPU 정보
```sh
cat /proc/cpuinfo
```

# 디스크 확인
```
df -h
```

# 커널 버전 확인
```
cat /proc/version       # 리눅스 커널 버전
cat /etc/rocky-release  # 리눅스 버전
```

# DB 사용자 추가
```sh
groupadd -g 505 dba # DB 관리자 그룹
useradd -u 505 -G dba rocky
```

# DB 버전 확인
```sh
mysql  Ver 15.1 Distrib 10.5.22-MariaDB, for Linux (x86_64) using  EditLine wrapper
```

# DB 별 용량 확인
# DB 계정 추가 관리
```
create user 'jaeho'@'localhost' identified by 'choa0306@@';
```

# DB 계정 열람
```
select User, Password from mysql.user;
```
![[Pasted image 20241016111931.png]]

# DB 권한 보기
```sql
show grants;
```
![[Pasted image 20241016112000.png]]
```
# 특정 사용자 권한 정보 확인
show grants for 'jaeho'@'localhost';
```
![[Pasted image 20241016112107.png]]


```
vi /etc/my.cnf
/etc/my.cnf.d
vi /etc/my.cnf.d/mariadb-server.cnf
```

bind-address
```
bind-address=127.0.0.1 # 원격 접속 비 허용
bind-address=0.0.0.0   # 모든 네트워크 원격 접속 허용
bind-address=192.168.56.0/24 # 해당 내트워크 시스템만 접속 허용
```

추가 설정
```
Port=5000 # 서비스 포트 설정
```

패스워드 보안
```
mysql -u root -p
```


```
create user 'test1'@'%' identified by '1234';
grant all privileges on school.* to 'test1'@'%';
show grants for 'test1'@'%';
```
![[Pasted image 20241016113846.png]]

```
create user 'test2'@'192.168.56.101' identified by '4231';
# test2는 192.168.56.101 시스템에서만 접속 가능
grant select, insert on school.student to 'test2'@'192.168.56.101';
# test2는 192.168.56.101 시스템 에서만 접속 가능 & school.student 테이블에만 select, insert 명령 가능
flush privileges;
```

- revoke 명령으로 권한 삭제 가능

계정 삭제 가능
```
drop user test1;
drop user 'test1'@'%';
```

한번에 권한 지급 하기
```sql
grant all privileges on school.* to 'test3'@'localhost' identified by '1234';
```

한번에 회수하기
```sql
 revoke all on school.* from 'test3'@'localhost';
```
