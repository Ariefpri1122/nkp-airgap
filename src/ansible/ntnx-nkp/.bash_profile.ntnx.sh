#!/bin/bash

export IMAGE="nkp-rocky-9.5-release-1.30.5-20241204003513.qcow2"
export NUTANIX_USER="admin"
export NUTANIX_PASSWORD="Nutanix/4u@2024"
export NUTANIX_ENDPOINT="https://pc.nutanix.local:9440"
export CLUSTER_NAME="DELL-R730XD-AHV"
export STORAGE_CONTAINER="default-storage"
export SSH_PUBLIC_KEY="/home/nutanix/.ssh/id_ed25519.pub"
# mirror registry
export MIRROR_REGISTRY_CACERT="/etc/docker/certs.d/airgap.nutanix.local:5000/registry.crt"
export MIRROR_REGISTRY_URL="https://airgap.nutanix.local:5000"
export MIRROR_REGISTRY_USERNAME="admin"
export MIRROR_REGISTRY_PASSWORD="nutanix/4u"
# private registry
export PRIVATE_REGISTRY_URL="https://registry.nutanix.local"
export PRIVATE_REGISTRY_USERNAME="nkp-user"
export PRIVATE_REGISTRY_PASSWORD="Nutanix/4u"
export PRIVATE_REGISTRY_CACERT="/etc/docker/certs.d/registry.nutanix.local/registry.crt"
