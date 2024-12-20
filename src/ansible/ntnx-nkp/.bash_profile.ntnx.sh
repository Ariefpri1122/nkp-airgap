#!/bin/bash

export IMAGE="nkp-rocky-9.5-release-cis-1.30.5-20241204003513.qcow2"
export NUTANIX_USER="admin"
export NUTANIX_PASSWORD="Nutanix/4u@2024"
export NUTANIX_ENDPOINT="https://10.10.20.31:9440"
export CLUSTER_NAME="DELL-R730XD-AHV"
export STORAGE_CONTAINER="default-storage"
export SSH_PUBLIC_KEY="/home/user/.ssh/id_ed25519.pub"
export REGISTRY_CACERT="/etc/docker/certs.d/airgap-0:5000/registry-ca.crt"
export REGISTRY_URL="https://airgap-0:5000"
export REGISTRY_USERNAME="admin"
export REGISTRY_PASSWORD="nutanix/4u"
