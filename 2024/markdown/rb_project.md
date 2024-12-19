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

설치 ^OZ9nZE6q

표시된 ip 주소로 접속 ^cLFq3r9H

ubuntu 이미지 업로드(데이터스토어 브라우저) ^sIqSbINT

설치할 때 용량을 넉넉하게 주자
넉넉하게 100GB
메모리도 넉넉하게 주자
  ^SoZsOR6J

하던대로 Ubuntu 설치하고 머신이름이랑 호스트 이름 설정한 것 까먹지말고 기억하기
IP 도 (172.16.153.134:master, 172.16.153.135:work_1, 172.16.153.136:work_2) ^Z6hNmiLu

머신 하나를 구축하고 apt update -y && apt full-upgrade -y
apt install -y openssh-server
systemctl start ssh && systemctl enable ssh 로 시스템 최신화
외부로 옮기고 ova 파일 활용해서 가져오기  ^Pu2IpSC3

## Element Links
8aYAVKPI: [[ubuntu-wordpress docker]]

mac523sr: [[Excalidraw/rb_project.md#Code Block]]

zxVcQ1Di: [[docker-hub image share]]

emfdeh83: https://zkdlu.github.io/2020-12-28/troubleshooting01-%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EC%84%A4%EC%B9%98/

## Embedded Files
a2f0e97b8ab12337bd0cb1e7d0391fa550cf1e20: [[Pasted Image 20241206090842_911.png]]

f4b237f743ec0aee85ba7aa7c31d3397ae34cf27: [[Pasted Image 20241206122638_902.png]]

0005db1d8db7f9d3a98579afc0a85cd1704a6b07: [[Pasted Image 20241206143042_208.png]]

5e5b1f72fc2226f17e1aedf4bdbb929193c85666: [[Pasted Image 20241206143100_399.png]]

ae3a0042e92ae4effb7d8ee17e9e08ec30321d56: [[Pasted Image 20241206144008_462.png]]

0a7d2517052e4cab94cc361dcad1e1e1af9978f5: [[Pasted Image 20241206144049_581.png]]

e9f4b8004a93a57e79c1a57c5ce6fd386851509a: [[Pasted Image 20241206144101_893.png]]

4ed67b2ac6b0636668499e14604826331c6346e4: [[Pasted Image 20241206145938_542.png]]

29b21973181f05f0a5ac078c0b484a6fea40b9cb: [[Pasted Image 20241206154240_050.png]]

%%
## Drawing
```compressed-json
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

3CAaYYuFoggAA===
```
%%