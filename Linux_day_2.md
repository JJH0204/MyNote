# 리눅스 앱 자동 업데이트 끄기
	`gsettings set org.gnome.software download-updates false`
	`systemctl disable dnf-makecache.service`
	`systemctl disable dnf-makecache.timer`

# selinux 설정끄기
### selinux 설정 확인
	`sestatus`

### 텍스트 파일 수정
	`vi /etc/sysconfig/selinux`
	disavled로 설정 수정

### 명령어로 설정 끄기
	grubby --update-kernel ALL --args selinux=0

### 명령어로 설정 켜기
	grubby --update-kernel ALL --remove-args selinux

