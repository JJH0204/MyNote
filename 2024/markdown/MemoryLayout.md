> [!메모리 레이아웃(Memory Layout)이란]
> 프로세스 [가상 메모리(Virtual Memory)](VirtualMemory.md)의 구성을 말한다.
> 프로그램을 실행하면 운영체제에게 사용 가능한 메모리 공간을 할당해 준다.
> 컴퓨터 과학에서는 이 공간을 가상 메모리라고 부른다.

- 운영체제는 프로그램의 정보를 참조하여 프로그램에 저장된 데이터가 적절한 영역에 저장되게 한다.
- 프로세스가 사용할 가상 메모리를 용도 별로 구획하고, 프로세스가 사용하는 데이터를 적절한 구획에 저장한다.
- 유사한 데이터를 모아 놓기 때문에 운영체제는 각 구획에 적절한 권한을 부여할 수 있으며, 개발자는 프로세스의 메모리를 더 직관적으로 이해할 수 있다.

# [윈도우 프로세스의 메모리 레이아웃](WindowsMemoryLayout.md)
