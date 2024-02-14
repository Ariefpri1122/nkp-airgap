## Post Instal Nutanix Cluster

Ada beberapa operational yang perlu kita lakukan setelah install nutanix cluster, seperti berikut:

1. Lakukan update software dengan menggunakan Menu LCM pada Prism Element
2. Deploy Prism Central
3. Register Prism Central to Prism Element
4. Lakukan update software dengan menggunakan Menu LCM pada Prism Central

### LCM update software

### NTP Server (offsite)

Siapkan Physical/Virtual machine yang akan dipasangkan untuk mirror NTP Server secara offline.

Sebagai contoh disini saya sudah menyiapkan VM dengan specifikasi seperti berikut:

```yaml
VM: 
    os: Oracle Linux v9.3
    vcpu: 2 cores
    memory: 4 GB
    storage: 
        size: 20 GB
        partision:
            lvm:
                /: 20 Gb
                swap: 4 Gb
    network:
        gateway: 10.12.10.254
        ip: 10.12.10.2
```

Kemudian kita install package ntp server dengan perintah berikut:

```bash
dnf update -y && \
dnf install chrony nc && \
systemctl enable --now chronyd && \
firewall-cmd --permanent --add-service=ntp && \
firewall-cmd --reload
```

Set Chrony to act as an NTP server for a local network. To turn Chrony into an NTP server add the following line into the main Chrony `/etc/chrony.conf` configuration file:

```conf
# Use public servers change me
pool id.pool.ntp.org iburst

allow 10.12.0.0/24
# add an other subnet you want to allow
```

Kemudian kita restart service `chronyd` dengan perintah berikut:

```bash
systemctl restart chronyd
```

To verify connection to UDP port 123;

```bash
nc -uzv 10.12.10.1 123
```

The output look like this:

![output](imgs/06-post-install/02a-ntp-server.png)

Setelah itu kita set NTP Server pada Prism Central pada menu `Setting -> NTP Servers` dengan menambahkan ip server yang telah kita setup seperti berikut:

![prism-central](imgs/06-post-install/02b-add-local-ntpserver.png)

### Darksite webserver (offline LCM)

Siapkan Physical/Virtual machine yang akan dipasangkan untuk webserver untuk menyimpan binary seperti release, image, patch dan lain-lain sehinga proses download dari internet di gantikan ke mekanisme ini.

Sebagai contoh disini saya sudah menyiapkan VM dengan specifikasi seperti berikut:

```yaml
VM: 
    os: Oracle Linux v9.3
    vcpu: 2 cores
    memory: 4 GB
    storage: 
        size: 100 GB
        partision:
            lvm:
                /: 95 Gb
                swap: 4 Gb
    network:
        gateway: 10.12.10.254
        ip: 10.12.10.1
```

Kemudian kita install package httpd dengan perintah berikut:

```bash
yum update && \
yum install -y httpd && \
systemctl enable --now httpd && \
firewall-cmd --zone=public --add-port=80/tcp --permanent && \
firewall-cmd --reload
```

Maka hasilnya seperti berikut:

![httpd-instaled](imgs/07-karbon/03-httpd-instaled.png)