`Web Application Firewall - 웹 방화벽
웹 서비스가 동작 중인 서버에서 자체적으로 사용할 수 있는 방화벽 어플리케이션

# 준비
## 웹 서비스 활성화
![[Pasted image 20241015143118.png]]

## httpd 모듈 확인
```
httpd -M
```
![[Pasted image 20241015143424.png]]

## mod_security 모듈 설치
```
dnf install -y mod_security
```
![[Pasted image 20241015143541.png]]

## 경로 확인
![[Pasted image 20241015143731.png]]
```
vi ./mod_security.conf
```
![[Pasted image 20241015143818.png]]
```
	SecRuleEngine On           // 설정 적용여부 결정 (비활: Off)
    SecRequestBodyAccess On    // 웹 소스 본문<body>도 점검
    SecRule REQUEST_HEADERS:Content-Type "text/xml" \ 
         "id:'200000',phase:1,t:none,t:lowercase,pass,nolog,ctl:requestBodyProcessor=XML"
    SecRequestBodyLimit 13107200        // 메모리 제안
    SecRequestBodyNoFilesLimit 131072   
    SecRequestBodyInMemoryLimit 131072  
    SecRequestBodyLimitAction Reject    // 메모리 제안을 초과하면 수행할 액션

	SecPcreMatchLimit 1000     //
	
```

# Rules 생성
## 파일 경로
```
/etc/httpd/modsecurity.d
```
![[Pasted image 20241015144534.png]]
## 파일 내용
```
 vi ./local_rules/modsecurity_localrules.conf
```
![[Pasted image 20241015144641.png]]
## crs 링크
https://owasp.org/www-project-modsecurity-core-rule-set/

## Rules 작성
```
SecDefaultAction "탐지되었을 때 기본 액션"
```
```
SecDefaultAction "phase:2,deny,log,status:406"
```
- 차단/로그화/클라이언트 메시지 설정
```
SecRule REQUEST_URI "/etc/passwd" "id:'500001'"
SecRule REQUEST_URI "../../" "id:'500002'"
SecRule ARGS "<[Ss][Cc][Rr][Ii][Pp][Tt]>" "id:'500003'" # XSS 공격 탐지
```
- 차단/탐지 하고 싶은 내용 작성

# 테스트
## 웹 서버 접속
![[Pasted image 20241015152539.png]]
## /etc/passwd
![[Pasted image 20241015152625.png]]
- 406 에러 코드 확인
## ../../
![[Pasted image 20241015152650.png]]
- 406 에러 코드 확인

## /etc/shadow
![[Pasted image 20241015152717.png]]
- 404 에러: 별도의 룰 설정을 하지 않았기 때문에 발생

# 로그 확인
![[Pasted image 20241015152956.png]]
## audit
![[Pasted image 20241015153113.png]]
## debug
![[Pasted image 20241015153226.png]]
- 아직 별 내용이 없다.

# CRS 설정
## 설치
```
dnf install -y mod_security_crs
```
![[Pasted image 20241015153434.png]]
## 설치 경로
![[Pasted image 20241015153502.png]]
```
/usr/share/mod_modsecurity_crs/rules
```
## Rule 확인 (wordpress)
```
vi ./REQUEST-903.9002-WORDPRESS-EXCLUSION-RULES.conf
```
