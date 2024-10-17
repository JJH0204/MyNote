Percona Monitoring & Management

# 설치 방법
- 소스 코드
- 패키지 관리자 (클라이언트)
- docker (서버)

# 서버 설치
## docker 설치
---
```sh
dnf update -y
dnf install -y docker
```
## 이미지 설치
---
```sh
docker pull percona/pmm-server:latest
```
![[Pasted image 20241017091129.png]]
```sh
docker images
```
## 볼륨 생성
---
```sh
docker volume create pmm-data
```
## 실행 중인 도커 이미지 확인
---
```sh
docker ps
docker ps -a
```
## 이미지 실행
---
```sh
docker run --detach --restart always --publish 443:443 -v pmm-data:/srv --name pmm-server docker.io/percona/pmm-server:latest
```
