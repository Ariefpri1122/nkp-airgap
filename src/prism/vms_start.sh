#!/bin/sh

VM_LIST=(NTNX-PC-01 NTNX-Airgap NTNX-NDB-Server NTNX-NDB-Agent-DC)

for vm_name in "${VM_LIST[@]}"; 
do 
acli vm.on $vm_name; 
done