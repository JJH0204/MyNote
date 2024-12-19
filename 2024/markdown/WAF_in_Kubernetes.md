윈도우 호스트 머신에서 쿠버네티스 클러스터를 운영하며, 워커 노드에서 Docker 이미지로 Django 웹 서버를 구동 중일 때, 프록시 서버를 통해 WAF(Web Application Firewall)를 설정하려면 다음 단계를 따르면 돼.

**1. 인그레스 컨트롤러(Ingress Controller) 설정**

쿠버네티스에서 인그레스는 클러스터 외부에서 내부 서비스로의 HTTP 및 HTTPS 경로를 관리하는 리소스야. 인그레스 컨트롤러는 이러한 인그레스 리소스를 처리하는 컴포넌트로, Nginx 인그레스 컨트롤러가 널리 사용돼.

- **Nginx 인그레스 컨트롤러 설치**:
    
    - Helm을 사용하여 설치할 수 있어.
        
        ```bash
        helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
        helm install ingress-nginx ingress-nginx/ingress-nginx
        ```
        
    - 설치 후, 인그레스 컨트롤러가 올바르게 동작하는지 확인해.
        
        ```bash
        kubectl get pods -n ingress-nginx
        ```
        

**2. ModSecurity를 통한 WAF 설정**

Nginx 인그레스 컨트롤러는 ModSecurity를 통합하여 WAF 기능을 제공할 수 있어.

- **ModSecurity 활성화**:
    
    - 인그레스 컨트롤러의 ConfigMap을 수정하여 ModSecurity를 활성화해.
        
        ```yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: nginx-configuration
          namespace: ingress-nginx
        data:
          enable-modsecurity: "true"
          enable-owasp-modsecurity-crs: "true"
        ```
        
    - 설정 적용 후, 인그레스 컨트롤러를 재시작해.
        
        ```bash
        kubectl rollout restart deployment ingress-nginx-controller -n ingress-nginx
        ```
        

**3. 인그레스 리소스 생성 및 Django 서비스 연결**

Django 웹 서버를 외부에 노출하기 위해 인그레스 리소스를 생성하고, 이를 통해 트래픽을 관리해.

- **인그레스 리소스 예시**:
    
    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: django-ingress
      namespace: your-namespace
      annotations:
        nginx.ingress.kubernetes.io/enable-modsecurity: "true"
        nginx.ingress.kubernetes.io/enable-owasp-modsecurity-crs: "true"
    spec:
      rules:
        - host: your-domain.com
          http:
            paths:
              - path: /
                pathType: Prefix
                backend:
                  service:
                    name: django-service
                    port:
                      number: 80
    ```
    
    - `your-namespace`를 실제 네임스페이스로, `your-domain.com`을 실제 도메인으로, `django-service`를 Django 서비스 이름으로 변경해.

**4. WAF 규칙 구성 및 테스트**

ModSecurity는 OWASP Core Rule Set(CRS)을 기본으로 제공하지만, 필요에 따라 사용자 정의 규칙을 추가할 수 있어.

- **규칙 구성**:
    
    - ConfigMap에 추가 규칙을 정의하거나, 별도의 파일로 관리하여 마운트할 수 있어.
- **테스트**:
    
    - WAF가 올바르게 동작하는지 확인하기 위해 다양한 공격 시나리오를 시뮬레이션하고, 로그를 통해 차단 여부를 확인해.

**참고 자료**

- [쿠버네티스에서 윈도우 컨테이너 스케줄링을 위한 가이드](https://kubernetes.io/ko/docs/concepts/windows/user-guide/)
    
- [쿠버네티스에서 윈도우 컨테이너 스케줄링을 위한 가이드](https://k8s-docs.netlify.app/ko/docs/setup/production-environment/windows/user-guide-windows-containers/)
    
- [Kubernetes WAF: 4 Types of K8s WAFs and How to Choose](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-waf/)
    

이러한 단계를 따르면, 윈도우 기반 쿠버네티스 클러스터에서 Django 웹 서버 앞단에 프록시 서버를 구성하고, WAF를 설정하여 보안을 강화할 수 있어