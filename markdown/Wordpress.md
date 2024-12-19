# Wordpress 환경 구축
## Use Docker
### 1. Docker 저장소 설정
- Docker 패키지는 기본 Rocky Linux 리포지터리에 포함되어 있지 않기 때문에, Docker 공식 리포지터리를 추가해줘야 한다.
```
dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

### 2. Docker 설치
