# 1. 코드 변경 감지
- Github Webhook
- 개발자(코드커밋/푸시)>Github(변경사항 알림)>Jenkins
# 2. Jenkins 파이프라인
- 관리자 역할
## 2.1. SonarQube
- 코드 품질 검사(버그 찾기/취약점 검사/코드 스타일 검사)
## 2.2. Docker Image 빌드
- 애플리케이션과 필요한 모든 것을 하나의 패키지로 만듦(코드/실행환경/설정)
- 생성한 이미지는 주로 Docker Hub에 저장됨
## 2.3. Kubernetes 매