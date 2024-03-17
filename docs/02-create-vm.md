## Create Virtual Machine (VM) template

Untuk membuat Virtual Machine kita membutuhkan ISO image, untuk OS yang akan kita gunakan adalah Oracle Linux v8.7 karena CentOS version 7 & 8 akan end of life (EOL) pada 2024-04 jadi kita ganti default OS menjadi OracleLinux. 

Tahap-tahap untuk membuat Virtual Machine seperti berikut:

- Download iso [OracleLinux](https://yum.oracle.com/oracle-linux-isos.html)
- Create Virtual Machine
- Post Installation
    - Update system seperti `kernel`, `libs` dll
    - Addons commons package seperti `curl`, `wget`, `tmux` dll
    - Setup `/etc/selinux/conf`
    - Setup `/etc/lvm.conf`

## Download ISOs for OracleLinux 8.7

Sekarang kita download dulu Installation Media (ISOs) untuk OracleLinux v8.7 untuk version DVD seperti berikut:

![download-iso](imgs/06b-create-vm-oraclelinux8/01-iso-download.png)

Kita copy link download tersebut, kemudian kita ke Prism Central menudian akses menu [Compute & Storage]() -> [Images]() dan [Add Image]() pilih [URL]() dan masukan link `https://yum.oracle.com/ISOS/OracleLinux/OL8/u7/x86_64/OracleLinux-R8-U7-x86_64-dvd.iso` seperti berikut:

![add-image](imgs/06b-create-vm-oraclelinux8/01a-prism-add-image.png)

Kemudian [Next](), simpan di [Place image directly on cluster]() dan [Save]() kemudian tunggu sampai image selesai terupload. Jika sudah selesai terdownload hasilnya seperti berikut:

![image-downloaded](imgs/06b-create-vm-oraclelinux8/01b-image-downloaded.png)

## Create Virtual Machine (VM)

Selanjutnya kita buat Virtual Machine (VM) dengan specifikasi seperti berikut:

```yaml
configuration:
    name: template-oraclelinux-8.7
    description: Template OS Linux with OracleLinux v8.7
    properties:
        cpus: 2
        corePerCpu: 2
        memory: 4
resources:
    disk:
        - type: Disk
          operation: Allocate on Storage Container
          strageContainer: default-storage
          capacity: 50 GiB
          busType: SCSI
        - type: CD-ROM
          operation: Empty CD-ROM
          busType: SATA
    networks:
        - subnet: Primary
          networkConnectionState: Conntected
          assignmentType: Assign with DHCP
```

Untuk membuatnya, kita ke Prism Central kemudian menu [Compute & Storage]() -> [VMs]() dan click button [Add VM]() seperti berikut:

![add-vm](imgs/06b-create-vm-oraclelinux8/02-vm-config.png)

Kemudian click button [Next](), selanjutnya kita pilih disks dan network seperti berikut:

![set-resources](imgs/06b-create-vm-oraclelinux8/02a-resources.png)

Kemudian click button [Next](), selanjutnya di menu management kita biarkan default seperti berikut:

![set-management](imgs/06b-create-vm-oraclelinux8/02b-management.png)

Lalu click button [Next], maka akan muncul summary vm will be created seperti berikut:

![vm-summary](imgs/06b-create-vm-oraclelinux8/02c-summary.png)

Setelah itu click button [Create VM](), maka hasilnya seperti berikut:

![vm-created](imgs/06b-create-vm-oraclelinux8/02d-vm-created.png)

## Deploy OS OracleLinux v8.7