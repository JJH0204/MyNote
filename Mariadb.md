mysql의 후속작으로 거의 모든 명령어가 mysql과 동일

## 보안 설정 (필수)
---
```sh
mysql-secure-installation
```

## 명령어
---
```
mysql -u root -p // root 계정으로 DB 접속 (-p가 없어도 접속이 가능하던데?)
mariaDB[(none)]> // DB에 접속 중인 상태 (none) = 접속 중인 DB
mariaDB[(none)]> show databases; // 모든 DB 표시(;으로 명령어 마지막 표시)
mariaDB[(none)]> use [mysql]; //mysql DB 접속
mariaDB[(mysql)]> show [tables]; //DB의 모든 테이블 리스트 출력
mariaDB[(mysql)]> desc [tableName]; // tableName의 칼럼 리스트 출력
mariaDB[(mysql)]> select * from [tableName]; // tableName의 모든 데이터 출력
mariaDB[(mysql)]> select [칼럼1,...] from [tableName]; // tableName에서 칼럼1,... 에 해당하는 데이터만 출력
mariaDB[(mysql)]> exit // DB 나가기
mariaDB[(none)]> creat database [DBName]; // DB 생성
mariaDB[(none)]> use [DBName];
mariaDB[(DBName)]> creat table [tableName] (); // 테이블 생성

```