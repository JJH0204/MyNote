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
