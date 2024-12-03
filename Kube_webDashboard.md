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
eyJhbGciOiJSUzI1NiIsImtpZCI6IjlHTlJVZDk2dmVTR1ZqU1pLVjBVWWhqRUlDUGRHVXk0cmg3MDBRbTVaVG8ifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzMzMjA2NDE0LCJpYXQiOjE3MzMyMDI4MTQsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiMzFkOTNjYzQtMmUxMi00MjAwLWE3NjgtM2VkYzdjZDViYjdiIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJhZG1pbi11c2VyIiwidWlkIjoiMWVkMWZmZjEtYTZlMC00N2NkLTk2MTAtZTlhMzFmMDFlZTdiIn19LCJuYmYiOjE3MzMyMDI4MTQsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlcm5ldGVzLWRhc2hib2FyZDphZG1pbi11c2VyIn0.lwlDZoOErv6jRLTQT-ckpuQ6TjWNxwWM_wbcTRwIVmjAXQlonrF-Yku-vTXHIB39vHJYijw5Nq3V0f9OzOeN7A5H9d7Wa8WJMFi-K-wsMcfVh_PD9SVlOhy2cOUkIpVC98LaCXz0ksgZvKewII1sKbapF0xkEjVaOqiRHg39kbgsAOWiiyccIiVdocesuLcx7T2LbCknDdwIQEotfcl7uhFs9tDnmDDn7ver2x2NY-T16hxekXc4uhz8ZNfbUxDu9UO5XjSCy7NP9Q5GiYOjeSlj5Qx8Hx4IqOu1Yf_McQTfAEDl7roFIJZs-SL9jCu_YfGkEWHNz9LPL3GJSfManA
```
브라우저 접속