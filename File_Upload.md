![[Pasted image 20241008092416.png]]
![[Pasted image 20241008092327.png]]![[Pasted image 20241008092443.png]]
![[Pasted image 20241008092351.png]]
![[Pasted image 20241008092337.png]]
![[Pasted image 20241008092504.png]]
- 업로드 되는 파일에 대한 검증이 없기에 파일 업로드에 취약점이 발생한다.


medium
![[Pasted image 20241008092654.png]]
- JPEG PNG 파일만 올릴 수 있다고 한다.
- [[MIME]] 라고 하는데 브라우저가 확장자를 인식할 수 있도록 개발자가 관리하는 내용에 의해 파일을 인식한다.
- MIME를 속인다면 원하는 파일을 업로드 할 수 있을 것 같다.
![[Pasted image 20241008093247.png]]![[Pasted image 20241008093312.png]]
- 확장자가 바뀌어도 코드는 유지된다.

![[Pasted image 20241008093424.png]]
- 업로드 되었다.
![[Pasted image 20241008093501.png]]
- 이렇게 명령어를 넣으면 실행할 수 있을까?
![[Pasted image 20241008093528.png]]
- 실행은 안된다.

- 프록시를 사용하면 실행할 수 있을 것 같다.

![[Pasted image 20241008094116.png]]
- 파일을 업로드할 때 intercept 된 내용이다.
- 파일 이름을 .php로 바꾼다.![[Pasted image 20241008094139.png]]
- 이후 패킷을 전달하면 파일이름이 바뀌어 업로드 된다.![[Pasted image 20241008094509.png]]
![[Pasted image 20241008094602.png]]
- 업로드 타입은 MIME 에서 정의되기 때문에 사용자가 임의로 확장자만 맞춰서 업로드하는 것은 막을 수 없다.

Hight
![[Pasted image 20241008094919.png]]
- 버퍼에서 파일 이름을 변경해도 업로드 되지 않는다.
![[Pasted image 20241008095004.png]]
- uploaded_ext: 파일의 확장자
- 확장자를 명확하게 지정해서 업로드 시 .php 같이 명칭을 바꾸는 것이 불가능해 졌다.
- 하지만 [[메타 데이터]]를 수정해서 업로드 하면 우회할 수 있을 것 같은데??
- 아무 이미지를 다운로드 받는다.![[Pasted image 20241008100756.png]]
- 다운받은 이미지는 업로드가 가능한 것을 확인![[Pasted image 20241008100844.png]]
- exif tool 설치
- [[exiftool]] 파일경로 > 메타데이터 확인 가능![[Pasted image 20241008101004.png]]
- 기존의 메타 데이터(Encoding Process)를 조작해 php 코드를 넣을 수 있다.![[Pasted image 20241008101613.png]]
- 