# Docker Hub

**Docker Hub**는 도커의 공식 레지스트리로, 도커 이미지를 저장하는 저장소입니다. Docker Hub 사용자는 이미지를 자유롭게 업로드하거나 다운 받아 사용합니다. 다른 사용자가 업로드한 이미지 뿐만 아니라 도커에서 제공하는 공식 이미지를 사용할 수 있다는 것도 편리합니다. 공식 이미지는 기본 OS(Linux, CentOS 등) 이미지나, 특정 프로그래밍 언어의 개발 환경 등을 제공합니다. 비공개 이미지를 업로드하여 개인적으로 사용하거나 팀끼리 공유할 수도 있습니다.

![](https://dreamhack-lecture.s3.amazonaws.com/media/968ff0ffd16646ad8ac0e5acde6ac81ad3bcd396d0c2a935bef36b894ec85dbd.png)

# Docker Hub 이미지 업로드

Docker Hub를 이용하면 Dockerfile이 아닌 이미지 그 자체를 보관하고 공유할 수 있습니다. 자신만의 문제 풀이 환경을 구축해 두고 사용하고 싶거나, 워게임을 직접 제작하여 다른 사람들과 공유하고 싶은 경우 등에 유용합니다. 그럼 Docker Hub 레포지토리에 이미지를 업로드하는 방법을 소개하겠습니다.

## 1. `docker login`

Docker Hub에 로그인합니다.
```
user@user-VirtualBox:~$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: dreamhackofficial
Password: 
WARNING! Your password will be stored unencrypted in /home/user/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
user@user-VirtualBox:~$ 
```
## 2. `docker build -t [사용자]/[레포지토리명]:[TAG] [Dockerfile 경로]`

Dockerfile을 이용하여 이미지를 빌드합니다. 이미지 이름은 `[사용자]/[레포지토리명]:[TAG]` 형식으로 작성합니다. `dreamhackofficial/exercise-docker:1`을 빌드하겠습니다.
```
user@user-VirtualBox:~/Desktop/ex-docker$ docker build -t dreamhackofficial/exercise-docker:1 .
[+] Building 1.8s (18/18) FINISHED                                              
 => ...생략...                                
 => exporting to image                                                     0.0s
 => => exporting layers                                                    0.0s
 => => writing image sha256:9d201c4de2b62519383058265e31669b167c422502643  0.0s
 => => naming to docker.io/dreamhackofficial/exercise-docker:1             0.0s
user@user-VirtualBox:~/Desktop/ex-docker$ docker images
REPOSITORY                          TAG       IMAGE ID       CREATED         SIZE
dreamhackofficial/exercise-docker   1         9d201c4de2b6   6 hours ago     122MB 
```

## 3. `docker push [사용자]/[레포지토리명]:[TAG]`

레포지토리에 이미지를 업로드합니다.
```
user@user-VirtualBox:~/Desktop/ex-docker$ docker push dreamhackofficial/exercise-docker:1
The push refers to repository [docker.io/dreamhackofficial/exercise-docker]
5f70bf18a086: Pushed 
4958ae9bc6ae: Pushed 
4b9b1ff53c81: Pushed 
5d89cab1df92: Pushed 
557171cb0464: Pushed 
e04c36b2101d: Pushed 
c8fe798e77a1: Pushed 
714c2f225f87: Pushed 
60ac9e1e9e64: Pushed 
3cc715e175c0: Pushed 
0482f429f461: Pushed 
b93c1bd012ab: Mounted from library/ubuntu 
1: digest: sha256:b0288419aa476a56c62d380f41c384f345405b41f7cffffa41aa9c1860fe4617 size: 2818
user@user-VirtualBox:~/Desktop/ex-docker$
```

Docker Hub의 레포지토리에 이미지가 업로드된 모습입니다. 우측의 명령어를 복사하여 누구나 이미지를 다운받을 수 있습니다.

![](https://dreamhack-lecture.s3.amazonaws.com/media/4e0adcfd919718cc8915ace826f825b3bce348d9c6738085b076499e6fcea17a.png)

![](https://dreamhack-lecture.s3.amazonaws.com/media/82ad57715d32244898c2e9cab793fe7bb45344715bebba5f3dd9b20e4317f3b3.png)

# Docker Hub 이미지 다운로드

Docker Hub에서 이미지는 레포지토리에 보관됩니다. `dreamhackofficial/exercise-docker` 레포지토리에서 앞서 업로드했던 이미지를 다운받을 수 있습니다.

## `docker pull`

`docker pull` 명령어는 Docker Hub에서 이미지를 다운로드합니다. 원하는 레포지토리와 태그를 클릭하여 제공되는 `docker pull` 명령어를 사용합니다.

![](https://dreamhack-lecture.s3.amazonaws.com/media/35e1bd8493e44535b0448761e98dcd8d81ebae728cd1eb6a06974040c54623a2.png)

아래는 `dreamhackofficial/exercise-docker` 레포지토리의 Tag 1 이미지를 성공적으로 다운로드한 모습입니다. 해당 이미지로 컨테이너를 생성하고 실행하여 사용할 수 있습니다.
```
user@user-VirtualBox:~/Desktop/ex-docker$ docker pull dreamhackofficial/exercise-docker:1
1: Pulling from dreamhackofficial/exercise-docker
2ab09b027e7f: Already exists
dae082a9e205: Pull complete
ab969aeba5d6: Pull complete
cff12ac5c589: Pull complete
3f1e6d67fba6: Pull complete
818905cc8cec: Pull complete
09532c870255: Pull complete
3eda49607555: Pull complete
a88f78b4c1db: Pull complete
4ccef51b986d: Pull complete
5cf58cbc005e: Pull complete
4f4fb700ef54: Pull complete
Digest: sha256:b0288419aa476a56c62d380f41c384f345405b41f7cffffa41aa9c1860fe4617
Status: Downloaded newer image for dreamhackofficial/exercise-docker:1
docker.io/dreamhackofficial/exercise-docker:1
```