## Enable NDB Server

Requirement to enable Nutanix Database Server (NDB) formally ERA:

- Nutanix Prism
- `NDB-Server.qcow2` disk image, download from [Nutanix Support Download](https://portal.nutanix.com/page/downloads?product=ndb)
    ![ndb-download](imgs/11-ndb/00-ndb-download.png)
- Deploy NDB-Server as VM from Prism Element
- Setup & Configure

### Upload disk image to Prism Element

First we need upload disk image to Image Configuration from Settings -> Image Configuration 

![menu-image](imgs/11-ndb/01-upload-ndb-qcow2.png)

then Add Disk look like 

![add-disk-image](imgs/11-ndb/01a-uploading-qcow2-image.png)

And save, finally image can be used to create Virtual Machine

![list-disk-image](imgs/11-ndb/01b-image-activated.png)

### Deploy NDB-Server using VM

To deploy NDB-Server very stright-forward, simply create an Virtual Machine from Prism Element 

![menu-vm](imgs/11-ndb/02-deploy-era-vm.png)

```bash
#cloud-config
runcmd:
 - configure_static_ip ip=<your-ndb-vm> gateway=<your-subnet-gw> netmask=255.255.255.0 nameserver=8.8.8.8
```