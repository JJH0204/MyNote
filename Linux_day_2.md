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

# 절대 경로와 상대 경로
- 디렉토리(폴더) 경로를 처음부터 끝까지 모두 작성하는 것 = 절대 경로
	cd /etc/passwd
- 현재 디렉토리(폴더) 기준 목표까지 경로를 표현 = 상대 경로
	cd ../passwd