![[Pasted image 20241018090610.png]]
# \[취약한 Wordpress 서버 구축]
![[Pasted image 20241018091050.png]]
![[Pasted image 20241018091334.png]]
## 1. docker 환경 구축
![[Pasted image 20241018091650.png]]
## 2. docker 환경 설정 파일
```yml
version: '3.1'

services:

  wordpress:
    image: wordpress:4.7-php5.6-apache  # PHP 5.6과 워드프레스 4.7이 포함된 이미지
    restart: always
    ports:
      - 8080:80  # 워드프레스 컨테이너에서 포트 80을 호스트의 포트 8080으로 연결
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: exampleuser
      WORDPRESS_DB_PASSWORD: examplepass
      WORDPRESS_DB_NAME: exampledb
    volumes:
      - ./wordpress_data:/var/www/html  # 워드프레스 파일이 저장될 경로

  db:
    image: mariadb:10.5  # MariaDB 10.5 이미지 사용
    restart: always
    environment:
      MARIADB_DATABASE: exampledb
      MARIADB_USER: exampleuser
      MARIADB_PASSWORD: examplepass
      MARIADB_ROOT_PASSWORD: rootpass
    volumes:
      - ./db_data:/var/lib/mysql  # MariaDB 데이터베이스 파일 저장 경로

  phpmyadmin:
    image: phpmyadmin/phpmyadmin  # phpMyAdmin 컨테이너
    restart: always
    ports:
      - 8081:80  # phpMyAdmin 포트 8081에서 실행
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: rootpass

```
## 3. 실행
```sh
docker compose up -d
```
![[Pasted image 20241018092214.png]]
## 4. wordpress 설정
![[Pasted image 20241018092358.png]]