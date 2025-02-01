- 우분투 리눅스 22.04에 [도커 엔진 설치](https://docs.docker.com/engine/install/ubuntu/)후 [도커](Spaces/Desc/Docker.md)를 사용

# 도커 설치
---
- 아래 명령어를 순서대로 실행하여 도커 엔진을 설치한다.
```
$ sudo apt-get update
$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg
```

```
$ sudo mkdir -m 0755 -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```
$ echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# 도커 설치 확인
---
```
$ sudo docker run hello-world
```
![[Pasted image 20240806142939.png]]
- Hello from Docker! 가 출력되면 도커 엔진이 설치된 것이다.

# [[Docker_Build]]
---

