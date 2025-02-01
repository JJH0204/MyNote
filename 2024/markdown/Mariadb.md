mysql의 후속작으로 거의 모든 명령어가 mysql과 동일
- [[RDBMS]]

## 보안 설정 (필수)
---
```sh
mysql-secure-installation
```

## DB 명령어
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
mariaDB[(DBName)]> creat table [tableName] (칼럼 자료형(자리수), ...); // 테이블 생성

```

## Table 명령어
---
```
alter table [tableName] add [칼럼이름] [자료형] [순서];
// 칼럼 추가 명령어 (순서 생략가능)
// (칼럼이름 자료형(자릿수), ...) 형식으로 다수 입력 가능
// 순서 미 입력 시 기본으로 가장 뒤에 저장
// first: 가장 처음, after 칼럼이름: 해당 칼럼의 뒤에, defore 칼럼이름: 해당 칼럼 앞에

alter table [tableName] modeify [칼럼이름] [자료형] [순서];
// 이미 입력된 칼럼의 정보 수정에 사용(자료형, 순서)

alter table [tableName] drop [칼럼이름];
// 칼럼 삭제

alter table [tableName1] [tableName2];
// 칼럼이름 변경

insert int [tableName] (칼럼1, 칼럼2, ...) values (값1, 값2, ...);
// 데이터 입력

update [tableName] set 칼럼 = 값;
// 해당 칼럼의 모든 행에 저장된 데이터를 '값'으로 변경

update [tableName] set 칼럼 = 값 where [기준칼럼] = [키값];
// 기준칼럼의 행들 중 키값에 해당하는 행의 칼럼에 값 대입

delete from [tableName] where 칼럼 = 값;
// 칼럼에 값을 저장한 행을 삭제

delete from [tableName];
// 테이블 삭제

drop [대상] [이름]; // 데이터 삭제 명령어
```