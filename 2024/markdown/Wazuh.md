대표적인 보안 관제 솔루션
https://wazuh.com/
![[Pasted image 20241024093123.png]]
![[Pasted image 20241024093817.png]]
사전 정보
---
[Elastic Search](https://www.google.com/search?q=elasticsearch&oq=Elastic&gs_lcrp=EgZjaHJvbWUqCggBEAAYsQMYgAQyDwgAEEUYORiDARixAxiABDIKCAEQABixAxiABDINCAIQABiDARixAxiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTYxODZqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8)
[ELK Stack](https://velog.io/@holidenty/ELK-ELK-Stack-%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C)

Server Install
---
최소 사양
![[Pasted image 20241024101257.png]]

간편 설치 명령어
```sh
curl -sO https://packages.wazuh.com/4.9/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
```
- 설치 후 패스워드 꼭 기억하기
```
INFO: --- Summary ---
INFO: You can access the web interface https://<wazuh-dashboard-ip>
    User: admin
    Password: <ADMIN_PASSWORD>
INFO: Installation finished.
```
```
User: admin
Password: ZfttyCjs+9pzjc9f4nlX.c86TJt4rslX
```
방화벽 허용
```sh
[root@Linux1 ~]# firewall-cmd --permanent --add-service=http
success
[root@Linux1 ~]# firewall-cmd --permanent --add-service=https
success
[root@Linux1 ~]# firewall-cmd --reload
success
```

웹 접속
`https://<wazuh-dashboard-ip>`
![[Pasted image 20241024101455.png]]


Install script
---
```
dnf update -y, reboot
 dnf install -y coreutils chkconfig tar libcap
인증서 저장소 설치
curl -sO https://packages.wazuh.com/4.4/wazuh-certs-tool.sh
curl -sO https://packages.wazuh.com/4.4/config.yml
vi config.yml
nodes:
  # Wazuh indexer nodes
  indexer:
    - name: wazuh-01
      ip: 192.168.1.220(본인 wazuh ip)

  # Wazuh server nodes
  # If there is more than one Wazuh server
  # node, each one must have a node_type
  server:
    - name: wazuh-01
      ip: 192.168.1.220(본인 wazuh ip)

  # Wazuh dashboard nodes
  dashboard:
    - name: dashboard
      ip: 192.168.1.220(본인 wazuh ip)

인증서 설치
bash ./wazuh-certs-tool.sh -A
tar -cvf ./wazuh-certificates.tar -C ./wazuh-certificates/ .
rm -rf ./wazuh-certificates

Wazuh 저장소 설치
rpm --import https://packages.wazuh.com/key/GPG-KEY-WAZUH
echo -e '[wazuh]\ngpgcheck=1\ngpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH\nenabled=1\nname=EL-$releasever - Wazuh\nbaseurl=https://packages.wazuh.com/4.x/yum/\nprotect=1' | tee /etc/yum.repos.d/wazuh.repo
[wazuh]
gpgcheck=1
gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH 
enabled=1 name=EL-$releasever - Wazuh 
baseurl=https://packages.wazuh.com/4.x/yum/ 
protect=1
 dnf makecache

설치
dnf -y install wazuh-indexer
 vi /etc/wazuh-indexer/opensearch.yml
network.host: "192.168.1.220"
node.name: "wazuh-01"
cluster.initial_master_nodes:
- "wazuh-01"
plugins.security.nodes_dn:
- "CN=wazuh-01,OU=Wazuh,O=Wazuh,L=California,C=US"

indexer 보안인증서 배포
export NODE_NAME=wazuh-01
# mkdir /etc/wazuh-indexer/certs
# tar -xf ./wazuh-certificates.tar -C /etc/wazuh-indexer/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./admin.pem ./admin-key.pem ./root-ca.pem
# mv -n /etc/wazuh-indexer/certs/$NODE_NAME.pem /etc/wazuh-indexer/certs/indexer.pem
# mv -n /etc/wazuh-indexer/certs/$NODE_NAME-key.pem /etc/wazuh-indexer/certs/indexer-key.pem
# chmod 500 /etc/wazuh-indexer/certs
# chmod 400 /etc/wazuh-indexer/certs/*
# chown -R wazuh-indexer:wazuh-indexer /etc/wazuh-indexer/certs
systemctl enable(start) wazuh-indexer
방화벽 허용
firewall-cmd --permanent --add-port=9200/tcp
firewall-cmd --reload

indexer 보안 스크립트 실행
/usr/share/wazuh-indexer/bin/indexer-security-init.sh

indexer 설치 완료
# curl -k -u admin:admin https://wazuh-01.centlinux-com.com:9200
{
  "name" : "wazuh-01",
  "cluster_name" : "wazuh-cluster",
  "cluster_uuid" : "OYd3dDQ5QUmoGfN0QQ1uxQ",
  "version" : {
    "number" : "7.10.2",
    "build_type" : "rpm",
    "build_hash" : "7203a5af21a8a009aece1474446b437a3c674db6",
    "build_date" : "2023-02-24T18:57:04.388618985Z",
    "build_snapshot" : false,
    "lucene_version" : "9.5.0",
    "minimum_wire_compatibility_version" : "7.10.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "The OpenSearch Project: https://opensearch.org/"
}

wazuh-manager 설치
dnf install -y wazuh-manager
systemctl enable --now wazuh-manager
firewall-cmd --permanent --add-port={1514,1515}/tcp
firewall-cmd --reload

filebeat 설치
dnf install -y filebeat
샘플 filebeat software 다운
curl -so /etc/filebeat/filebeat.yml https://packages.wazuh.com/4.4/tpl/wazuh/filebeat/filebeat.yml

vi /etc/filebeat/filebeat.yml
hosts: ["192.168.1.220:9200"]

filebeat keystore create
admin/admin 계정 설정
echo admin | filebeat keystore add username --stdin --force
echo admin | filebeat keystore add password --stdin --force

alert template 다운
curl -so /etc/filebeat/wazuh-template.json https://raw.githubusercontent.com/wazuh/wazuh/4.4/extensions/elasticsearch/7.x/wazuh-template.json
chmod go+r /etc/filebeat/wazuh-template.json

filebeat 모듈 설치
curl -s https://packages.wazuh.com/4.x/filebeat/wazuh-filebeat-0.2.tar.gz | tar -xvz -C /usr/share/filebeat/modulesd

Wazuh server에 보안 인증서 배포
export NODE_NAME=wazuh-01
# mkdir /etc/filebeat/certs
# tar -xf ./wazuh-certificates.tar -C /etc/filebeat/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./root-ca.pem
# mv -n /etc/filebeat/certs/$NODE_NAME.pem /etc/filebeat/certs/filebeat.pem
# mv -n /etc/filebeat/certs/$NODE_NAME-key.pem /etc/filebeat/certs/filebeat-key.pem
# chmod 500 /etc/filebeat/certs
# chmod 400 /etc/filebeat/certs/*
# chown -R root:root /etc/filebeat/certs

filebeat 실행
systemctl enable --now filebeat
filebeat 설치 확인
filebeat test output
elasticsearch: https://192.168.1.220:9200...
  parse url... OK
  connection...
    parse host... OK
    dns lookup... OK
    addresses: 192.168.18.83
    dial up... OK
  TLS...
    security: server's certificate chain verification is enabled
    handshake... OK
    TLS version: TLSv1.3
    dial up... OK
  talk to server... OK
  version: 7.10.2

wazuh-dashboard 설치
dnf install -y wazuh-dashboard
vi /etc/wazuh-dashboard/opensearch_dashboards.yml
server.host: 192.168.1.220
opensearch.hosts: https://192.168.1.220:9200

wazuh-dashboard에 보안 인증서 배포
# export NODE_NAME=wazuh-01
# mkdir /etc/wazuh-dashboard/certs
# tar -xf ./wazuh-certificates.tar -C /etc/wazuh-dashboard/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./root-ca.pem
# mv -n /etc/wazuh-dashboard/certs/$NODE_NAME.pem /etc/wazuh-dashboard/certs/dashboard.pem
# mv -n /etc/wazuh-dashboard/certs/$NODE_NAME-key.pem /etc/wazuh-dashboard/certs/dashboard-key.pem
# chmod 500 /etc/wazuh-dashboard/certs
# chmod 400 /etc/wazuh-dashboard/certs/*
# chown -R wazuh-dashboard:wazuh-dashboard /etc/wazuh-dashboard/certs

wazuh-dashboard
systemctl enable --now wazuh-dashboard
firewall-cmd --permanent --add-service=https
firewall-cmd --reload

웹 접속 완료 -> admin / admin
```