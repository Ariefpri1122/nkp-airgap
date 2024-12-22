#!/bin/bash
export NKP_CLUSTER_NAME="nkp-worker1-hpoc"
export SUBNET="mgnt.ntnx.ipam.local"
export CONTROLPLANE_VIP="10.10.20.100"
export METALLB_IP_RANGE="10.10.20.101-10.10.20.105"

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
    --registry-url=${PRIVATE_REGISTRY_URL} \
    --registry-username=${PRIVATE_REGISTRY_USERNAME} \
    --registry-password=${PRIVATE_REGISTRY_PASSWORD} \
    --registry-cacert=${PRIVATE_REGISTRY_CACERT} \
    --registry-mirror-url=${REGISTRY_URL} \
    --registry-mirror-username=${REGISTRY_USERNAME} \
    --registry-mirror-password=${REGISTRY_PASSWORD} \
    --registry-mirror-cacert=${REGISTRY_CACERT} \
    --kubernetes-service-load-balancer-ip-range=${METALLB_IP_RANGE} \
    --ssh-public-key-file=${SSH_PUBLIC_KEY} \
    --control-plane-replicas 3 \
    --control-plane-cores-per-vcpu 1 \
    --control-plane-vcpus 8 \
    --control-plane-memory 8 \
    --worker-replicas 3 \
    --worker-vcpus 8 \
    --worker-cores-per-vcpu 1 \
    --worker-memory 8 \
    --insecure