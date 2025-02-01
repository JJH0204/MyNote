### 대시보드 배포

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

### 관리자 계정 생성
```
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
EOF
```
NodePort로 서비스 변경
```
kubectl patch svc kubernetes-dashboard -n kubernetes-dashboard -p '{"spec": {"type": "NodePort"}}'
```
서비스 상태 확인(노드포트 확인)
```
kubectl get svc -n kubernetes-dashboard
```
![[Pasted image 20241203163841.png]]
접근 토큰 생성
```
kubectl -n kubernetes-dashboard create token admin-user
```
```
eyJhbGciOiJSUzI1NiIsImtpZCI6Inh0bDhiU0t3QUdnX0R6QlpGMGNzRW9yYWo3TTVaMUw5WmNfbTVhd0lyd2sifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzMzMjE1MTMyLCJpYXQiOjE3MzMyMTE1MzIsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiOGYxMWY2NzktNDhlZC00YjE3LWJhZjMtY2IxNzRjMjFiMTY4Iiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJhZG1pbi11c2VyIiwidWlkIjoiYWFjZWFjZjItYjFkOS00MmE4LTg1OGQtZDUxYmY3NTYwYmUyIn19LCJuYmYiOjE3MzMyMTE1MzIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlcm5ldGVzLWRhc2hib2FyZDphZG1pbi11c2VyIn0.QGuAXMyHfh8MKKjkBq0HF7MSbQtgy1H05p9TWmi8l9wJj20_zg3tfcY_VlJZTimZwFpE7rSEtwbOtOkU8iG_oCQJDSl2yrchTdHVi4CQobe_m_J6g0A1IbtKKJk1rMlZ2FQVCgAHboCRpi1vYVLMv7SRMkTdKDeOKP80pSEaZkvA6fKy9mwpmZlyLN8BzvAEP-bqBBMH8qo00ikdu4qTLSAEwjFsuMPfjrlr_ygNLZS_g6_tuUAC9Ge17NxUDpWSWWBiIJwUD2HOuUmWx-nxKi0Egg9eJHlCDbT0KOuoBrZJHQN4PkSr5fMUSMQi8tAxTVm9Pgd-GtCFq_G4Nobpbw
```
브라우저 접속
`https://192.168.1.117:30164` 
`https://192.168.1.116:30164` 
![[Pasted image 20241203164252.png]]