# \[1] 정보 수집 (Scaning)
> [!Note]
> Attacker
> - ip: 192.168.56.105/24
> 
> victim
> - 같은 동일한 네트워크 대역에 있다고 가정하고 진행
## \[1-1] Victim 대상 찾기
---
> netdiscover, nmap 등 scaning tool을 활용해 피해자 PC의 IP를 찾는다.
- `nmap 192.168.56.0/24`![[{502F8A71-3DD0-4168-9BC5-DEA47F1F3170}.png]]
- `netdiscover -r 192.168.56.0/24`![[{DF454A6C-E996-4D79-91DC-61722923A87A}.png]]

> [!Note]
> Attacker
> - ip: 192.168.56.105/24
> 
> victim
> - ip: 192.168.56.104/24
> - ssh, http, https 서비스가 동작 중임을 확인했다.
> - ssh 접속을 먼저 시도하는 것은 흔적(Log)을 남길 수 있기 때문에 지양하고,
>   ip 를 활용해 web 접속을 시도한다.

## \[1-2] Browser 접속
---
> victim server에서 서비스 중인 웹 서비스를 활용해 접속을 시도한다.
- browser 접속: `http://192.168.56.104/`![[{A4990424-8C50-484E-B93C-5ED7441EF255}.png]]
- browser 접속: `https://192.168.56.104/`![[{9FDE5F88-F1C5-4AF5-95DE-47F74DE38D0A}.png]]
> [!Note]
> `http://(또는 https://)ip/`를 활용한 웹 서비스 접속이 원활하지 않다.
> 다른 접속 방법을 찾아야 한다.

### https 프로토콜의 특성 활용한 도메인 이름 찾기
- 브라우저의 기능을 활용해 https의 설정(key)를 볼 수 있다.![[{B2B64A99-A38F-4882-B150-5AA6D6654A6F}.png]]![[{E29A501C-1B1D-43A1-A18D-EA84783989D1}.png]]![[{E607599B-3B8D-45DF-A199-C803C42EA692}.png]]
- 찾은 도메인 이름으로 사이트에 접속할 수 있도록 host파일 수정한다.
	- `sudo vi /etc/hosts`
	- `192.168.56.104 earth.local`, `192.168.56.104 terratest.earth.local` 추가
	- 저장
- 도메인 이름으로 웹 서비스에 접속한다.![[{DA2C17DA-7807-4E49-8AA6-BB630C44C4E4}.png]]![[{95FDB3AA-A84A-4E4C-9BDA-37FD1D21A23A}.png]]
> [!Note]
> https ssl key 설정을 통해 알아낸 도메인 이름(earth.local/terratest.earth.local)으로 웹 서비스 접속에 성공했다.
> `http://earth.local/`, `http://terratest.earth.local/`, `https://earth.local/` > 웹 서비스 페이지로 접속
> `https://terratest.earth.local/` > 더미 페이지로 접속

### 서비스 분석
- 실제 기능을 사용(또는 F12, 개발자 툴을 활용)하며 서비스 특징을 분석한다.
- 텍스트 입력
  ![[Pasted image 20240926085614.png]]
  지구로 보낼 메시지를 입력할 수 있는 입력 칸이 활성화 되어 있다.
- 암호 입력
  ![[Pasted image 20240926090043.png]]
- 전송 버튼
  ![[Pasted image 20240926090126.png]]
- 이전 메시지 기록![[Pasted image 20240926090147.png]]
  지구로 보내는 메시지는 함께 입력한 암호와 조합해 암호화하여 저장된다.
  사이트에서 사용하고 있는 암호화 로직이 무엇인지 찾을 필요가 있어 보인다.

### dirb 툴을 활용한 scaning
- dirb tool
- 웹 페이지에 생성될 가능성이 있는 모든 디렉토리 이름을(웹 개발자가 서비스를 구축할 때 자주 사용하는 디렉토리 이름을) 대입하여 접속 가능 여부를 출력
- 