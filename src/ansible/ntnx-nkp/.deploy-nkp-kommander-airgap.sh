#!/bin/bash
export NKP_CLUSTER_NAME="nkp-kommander-hpoc1030"
export SUBNET="ntnx-mgnt-ipam-local"
export CONTROLPLANE_VIP="10.10.30.32"
export METALLB_IP_RANGE="10.10.30.41-10.10.30.45"

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
    --registry-mirror-url=${MIRROR_REGISTRY_URL} \
    --registry-mirror-username=${MIRROR_REGISTRY_USERNAME} \
    --registry-mirror-password=${MIRROR_REGISTRY_PASSWORD} \
    --registry-mirror-cacert=${MIRROR_REGISTRY_CACERT} \
    --kubernetes-service-load-balancer-ip-range=${METALLB_IP_RANGE} \
    --ssh-public-key-file=${SSH_PUBLIC_KEY} \
    --control-plane-replicas=1 \
    --control-plane-cores-per-vcpu=1 \
    --control-plane-vcpus=4 \
    --control-plane-memory=8 \
    --worker-replicas=1 \
    --worker-vcpus=8 \
    --worker-cores-per-vcpu=1 \
    --worker-memory=16 \
    --insecure=true \
    --self-managed=true