>[!Note]
>파일 시스템이나 저장 장치를 특정 디렉터리에 연결하여 그 내용을 접근 가능하게 하는데 사용된다.

# mount 마운트
---
윈도우의 PnP(Plug and Play)방식과 달리 리눅스는 연결 후 직접 마운트 과정을 거쳐야 사용할 수 있다.
- 마운트: 물리적인 장치를 특정한 디렉토리에 연결 시켜주는 과정

>[!장치 연결]
>mount /dev/cdrom /mnt/dvd
>mount \[장치 이름] \[연결할 디렉토리 이름]

>[!장치 해제]
>umount /dev/cdrom
>umount \[장치 이름]

- 정상적인 장치 연결과 해제를 위해서 연결할 디렉토리 밖에서 작업을 수행하는 것이 좋다.
- 마운트 하는 것으로 기존에 저장된 파일이 삭제되거나 하지 않는다.

# fdisk -l
---
![[Pasted image 20240810171616.png]]
- 연결된 저장 장치를 찾는 방법
- 

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

### 주요 옵션

- **-t**: 파일 시스템 유형을 지정합니다. 예를 들어, ext4, nfs, iso9660 등을 사용할 수 있습니다.
    `mount -t ext4 /dev/sda1 /mnt`
    
- **-o**: 여러 마운트 옵션을 지정할 수 있습니다. 옵션은 쉼표로 구분해 나열할 수 있습니다.
    
    - **ro**: 읽기 전용으로 마운트합니다.
        `mount -o ro /dev/sda1 /mnt`
        
    - **rw**: 읽기/쓰기로 마운트합니다.
        `mount -o rw /dev/sda1 /mnt`
        
    - **noatime**: 파일 접근 시간을 업데이트하지 않습니다. 성능을 향상시킬 수 있습니다.
        
        `mount -o noatime /dev/sda1 /mnt`
        
    - **async**: 비동기식으로 파일 시스템 동작을 설정합니다.
        
        `mount -o async /dev/sda1 /mnt`
        
    - **sync**: 동기식으로 파일 시스템 동작을 설정합니다.
        
        `mount -o sync /dev/sda1 /mnt`
        
    - **remount**: 이미 마운트된 파일 시스템의 옵션을 변경합니다.
        `mount -o remount,rw /mnt`
        
    - **loop**: ISO 파일 같은 디스크 이미지 파일을 마운트할 때 사용합니다.
        
        `mount -o loop image.iso /mnt`
        
- **-a**: `/etc/fstab` 파일에 정의된 모든 파일 시스템을 마운트합니다.
    `mount -a`
    
- **-r**: 읽기 전용으로 마운트합니다. 이는 `-o ro`와 동일합니다.
    `mount -r /dev/sda1 /mnt`
    
- **-n**: `/etc/mtab` 파일을 업데이트하지 않고 마운트합니다. 시스템 관리 작업 중에 유용할 수 있습니다.
    `mount -n /dev/sda1 /mnt`
    
- **-v**: 마운트 작업 중에 상세 정보를 출력합니다.
    `mount -v /dev/sda1 /mnt`
    
- **-L**: 볼륨 라벨을 사용하여 마운트할 장치를 지정합니다.
    `mount -L mylabel /mnt`
    

### 예시 명령어

- USB 드라이브 마운트:
    `sudo mount -o rw,async /dev/sdb1 /mnt/usb`
    
- NFS 공유 마운트:
    `sudo mount -t nfs -o rw,vers=4 server:/shared /mnt/nfs`
    
- ISO 파일 마운트:
    `sudo mount -o loop image.iso /mnt/iso`

이렇게 `mount` 명령어는 리눅스에서 파일 시스템을 효율적으로 관리하고, 다양한 저장 장치와 네트워크 리소스를 통합하는 데 필수적인 도구이다.