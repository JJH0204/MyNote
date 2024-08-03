# 리눅스 자동 업데이트 끄기
	`gsettings set org.gnome.software download-updates false`
	`systemctl disable dnf-makecache.service`
	`systemctl disable dnf-makecache.timer`

# selinux 설정 끄기
### selinux 설정 확인
	`sestatus`

### 텍스트 파일 수정
	`vi /etc/sysconfig/selinux`
	disavled로 설정 수정

### 명령어로 설정 끄기
	grubby --update-kernel ALL --args selinux=0

### 명령어로 설정 켜기
	grubby --update-kernel ALL --remove-args selinux

# IP 변경
### 설정파일 경로
	`/etc/NetworkManager/system-connections/enp0s3.nmconnection`

### 랜카드 끄기
	nmcli connection down enp0s3

### 랜카드 켜기
	nmcli connection up enp0s3
	