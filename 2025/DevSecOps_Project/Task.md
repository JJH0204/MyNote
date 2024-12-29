sudo apt install iputils-ping
vim /etc/netplan/
dhcp: no
addresses:
  - 192.168.1.100-105/16
gateway4: 192.168.0.1
nameservers:
  addresses: [8.8.8.8]

~~쿠버네티스 환경에 웹 서비스 와 ELK Stack + Jenkins 구동 시키기~~

