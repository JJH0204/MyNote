---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'



# Code Block

```dockerfile
# 베이스 이미지 설정
FROM ubuntu:latest

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    apache2 \
    mariadb-server \
    php \
    php-mysql \
    curl \
    && apt-get clean

# WordPress 다운로드 및 설정
RUN curl -o /tmp/wordpress.tar.gz https://wordpress.org/latest.tar.gz && \
    tar -xzf /tmp/wordpress.tar.gz -C /var/www/html && \
    rm /tmp/wordpress.tar.gz && \
    chown -R www-data:www-data /var/www/html/wordpress && \
    chmod -R 755 /var/www/html/wordpress

# Apache 설정 활성화
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    a2enmod rewrite

# 포트 설정
EXPOSE 80

# MariaDB 기본 설정
RUN service mysql start && \
    mysql -e "CREATE DATABASE wp_database;" && \
    mysql -e "CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'wp_password';" && \
    mysql -e "GRANT ALL PRIVILEGES ON wp_database.* TO 'wp_user'@'localhost';" && \
    mysql -e "FLUSH PRIVILEGES;"

# 시작 스크립트
CMD service mysql start && service apache2 start && tail -f /dev/null
```

# Excalidraw Data
## Text Elements
Ubuntu wordpress myself ^j2dWnWGT

도커 이미지 생성
- docker image tag ubuntu krjaeh0/ubuntu-wordpress:latest
 ^AKKNVJuN

[root@Rocky ~]# docker container ls
CONTAINER ID   IMAGE           COMMAND       CREATED          STATUS          PORTS                                     NAMES
0a1244bff39c   ubuntu:latest   "/bin/bash"   29 minutes ago   Up 29 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   ubuntu-wordpress ^Xd6nsNpX

docker commit 0a1244bff39c krjaeh0/ubuntu-wordpress:latest ^7fI0izMh

docker image push krjaeh0/ubuntu-wordpress:latest ^yj7IMaOI

위 도커 이미지를 이용해 wordpress 서비스를 구동할 경우 apache2 / mariadb 서비스를 직접 활성화 할 필요가 있다.

docker run -it --name ubuntu-wp -p 8080:80 krjaeh0/ubuntu-wordpress:latest
(또는 이미 컨테이너가 실행 중이라면)-> docker exec -it <컨테이너 ID> /bin/bash

service apache2 start && service mariadb start ^uRpB4dCL

docker run --name ubuntu-wp -p 8080:80 krjaeh0/ubuntu-wordpress:latest bash -c "service apache2 start && service mariadb start && tail -f /dev/null" ^yZNxHdps

`docker run` 명령어와 `service apache2 start && service mariadb start`를 하나의 명령어로 묶으려면, Docker 컨테이너의 실행 시점에 `bash` 명령어를 활용해 초기화 스크립트를 실행하면 돼. 아래는 이를 구현하는 방법이야.

---

## 1. **명령어 한 줄로 실행**

`docker run` 명령어에서 `bash -c`를 사용하면 두 서비스를 시작하고 컨테이너를 유지하는 명령을 작성할 수 있어:

```bash
docker run -it --name ubuntu-wp -p 8080:80 krjaeh0/ubuntu-wordpress:latest bash -c "service apache2 start && service mariadb start && tail -f /dev/null"
```

### 명령어 설명:
- **`bash -c`**: 복합 명령어를 실행.
- **`service apache2 start`**: Apache2 서비스 시작.
- **`&&`**: 이전 명령이 성공하면 다음 명령 실행.
- **`service mariadb start`**: MariaDB 서비스 시작.
- **`tail -f /dev/null`**: 컨테이너를 종료하지 않고 계속 실행 상태를 유지.

---

## 2. **스크립트 파일로 처리**

명령어가 길다면 스크립트 파일로 만들어 간단히 처리할 수 있어.

### 스크립트 파일 작성
컨테이너 안에서 실행할 초기화 스크립트를 작성:
```bash
echo -e "#!/bin/bash\nservice apache2 start\nservice mariadb start\ntail -f /dev/null" > init.sh
chmod +x init.sh
```

### 스크립트 기반으로 실행
위 스크립트를 컨테이너에 복사한 후, 다음과 같이 실행:
```bash
docker run -it --name ubuntu-wp -p 8080:80 krjaeh0/ubuntu-wordpress:latest ./init.sh
```

---

## 3. **Dockerfile 수정 (최적화 방법)**

이미지 자체를 수정해 항상 두 서비스를 자동으로 시작하도록 만들면 실행 명령이 더 간단해져.

### Dockerfile 수정:
Dockerfile에 아래와 같이 `CMD`를 추가:
```dockerfile
CMD service apache2 start && service mariadb start && tail -f /dev/null
```

이미지 빌드:
```bash
docker build -t krjaeh0/ubuntu-wordpress .
```

수정된 이미지를 실행:
```bash
docker run -it --name ubuntu-wp -p 8080:80 krjaeh0/ubuntu-wordpress:latest
```

---

## 4. **Docker Compose 사용**

`docker-compose.yml` 파일을 사용해 서비스를 시작하도록 설정할 수도 있어.

### Compose 파일 작성:
```yaml
version: '3.8'
services:
  ubuntu-wp:
    image: krjaeh0/ubuntu-wordpress:latest
    ports:
      - "8080:80"
    command: bash -c "service apache2 start && service mariadb start && tail -f /dev/null"
```

실행:
```bash
docker-compose up -d
```

---

## 요약

1. **한 줄로 실행**: `docker run`과 `bash -c`를 조합.
2. **초기화 스크립트**: 스크립트를 실행하도록 설정.
3. **Dockerfile 수정**: 이미지에서 자동으로 실행되도록 구성.
4. **Docker Compose**: 관리와 실행을 단순화.

이 중 하나를 선택해 사용하면 돼. 가장 간단한 방법은 한 줄로 실행하는 첫 번째 방법이야! 😊 ^xvGFh9uR

## Element Links
8aYAVKPI: [[ubuntu-wordpress docker]]

mac523sr: [[Excalidraw/rb_project.md#Code Block]]

zxVcQ1Di: [[docker-hub image share]]

## Embedded Files
a2f0e97b8ab12337bd0cb1e7d0391fa550cf1e20: [[Pasted Image 20241206090842_911.png]]

f4b237f743ec0aee85ba7aa7c31d3397ae34cf27: [[Pasted Image 20241206122638_902.png]]

%%
## Drawing
```compressed-json
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
```
%%