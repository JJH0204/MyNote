![[Pasted image 20241008103744.png]]
- (수동점검 , 자동점검) 두 방법이 있다.

![[Pasted image 20241008104030.png]]![[Pasted image 20241008104042.png]]
- 잘못된 구문을 입력하면 syntax 에러를 출력 > sql injection에 반응 하는 것을 확인
![[Pasted image 20241008104154.png]]
- 0 을 입력을 통해 해당되는 sql 조건 문을 확인
![[Pasted image 20241008104226.png]]
![[Pasted image 20241008104403.png]]
- 1~5까지 입력을 허용
![[Pasted image 20241008104443.png]]![[Pasted image 20241008104508.png]]
- 의도적으로 잘못된 구문 입력
![[Pasted image 20241008104523.png]]![[Pasted image 20241008104550.png]]
- 의도적으로 참이 되는 구문을 입력
![[Pasted image 20241008104614.png]]![[Pasted image 20241008104625.png]]
- 주석을 넣으니 다른 계정 정보도 확인할 수 있게된다.
- sql 문을 잘 설정하면 공격자가 원하는 정보를 얻을 수도 있을 것 같다.
- 