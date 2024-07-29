>[!Note]
>파일 시스템이나 저장 장치를 특정 디렉터리에 연결하여 그 내용을 접근 가능하게 하는데 사용된다.

## 기본 사용 방법
- **파일 시스템 목록 확인**:
    
    mount
    
    이 명령어는 현재 시스템에 마운트된 모든 파일 시스템을 보여줘.
    
- **특정 파일 시스템 목록 확인**:
    
    mount -t ext4
    
    특정 유형(ext4)의 파일 시스템만 나열해줘​ ([phoenixNAP | Global IT Services](https://phoenixnap.com/kb/linux-mount-command))​.
    
- **파일 시스템 마운트**:
    
    sudo mount /dev/sdb1 /mnt/media
    
    이 명령어는 `/dev/sdb1` 장치를 `/mnt/media` 디렉터리에 마운트해. 추가 옵션이 필요하면 `-o` 플래그를 사용할 수 있어:
    
    mount -o [options] [device] [dir]
    
- **/etc/fstab 파일을 이용한 마운트**: `/etc/fstab` 파일은 시스템 장치의 마운트 위치와 옵션을 설명하는 라인을 포함하고 있어. 여기에는 내부 장치나 네트워크 공유를 정의할 수 있어:
    
    <file system> <mount point> <type> <options> <dump> <pass>
    
    예를 들어, 다음과 같은 라인을 추가할 수 있어:
    
    /dev/sdb1 /mnt/media ext4 defaults 0 0
    
    이를 통해 시스템 부팅 시 자동으로 마운트할 수 있다.
    

### 실용적인 예시

- **USB 드라이브 마운트**:
    
    sudo mount /dev/sdX1 /mnt/usb

    
    여기서 `/dev/sdX1`은 USB 드라이브를 나타내고, `/mnt/usb`는 마운트 지점을 나타내.
    
- **네트워크 공유(NFS) 마운트**:
    
    sudo mount -t nfs server:/path/to/share /mnt/nfs

    
    `server`는 NFS 서버의 호스트명이나 IP 주소고, `/path/to/share`는 공유 디렉터리야. `/mnt/nfs`는 로컬 시스템에서 사용할 마운트 지점이야
    
- **가상 파일 시스템(tmpfs) 마운트**:
    
    sudo mount -t tmpfs tmpfs /mnt/ramdisk

    
    이 명령어는 `tmpfs` 파일 시스템을 `/mnt/ramdisk`에 마운트해, 메모리에 저장된 데이터를 빠르게 접근할 수 있어


### 마운트 해제

파일 시스템을 더 이상 사용할 필요가 없으면 안전하게 해제해야 해:

sudo umount /mnt/usb


이렇게 `mount` 명령어는 리눅스에서 파일 시스템을 효율적으로 관리하고, 다양한 저장 장치와 네트워크 리소스를 통합하는 데 필수적인 도구이다.