#!/bin/sh

for vm_name in `acli vm.list power_state=on | awk '{print $1}'`; 
do 
acli vm.shutdown $vm_name; 
done