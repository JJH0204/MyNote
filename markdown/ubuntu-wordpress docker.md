Ubuntu 컨테이너 하나만을 사용해 WordPress와 MariaDB를 구성하려면, 하나의 컨테이너 안에서 모든 것을 설정해야 해. 이 방법은 컨테이너 관리가 단순화되지만, 한 컨테이너에 여러 서비스를 실행하기 때문에 시스템 관리 및 디버깅이 어려워질 수 있어.

아래는 하나의 Ubuntu 컨테이너에서 WordPress와 MariaDB를 설정하는 방법이야.

---

## 1. **Ubuntu 기반 Docker 컨테이너 생성**

### 컨테이너 생성 및 진입

먼저 Ubuntu 기반의 Docker 컨테이너를 생성하고 실행:

```bash
docker run -it --name ubuntu-wordpress -p 8080:80 ubuntu:latest
```

컨테이너가 실행되면 내부로 들어가게 돼. 만약 컨테이너를 생성한 후 다시 진입하려면:

```bash
docker exec -it ubuntu-wordpress bash
```

---

## 2. **필요한 패키지 설치**

컨테이너 내부에서 아래 명령어로 Apache, PHP, MariaDB를 설치:

```bash
apt-get update
apt-get install -y apache2 php php-mysql mariadb-server curl
```

---

## 3. **MariaDB 설정**

MariaDB 서비스를 시작하고 데이터베이스를 설정:

```bash
service mariadb start

# MariaDB 설정
mysql -uroot <<EOF
CREATE DATABASE wp_database;
CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'wp_password';
GRANT ALL PRIVILEGES ON wp_database.* TO 'wp_user'@'localhost';
FLUSH PRIVILEGES;
EOF
```

이제 `wp_database` 데이터베이스와 `wp_user` 사용자가 생성되었어.

---

## 4. **WordPress 설치**

WordPress를 다운로드하고 Apache 서버 디렉토리에 배치:

```bash
curl -o wordpress.tar.gz https://wordpress.org/latest.tar.gz
tar -xzf wordpress.tar.gz -C /var/www/html
rm wordpress.tar.gz
chown -R www-data:www-data /var/www/html/wordpress
chmod -R 755 /var/www/html/wordpress
```

---

## 5. **Apache 서버 시작**

Apache 서버를 시작:

```bash
service apache2 start
```

---

## 6. **WordPress 초기 설정**

1. 브라우저에서 `http://<서버 IP>:8080/wordpress`에 접속.
2. WordPress 설치 화면에서 데이터베이스 정보를 입력:
    - **데이터베이스 이름**: `wp_database`
    - **사용자 이름**: `wp_user`
    - **비밀번호**: `wp_password`
    - **데이터베이스 호스트**: `localhost`
3. 설정을 완료하고 관리자 계정을 생성.

---

## 7. **컨테이너 유지 및 관리**

### 컨테이너 종료 후 재시작

컨테이너를 중지하거나 재시작하려면:

```bash
docker stop ubuntu-wordpress
docker start ubuntu-wordpress
```

### 컨테이너 재진입

컨테이너 내부로 다시 접속하려면:

```bash
docker exec -it ubuntu-wordpress bash
```

---

## 장단점 분석

### 장점

- 하나의 컨테이너로 관리가 단순해짐.
- 설정 및 리소스 사용을 통합하여 관리 가능.

### 단점

- 한 컨테이너에서 두 가지 서비스(MariaDB, Apache)가 실행되므로 충돌 가능성 증가.
- 컨테이너가 중지되면 WordPress와 데이터베이스가 모두 다운됨.

---

이 방법으로 Ubuntu 기반의 단일 컨테이너에서 WordPress와 MariaDB를 실행할 수 있어. 추가 질문이 있으면 알려줘! 😊

![[Pasted image 20241206115921.png]]