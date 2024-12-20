#!/bin/bash

export IMAGE="nkp-rocky-9.5-release-cis-1.30.5-20241204003513.qcow2"
export SUBNET="mgnt.ntnx.ipam.local"
export NKP_CLUSTER_NAME="nkp-kommander-hpoc"
export CONTROLPLANE_VIP="10.10.20.5"
export METALLB_IP_RANGE="10.10.20.6-10.10.20.9"
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

nkp create cluster nutanix \
    --cluster-name=${NKP_CLUSTER_NAME} \
    --control-plane-prism-element-cluster=${CLUSTER_NAME} \
    --worker-prism-element-cluster=${CLUSTER_NAME} \
    --control-plane-subnets=${SUBNET} \
    --worker-subnets=${SUBNET} \
    --control-plane-endpoint-ip=${CONTROLPLANE_VIP} \
    --csi-storage-container=${STORAGE_CONTAINER} \
    --endpoint=${NUTANIX_ENDPOINT} \
    --control-plane-vm-image=${IMAGE} \
    --worker-vm-image=${IMAGE} \
    --registry-mirror-url=${REGISTRY_URL} \
    --registry-mirror-username=${REGISTRY_USERNAME} \
    --registry-mirror-password=${REGISTRY_PASSWORD} \
    --registry-mirror-cacert=${REGISTRY_CACERT} \
    --kubernetes-service-load-balancer-ip-range=${METALLB_IP_RANGE} \
    --ssh-public-key-file=${SSH_PUBLIC_KEY} \
    --control-plane-replicas 1 \
    --control-plane-cores-per-vcpu 1 \
    --control-plane-vcpus 8 \
    --control-plane-memory 16 \
    --worker-replicas 3 \
    --worker-vcpus 8 \
    --worker-cores-per-vcpu 1 \
    --worker-memory 16 \
    --insecure \
    --self-managed