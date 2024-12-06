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

## Element Links
8aYAVKPI: [[ubuntu-wordpress docker]]

mac523sr: [[Excalidraw/rb_project.md#Code Block]]

## Embedded Files
a2f0e97b8ab12337bd0cb1e7d0391fa550cf1e20: [[Pasted Image 20241206090842_911.png]]

f4b237f743ec0aee85ba7aa7c31d3397ae34cf27: [[Pasted Image 20241206122638_902.png]]

%%
## Drawing
```compressed-json
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
```
%%