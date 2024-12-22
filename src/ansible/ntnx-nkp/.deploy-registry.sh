#!/bin/bash
##############################################
# Name        : Docker_registry_setup.sh
# Author      : Dimas Maryanto
# Version     : 1.0
# Description : Script is used to configure registry with specified arguments
##############################################

mkdir -p certs auth && \
docker run --rm --entrypoint htpasswd xmartlabs/htpasswd -Bbn "admin" "nutanix/4u" | tee auth/htpasswd && \
openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt -subj "/C=ID/ST=Indonesia/L=Jakarta/O=Nutanix/OU=IT/CN=*.nutanix.local" -addext "subjectAltName = DNS:*.nutanix.local"

sudo mkdir -p /mnt/registry && \
sudo docker run -d -p 5000:5000  --restart=always --name DockerRegistry -v /mnt/registry:/var/lib/registry -v `pwd`/auth:/auth -e "REGISTRY_AUTH=htpasswd" -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd -v `pwd`/certs:/certs -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key registry:2

sudo firewall-cmd --zone=public --add-port=5000/tcp --permanent && \
sudo firewall-cmd --zone=public --add-port=8081/tcp --add-port=8086/tcp --add-port=8087/tcp --permanent && \
sudo firewall-cmd --zone=public --add-port=443/tcp --permanent && \
sudo firewall-cmd --reload
