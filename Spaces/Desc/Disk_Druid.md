Disk Druid는 리눅스 시스템, 특히 레드햇(Red Hat)과 페도라(Fedora) 설치 과정에서 사용되는 그래픽 사용자 인터페이스(GUI) 기반의 디스크 파티셔닝 도구입니다. 이 도구는 사용자가 하드 드라이브를 파티셔닝하는 과정을 쉽게 도와주며, 파티션 추가, 수정, 삭제 등의 작업을 수행할 수 있습니다​ ([Everything Linux 101 blog](https://everything-linux-101.com/linux-fdisk-parted-and-disk-druid-hard-disk-partitioning-in-red-hat-linux-linux-commands-training/))​​ ([Fedora People](https://jsmith.fedorapeople.org/drafts/install-guide-en_US/sn-disk-druid.html))​.

Disk Druid는 파티션을 생성하거나, 기존 파티션의 크기를 조정하고, 파일 시스템 타입을 변경하는 등의 작업을 수행할 수 있습니다. 특히 LVM(Logical Volume Manager) 설정이나 소프트웨어 RAID 구성도 지원하여 데이터 저장을 더 확장성 있고 안정적으로 관리할 수 있게 돕습니다​ ([Everything Linux 101 blog](https://everything-linux-101.com/linux-fdisk-parted-and-disk-druid-hard-disk-partitioning-in-red-hat-linux-linux-commands-training/))​​ ([Fedora People](https://jsmith.fedorapeople.org/drafts/install-guide-en_US/sn-disk-druid.html))​.

Disk Druid의 사용은 주로 설치 과정에서 이루어지며, 'Add', 'Edit', 'Delete' 버튼을 사용하여 파티션을 관리합니다. 파티션을 추가할 때는 새 파티션에 대한 세부 사항을 입력하고, 파티션 타입과 크기, 마운트 포인트 등을 설정할 수 있습니다​ ([Everything Linux 101 blog](https://everything-linux-101.com/linux-fdisk-parted-and-disk-druid-hard-disk-partitioning-in-red-hat-linux-linux-commands-training/))​.

이 도구는 파티션 테이블에 변화를 주기 전까지는 변경사항이 메모리에만 저장되기 때문에, 'Write' 버튼을 눌러 디스크에 변경사항을 적용해야 합니다. 만약 설정을 저장하지 않고 종료하려면, 'Quit' 버튼을 사용하여 변경사항을 저장하지 않고 나올 수 있습니다​ ([Everything Linux 101 blog](https://everything-linux-101.com/linux-fdisk-parted-and-disk-druid-hard-disk-partitioning-in-red-hat-linux-linux-commands-training/))​.

Disk Druid는 parted 유틸리티의 프런트 엔드로 작동하며, 사용자가 그래픽 인터페이스를 통해 파티션을 쉽게 관리할 수 있도록 돕습니다​ ([Massachusetts Institute of Technology](https://web.mit.edu/~linux/redhat/redhat-5.2/i386/doc/rhmanual/manual/doc033.htm))​. 이러한 특성 덕분에 리눅스 시스템 관리자 뿐만 아니라 일반 사용자도 디스크 관리 작업을 보다 편리하게 수행할 수 있습니다.

레드햇이나 페도라 같은 배포판을 사용할 때 Disk Druid를 활용하여 효과적으로 디스크 파티션을 관리할 수 있으며, 더 많은 정보와 사용법을 웹에서 찾아볼 수 있습니다.