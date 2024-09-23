- CentOS 에서는 firewalld 를 이용해 접근 제어를 하기 때문에 iptables를 사용하지 않게 되었다.
- 기존에 firewalld를 사용하고 있다면 둘 중 하나만 활성화 하여 사용해야 한다.
- [관련자료](https://linuxstory1.tistory.com/entry/iptables-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%B0%8F-%EC%98%B5%EC%85%98-%EB%AA%85%EB%A0%B9%EC%96%B4)

**설치**
```sh
dnf install -y iptables-services iptables-utils
systemctl start iptables
systemctl enable iptables
```

**기존 서비스 비활성화**
```sh
systemctl stop firewalld
systemctl disable firewalld
```

**Chain(zone) 설정 확인**
```sh
iptables -L
```
```sh
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
ACCEPT     icmp --  anywhere             anywhere
ACCEPT     all  --  anywhere             anywhere
ACCEPT     tcp  --  anywhere             anywhere             state NEW tcp dpt:ssh
REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination
REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```

**정책 추가**
```
iptables -A INPUT -s 192.168.1.8 -j DROP
```
- 출발지(192.168.1.8)에서 들어오는 패킷은 DROP한다.
- IP는 대역으로 설정가능(192.168.0.0/16)
- 