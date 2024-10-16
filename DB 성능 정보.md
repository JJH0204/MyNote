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

```