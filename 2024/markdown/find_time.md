- atime(access time): 
  vi, cat 등의 명령어를 통해 파일을 확인한 시간, ls -lu
- mtime(modification time): 
  파일의 수정한 시간, ls -l
- ctime(change time): 
  파일의 값(권한, 사이즈, 속성 등)을 수정한 시간, ls -lc

find 시간 옵션
- mtime
	- find ~~ mtime -3: 3일전(72시간)~현재시간
	- find ~~ mtime 3: 4일째(96시간)~3일전(72시간)
	- find ~~ mtime +3: 4일(96시간)전 모든 과거
- mmin