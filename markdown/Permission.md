> [!NOTE]
> `ls -l` 을 통해 파일/디렉토리의 사용자 권한을 확인할 수 있는데
> 이를 읽고 쓰고 수정하는 방법에 대해서 서술한다.

![[Pasted image 20240729180858.png]]
파일 권한 내용을 보면 순서대로 의미가 부여된다.

| - | 타입 | -:파일, d: 디렉토리, l:링크 |
| :--- | ---- | ---- |
| rw- | 소유자 권한 | r: 읽기, w: 쓰기, x: 실행, - 권한 없음 |
| r-- | 그룹 권한 | r: 읽기, w: 쓰기, x: 실행, - 권한 없음 |
| r-- | 다른 사용자 권한 | r: 읽기, w: 쓰기, x: 실행, - 권한 없음 |

위 이미지의 .hash_history 의 권한 내용을 분석하면 아래와 같다.
- - : 타입은 파일이다.
- rw-: 사용자는 해당 파일을 읽고 쓸 수 있지만, 실행은 불가능하다.
- ---: 그룹에서는 해당 파일에 대한 모든 권한이 없다.
- ---: 다른 사용자 또한 해당 파일에 대한 모든 권한이 없다.

숫자로 표현 가능하다
r = 4
w = 2
x = 1

777 = 모든 사용자가 모든 권한을 가진다.

# 권한 수정 명령어
`chmod [권한레벨] [바꿀파일이름]`
> 예) `chmod 755 sample.txt`

옵션으로 수정가능
> 예) `chmod ugo-r sample.txt`
> 예) `chmod ugo+wx sample.txt`
> u = user
> g = group
> o = other
# 소유자 변경
`chown [계정 이름] [대상파일(디렉토리)이름]`
> 예) `chown jang sample.txt`

`chown .[그룹이름] [대상파일(디렉토리)이름]`
> 예) `chown .buseo4 jang1.txt`

소유자와 그룹을 동시에 바꿀 수 있다.
> 예) `chown jang.jang jang1.txt`

디렉토리의 하위 디렉토리 및 하위 파일들까지 한번에 소유자 변경
> 예) `chown -R jang.jang dir`

소유자 변경은 루트 사용자만 가능


# Umask
---
- 파일의 기본 퍼미션 값 : 644
- 디렉토리의 기본 퍼미션 값 : 755
- umask 값에 의해 결정된다.
	- 파일(666) - umask(022) = 644
- umask 값을 누군가 임의로 바꾼다면 보안에 취약한 상황이 발생함으로 주의해야 한다.

# 관리자 권한 관리
---
- [블로그 포스팅](https://velog.io/@lenyleny/Linux-sudosusu-%EC%B0%A8%EC%9D%B4-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%99%80-%EC%B0%A8%EC%9D%B4-rootadminuser-%EC%B0%A8%EC%9D%B4)
- /etc/passwd의 UID, GID를 root와 같은 값을 주었을 때 root와 같은 시스템 권한을 갖는 것을 확인
- Real(RUID, RGID), Effective(EUID, EGID)로 나눠서 계정을 관리한다.

> [!Real/Effective]
> Real: 사용자 식별에 사용하는 아이디(또는 그룹)
> Effective: 사용자의 권한을 식별하는데 사용하는 아이디(또는 그룹)
- 최초 로그인 시에는 두 값이 같다. (SetUIDbit가 설정된 파일을 실행하기 전까지)
- [/etc/sudoers](https://mans-daily.tistory.com/entry/%EB%A6%AC%EB%88%85%EC%8A%A4UbuntuCentOS-etcsudoers-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EC%88%98%EC%A0%95%ED%95%98%EC%97%AC-sudo-%EA%B6%8C%ED%95%9C-%EB%B0%8F-root-%EA%B6%8C%ED%95%9C-%EB%B6%80%EC%97%AC%ED%95%98%EA%B8%B0)

## 특수 권한
- https://blog.naver.com/doctor-kick/222158625480
- https://eunguru.tistory.com/115
### SetUIDbit
```
-rwsr-xr-x. 1 root root 32656 May 15  2022 /usr/bin/passwd
```
- s: setUIDbit가 설정된 파일이라는 뜻
- 이 파일을 실행할 때만 지정된 사용자의 권한을 잠시 빌린다.(대부분 root)
- 사용자 권한의 s = 4000, 그룹 권한의 s = 2000


## [[Backdoor Attack]]

# 특정 사용자 또는 권한 가진 파일 찾기 
```
find / -user root -perm /4000
```