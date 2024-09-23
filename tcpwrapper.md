- host.allow, host.deny 두 파일을 활용해서 호스트 서비스에 접근하는 것을 허용 또는 거부 하는 기능
- [관련자료](https://dev-jaguar.tistory.com/entry/Linux-TCP-Wrapper-%EC%84%A4%EC%A0%95-hostsallow-hostsdeny)

```sh
vi /etc/host.deny
```
```sh
ALL:ALL # 모든 클라이언트에서 들어오는 모든 서비스 패킷은 거부
sshd:192.168.1.8 # 192.168.1.8에서 접속하는 ssh 패킷은 거부
httpd:192.168.0.0/255.255.0.0 # 192.169.0.0 네트워크 대역의 http 접속을 거부
```
- 허용할 경우 host.allow에 정책 설정

