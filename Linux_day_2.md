# 리눅스 앱 자동 업데이트 끄기
`gsettings set org.gnome.software download-updates false`
`systemctl disable dnf-makecache.service`
`systemctl disable dnf-makecache.timer`

# selinux 설정끄기
### selinux 설정 확인
`sestatus`
