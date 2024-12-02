---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'



# Code Block

```bash
version: '3.8'

services:
  wordpress:
    image: wordpress:5.0.3-apache
    ports:
      - "80:80"
    depends_on:
      - mariadb
    environment:
      WORDPRESS_DB_HOST: mariadb
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    restart: always

  mariadb:
    image: mariadb:latest
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: word123pass456
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    restart: always

volumes:
  db_data: {}
```

# Excalidraw Data
## Text Elements
[mission 1]
wordpress 5.x 이미지, 컨테이너 실행
wordpress 머신에 웹페이지 제작 후 정상 접속 확인
변경 사항을 포함한 이미지 생성 후 Docker Hub 업로드 후 확인 ^akFyW21k

- docker-compose.yml 파일을 통해 다수의 컨테이너 설정을 한번에 정의 ^F9BXZtX8

- docker compose up -d "docker-compose.yml 설정에 따라 컨테이너 실행" ^gjVC1h1s

## Element Links
dxLgULur: [[Excalidraw/Docker_실습.md#Code Block]]

%%
## Drawing
```compressed-json
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

AoQ9U9BZBFBRm12YAq69iwQhowAviWMQAA==
```
%%