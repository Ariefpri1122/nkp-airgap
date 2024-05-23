# Adding physical disk

```bash
# show cvm on pe
virsh list --all

# get metadata disk
virsh edit <cvm-domain-name>
```

```xml
<devices>
    <disk type='block' device='disk'>
      <driver name='qemu' type='raw' cache='none' io='native'/>
      <source dev='/dev/disk/by-id/changed-with-dev-id'/>
      <backingStore/>
      <target dev='changed-with-path-device-id' bus='scsi'/>
      <serial>changed-with-serial-disk</serial>
      <wwn>changed-with-wwn-id</wwn>
      <vendor>changed-with-vendor-name</vendor>
      <product>changed-with-product-name</product>
      <address type='drive' controller='0' bus='0' target='0' unit='1'/>
    </disk>
</devices>
```

find serial id with this command:

```bash
lshw -class disk
```

```bash
sudo cluster/bin/repartition_disks -d /dev/sdX
```

```bash
sudo cluster/bin/clean_disks -p /dev/sdX1
```

```bash
sudo cluster/bin/mount_disks -d /dev/sdx,...
```