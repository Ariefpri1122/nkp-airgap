Setelah kita install Nutanix OS menggunakan bootdrive, 

## Create cluster

Setelah kita organize host dan cvm, sekarang kita bisa membuat cluster dengan perintah berikut:

```bash
cluster -s <cvm-ips> --redundancy_factor=<number-of-factor> create
```

Jika dijalankan hasilnya seperti berikut:

```bash
nutanix@NTNX-9810330e-A-CVM:192.168.88.27:~$ cluster status
2023-08-25 02:07:45,107Z CRITICAL MainThread cluster:2930 Cluster is currently unconfigured. Please create the cluster.

nutanix@NTNX-ba60e5b2-A-CVM:192.168.88.32:~$ cluster -s 192.168.88.32,192.168.88.33,192.168.88.34 --redundancy_factor=2 create
2023-08-25 23:15:33,673Z INFO MainThread cluster:2943 Executing action create on SVMs 192.168.88.32,192.168.88.33,192.168.88.34
2023-08-25 23:15:36,700Z INFO MainThread cluster:1007 Discovered node:
ip: 192.168.88.32
        rackable_unit_serial: ba60e5b2
        node_position: A
        node_uuid: 599cd71a-b97f-4a5f-8294-7787e5892888

2023-08-25 23:15:36,701Z INFO MainThread cluster:1007 Discovered node:
ip: 192.168.88.33
        rackable_unit_serial: 9e7742d3
        node_position: A
        node_uuid: 0495d08d-3e7d-43bb-a785-4e5850c6b851

2023-08-25 23:15:36,701Z INFO MainThread cluster:1007 Discovered node:
ip: 192.168.88.34
        rackable_unit_serial: 350f3275
        node_position: A
        node_uuid: 3ebcaca5-1e34-4700-969e-824eec66dc88

2023-08-25 23:15:36,701Z INFO MainThread cluster:1025 Cluster is on arch x86_64
2023-08-25 23:15:36,701Z INFO MainThread genesis_utils.py:8077 Maximum node limit corresponding to the hypervisors on the cluster (set([u'kvm'])) : 32
2023-08-25 23:15:36,705Z INFO MainThread genesis_rack_utils.py:50 Rack not configured on node (svm_ip: 192.168.88.32)
2023-08-25 23:15:36,710Z INFO MainThread genesis_rack_utils.py:50 Rack not configured on node (svm_ip: 192.168.88.33)
2023-08-25 23:15:36,714Z INFO MainThread genesis_rack_utils.py:50 Rack not configured on node (svm_ip: 192.168.88.34)
2023-08-25 23:15:41,693Z INFO MainThread cluster:1332 iptables configured on SVM 192.168.88.32
2023-08-25 23:15:46,799Z INFO MainThread cluster:1332 iptables configured on SVM 192.168.88.33
2023-08-25 23:15:51,877Z INFO MainThread cluster:1332 iptables configured on SVM 192.168.88.34
2023-08-25 23:15:51,880Z INFO MainThread cluster:1351 Creating certificates
2023-08-25 23:15:56,715Z INFO MainThread cluster:1368 Setting the cluster functions on SVM node 192.168.88.32
2023-08-25 23:15:56,717Z INFO MainThread cluster:1373 Configuring Zeus mapping ({u'192.168.88.34': 3, u'192.168.88.33': 2, u'192.168.88.32': 1}) on SVM node 192.168.88.32
2023-08-25 23:15:58,254Z INFO MainThread cluster:1368 Setting the cluster functions on SVM node 192.168.88.33
2023-08-25 23:15:58,256Z INFO MainThread cluster:1373 Configuring Zeus mapping ({u'192.168.88.34': 3, u'192.168.88.33': 2, u'192.168.88.32': 1}) on SVM node 192.168.88.33
2023-08-25 23:16:00,615Z INFO MainThread cluster:1368 Setting the cluster functions on SVM node 192.168.88.34
2023-08-25 23:16:00,617Z INFO MainThread cluster:1373 Configuring Zeus mapping ({u'192.168.88.34': 3, u'192.168.88.33': 2, u'192.168.88.32': 1}) on SVM node 192.168.88.34
2023-08-25 23:16:02,958Z INFO MainThread cluster:1396 Creating cluster with SVMs: 192.168.88.32,192.168.88.33,192.168.88.34
2023-08-25 23:16:03,147Z INFO MainThread cluster:1407 Will seed prism with password hash $6$Ej223/QPGNcQB$Pp1plB7W2.hxswYWiywajdfgS0YYBCyxa/fK7eDoy8FzaDpZFjdJZLprFpCY8O.Y0dpdBNP.XQWT12WvRWCAQ/
2023-08-25 23:16:57,925Z INFO MainThread cluster:1425 Zeus is not ready yet, trying again in 5 seconds
2023-08-25 23:17:35,895Z INFO MainThread cluster:1444 Waiting for services to start
Waiting on 192.168.88.32 (Up) to start:  SysStatCollector IkatProxy IkatControlPlane SSLTerminator SecureFileSync Medusa DynamicRingChanger Pithos InsightsDB Athena Mercury Mantle Stargate InsightsDataTransfer Ergon GoErgon Cerebro Chronos Curator Prism Hera CIM AlertManager Arithmos Catalog Acropolis Uhura NutanixGuestTools MinervaCVM ClusterConfig APLOSEngine APLOS PlacementSolver Lazan Polaris Delphi Security Flow Anduril XTrim ClusterHealth
Waiting on 192.168.88.33 (Up) to start:  SysStatCollector IkatProxy IkatControlPlane SSLTerminator SecureFileSync Medusa DynamicRingChanger Pithos InsightsDB Athena Mercury Mantle Stargate InsightsDataTransfer Ergon GoErgon Cerebro Chronos Curator Prism Hera CIM AlertManager Arithmos Catalog Acropolis Uhura NutanixGuestTools MinervaCVM ClusterConfig APLOSEngine APLOS PlacementSolver Lazan Polaris Delphi Security Flow Anduril XTrim ClusterHealth
Waiting on 192.168.88.34 (Up, ZeusLeader) to start:  SysStatCollector IkatProxy IkatControlPlane SSLTerminator SecureFileSync Medusa DynamicRingChanger Pithos InsightsDB Athena Mercury Mantle Stargate InsightsDataTransfer Ergon GoErgon Cerebro Chronos Curator Prism Hera CIM AlertManager Arithmos Catalog Acropolis Uhura NutanixGuestTools MinervaCVM ClusterConfig APLOSEngine APLOS PlacementSolver Lazan Polaris Delphi Security Flow Anduril XTrim ClusterHealth

The state of the cluster: start
Lockdown mode: Disabled

        CVM: 192.168.88.33 Up
                                Zeus   UP       [12935, 12983, 12984, 12985, 12994, 13012]
                           Scavenger   UP       [17030, 17210, 17211, 17212]
                              Xmount   UP       [17027, 17185, 17186, 17221]
                    SysStatCollector   UP       [19631, 19771, 19772, 19773]
                           IkatProxy   UP       [20756, 20879, 20880, 20881]
                    IkatControlPlane   UP       [21459, 21594, 21595, 21596]
                       SSLTerminator   UP       [21567, 21768, 21769]
                      SecureFileSync   UP       [21636, 21835, 21836, 21837]
                              Medusa   UP       [22682, 22836, 22837, 22919, 23361]
                  DynamicRingChanger   UP       [25151, 25257, 25258, 25295]
                              Pithos   UP       [25198, 25356, 25357, 25391]
                          InsightsDB   UP       [25270, 25528, 25529, 25546]
                              Athena   UP       [25386, 25618, 25619, 25620]
                             Mercury   UP       [25478, 25685, 25686, 25745]
                              Mantle   UP       [25630, 25867, 25868, 25880]
                          VipMonitor   UP       [26665, 26666, 26667, 26668, 26676]
                            Stargate   UP       [26974, 27094, 27095, 27127, 27132]
                InsightsDataTransfer   UP       [27634, 27778, 27779, 27780, 27781, 27782, 27783, 27784, 27785]
                               Ergon   UP       [27861, 27983, 27984, 27985]
                             GoErgon   UP       [27951, 28066, 28067, 28141]
                             Cerebro   UP       [28164, 28248, 28249, 28368]
                             Chronos   UP       [28254, 28356, 28357, 28374]
                             Curator   UP       [28313, 28535, 28536, 28599]
                               Prism   UP       [28499, 28643, 28644, 28733]
                                Hera   UP       [28575, 28805, 28806, 28807]
                                 CIM   UP       [28746, 28918, 28919, 28926, 28928]
                        AlertManager   UP       [28897, 29105, 29106, 29135]
                            Arithmos   UP       [28959, 29175, 29176, 29298]
                             Catalog   UP       [29318, 29462, 29463, 29466]
                           Acropolis   UP       [29717, 29885, 29886, 29887]
                               Uhura   UP       [29833, 30015, 30016, 30565]
                   NutanixGuestTools   UP       [29980, 30155, 30156, 30166, 30183]
                          MinervaCVM   UP       [30944, 31084, 31085, 31086, 31368]
                       ClusterConfig   UP       [31098, 31245, 31246, 31247]
                         APLOSEngine   UP       [31156, 31299, 31300, 31301]
                               APLOS   UP       [31497, 31609, 31610, 31611]
                     PlacementSolver   UP       [31551, 31671, 31672, 31673, 31697]
                               Lazan   UP       [31675, 31822, 31823, 31824]
                             Polaris   UP       [31746, 31927, 31928, 32005]
                              Delphi   UP       [31775, 32065, 32066, 32067, 32078]
                            Security   UP       [32023, 32614, 32615, 32617]
                                Flow   UP       [319, 320, 321, 331, 32101]
                             Anduril   UP       [595, 596, 597, 32452]
                               XTrim   UP       [591, 770, 771, 772]
                       ClusterHealth   UP       [660, 918, 919]
2023-08-25 23:21:29,740Z INFO MainThread cluster:1450 Running CE cluster post-create script
2023-08-25 23:21:29,745Z INFO MainThread cluster:3104 Success!
```

Kemudian, temen-temen bisa akses salah satu ip cvm dengan port 9440 untuk mengkases Prism Element seperti berikut:

![first-login](imgs/05-prism-element/01-first-login-prism-element.png)

Login menggunakan default credential yaitu user = `admin` dan password = `nutanix/4u`, setelah itu temen-temen akan diarahkan untuk mengganti password default tersebut seperti berikut:

![changed-default-password](imgs/05-prism-element/01a-changed-default-login.png)

Setelah itu temen-temen login dengan credential yang baru, dan setelah itu temen-temen login ke Nutanix NEXT account seperti berikut:

![login-nutanix-next](imgs/05-prism-element/01b-login-nutanix-next.png)

Pada mesin tersebut harus terkoneksi ke internet, supaya bisa login ke Nutanix Prism Element. Jika tidak bisa login, silahkan coba ganti password dengan click reset password pada account [my.nutanix.com](https://my.nutanix.com) jika berhasil maka outputnya seperti berikut:

![prism-element-dashboard](imgs/05-prism-element/01c-pe-dashboard.png)

## Organize nodes

selanjutnya adalah kita organize dulu setiap nodenya seperti setting hostname lain-lain: 

Setup hostname for easyies to identified/troubleshoot when you got hardware problem:
- changed on host ip
- changed on cvm

Kurang lebih seperti berikut metricnya:

| IPMI          | Node name     | Host IP       | Hostname for HostIP   | CVM IP        | Hostname for CVM      |
| :---          | :---          | :---          | :---                  | :---          | :---                  |
| 192.168.88.12 | NTNX-B-CVM    | 192.168.88.22 | NTNX-NODE-B           | 192.168.88.32 | NTNX-CVM-B            |
| 192.168.88.13 | NTNX-C-CVM    | 192.168.88.22 | NTNX-NODE-C           | 192.168.88.33 | NTNX-CVM-C            |
| 192.168.88.14 | NTNX-D-CVM    | 192.168.88.22 | NTNX-NODE-D           | 192.168.88.34 | NTNX-CVM-D            |

Untuk mengganti Node Name pada CVM IP kita bisa menggunakan perintah berikut:

```bash
change_cvm_display_name --cvm_ip=<cvm-ip> --cvm_name=<cvm-display-name>
```

Jika kita exekusi hasilnya seperti berikut:

```bash
nutanix@NTNX-CVM-D:192.168.88.34:~$ change_cvm_display_name --cvm_ip=192.168.88.32 --cvm_name=NTNX-B-CVM
2023-08-26 00:16:22,135Z INFO change_cvm_display_name:207 Attempting to change the display name of the CVM
2023-08-26 00:16:22,136Z INFO zookeeper_session.py:191 change_cvm_display_name is attempting to connect to Zookeeper
2023-08-26 00:16:22,145Z INFO change_cvm_display_name:125 Retrieving the name of the CVM for the host
2023-08-26 00:16:22,147Z INFO zookeeper_session.py:625 ZK session establishment complete, sessionId=0x28a2f177ebb013e, negotiated timeout=20 secs
2023-08-26 00:16:22,706Z INFO change_cvm_display_name:156 Running prechecks before execution of script
2023-08-26 00:16:22,706Z INFO change_cvm_display_name:162 Running on AHV host
2023-08-26 00:16:22,707Z INFO change_cvm_display_name:168 Running on different CVM
2023-08-26 00:16:22,707Z INFO change_cvm_display_name:175 Display name is validated
Changing display name to NTNX-B-CVM. This will reboot the CVM. Do you want to proceed? (Y/N): Y
2023-08-26 00:16:26,901Z INFO change_cvm_display_name:248 Checking if shutdown token can be retrieved
2023-08-26 00:16:26,990Z INFO change_cvm_display_name:254 Shutting down CVM:192.168.88.32 for changing the display name
2023-08-26 00:16:57,533Z WARNING command.py:175 Timeout executing /usr/bin/ssh -q -o CheckHostIp=no -o ConnectTimeout=15 -o StrictHostKeyChecking=no -o TCPKeepAlive=yes -o UserKnownHostsFile=/dev/null -o ControlPath=/home/nutanix/.ssh/controlmasters/tmp__NS4L -o PreferredAuthentications=publickey  nutanix@192.168.88.32 source /etc/profile; /home/nutanix/cluster/bin/cvm_shutdown -h now: 30 secs elapsed
2023-08-26 00:16:57,534Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:16:57,534Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down

2023-08-26 00:17:57,738Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:17:57,738Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down
2023-08-26 00:18:57,957Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:18:57,957Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down
2023-08-26 00:18:58,120Z INFO change_cvm_display_name:263 CVM was shut down succesfully
2023-08-26 00:18:58,120Z INFO change_cvm_display_name:67 Running cmd: virsh domrename NTNX-ba60e5b2-A-CVM NTNX-B-CVM on host
2023-08-26 00:19:13,286Z INFO change_cvm_display_name:67 Running cmd: virsh start NTNX-B-CVM on host
2023-08-26 00:19:31,245Z INFO change_cvm_display_name:67 Running cmd: virsh autostart NTNX-B-CVM on host
2023-08-26 00:19:46,425Z INFO change_cvm_display_name:284 Attempting to create a backup of the NTNX-CVM.xml file on host
2023-08-26 00:19:46,527Z INFO change_cvm_display_name:103 Creating new CVM XML config file
2023-08-26 00:19:46,527Z INFO change_cvm_display_name:105 Running cmd: virsh dumpxml NTNX-B-CVM > NTNX-CVM.xml on host
2023-08-26 00:19:46,688Z INFO change_cvm_display_name:111 Successful in creating the XML file for the CVM.
2023-08-26 00:19:46,688Z INFO change_cvm_display_name:297 CVM rename successful

nutanix@NTNX-CVM-D:192.168.88.34:~$ change_cvm_display_name --cvm_ip=192.168.88.33 --cvm_name=NTNX-C-CVM
2023-08-26 00:26:55,578Z INFO change_cvm_display_name:207 Attempting to change the display name of the CVM
2023-08-26 00:26:55,580Z INFO zookeeper_session.py:191 change_cvm_display_name is attempting to connect to Zookeeper
2023-08-26 00:26:55,589Z INFO change_cvm_display_name:125 Retrieving the name of the CVM for the host
2023-08-26 00:26:55,594Z INFO zookeeper_session.py:625 ZK session establishment complete, sessionId=0x18a2f375f5a007c, negotiated timeout=20 secs
2023-08-26 00:26:56,156Z INFO change_cvm_display_name:156 Running prechecks before execution of script
2023-08-26 00:26:56,156Z INFO change_cvm_display_name:162 Running on AHV host
2023-08-26 00:26:56,156Z INFO change_cvm_display_name:168 Running on different CVM
2023-08-26 00:26:56,157Z INFO change_cvm_display_name:175 Display name is validated
Changing display name to NTNX-C-CVM. This will reboot the CVM. Do you want to proceed? (Y/N): Y
2023-08-26 00:26:57,986Z INFO change_cvm_display_name:248 Checking if shutdown token can be retrieved
2023-08-26 00:26:58,074Z INFO change_cvm_display_name:254 Shutting down CVM:192.168.88.33 for changing the display name
2023-08-26 00:27:28,512Z WARNING command.py:175 Timeout executing /usr/bin/ssh -q -o CheckHostIp=no -o ConnectTimeout=15 -o StrictHostKeyChecking=no -o TCPKeepAlive=yes -o UserKnownHostsFile=/dev/null -o ControlPath=/home/nutanix/.ssh/controlmasters/tmpDYJE6l -o PreferredAuthentications=publickey  nutanix@192.168.88.33 source /etc/profile; /home/nutanix/cluster/bin/cvm_shutdown -h now: 30 secs elapsed
2023-08-26 00:27:28,513Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:27:28,513Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down
2023-08-26 00:27:42,403Z INFO zookeeper_session.py:625 ZK session establishment complete, sessionId=0x18a2f375f5a007c, negotiated timeout=20 secs
2023-08-26 00:28:28,708Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:28:28,708Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down
2023-08-26 00:28:28,865Z INFO change_cvm_display_name:263 CVM was shut down succesfully
2023-08-26 00:28:28,865Z INFO change_cvm_display_name:67 Running cmd: virsh domrename NTNX-9e7742d3-A-CVM NTNX-C-CVM on host
2023-08-26 00:28:44,033Z INFO change_cvm_display_name:67 Running cmd: virsh start NTNX-C-CVM on host
2023-08-26 00:29:02,063Z INFO change_cvm_display_name:67 Running cmd: virsh autostart NTNX-C-CVM on host
2023-08-26 00:29:17,237Z INFO change_cvm_display_name:284 Attempting to create a backup of the NTNX-CVM.xml file on host
2023-08-26 00:29:17,339Z INFO change_cvm_display_name:103 Creating new CVM XML config file
2023-08-26 00:29:17,340Z INFO change_cvm_display_name:105 Running cmd: virsh dumpxml NTNX-C-CVM > NTNX-CVM.xml on host
2023-08-26 00:29:17,504Z INFO change_cvm_display_name:111 Successful in creating the XML file for the CVM.
2023-08-26 00:29:17,505Z INFO change_cvm_display_name:297 CVM rename successful

nutanix@NTNX-CVM-B:192.168.88.32:~$ change_cvm_display_name --cvm_ip=192.168.88.34 --cvm_name=NTNX-D-CVM
2023-08-26 00:36:01,801Z INFO change_cvm_display_name:207 Attempting to change the display name of the CVM
2023-08-26 00:36:01,803Z INFO zookeeper_session.py:191 change_cvm_display_name is attempting to connect to Zookeeper
2023-08-26 00:36:01,811Z INFO change_cvm_display_name:125 Retrieving the name of the CVM for the host
2023-08-26 00:36:01,816Z INFO zookeeper_session.py:625 ZK session establishment complete, sessionId=0x28a2f4015f2007f, negotiated timeout=20 secs
2023-08-26 00:36:02,495Z INFO change_cvm_display_name:156 Running prechecks before execution of script
2023-08-26 00:36:02,496Z INFO change_cvm_display_name:162 Running on AHV host
2023-08-26 00:36:02,496Z INFO change_cvm_display_name:168 Running on different CVM
2023-08-26 00:36:02,496Z INFO change_cvm_display_name:175 Display name is validated
Changing display name to NTNX-D-CVM. This will reboot the CVM. Do you want to proceed? (Y/N): Y
2023-08-26 00:36:05,639Z INFO change_cvm_display_name:248 Checking if shutdown token can be retrieved
2023-08-26 00:36:05,734Z INFO change_cvm_display_name:254 Shutting down CVM:192.168.88.34 for changing the display name
2023-08-26 00:36:36,175Z WARNING command.py:175 Timeout executing /usr/bin/ssh -q -o CheckHostIp=no -o ConnectTimeout=15 -o StrictHostKeyChecking=no -o TCPKeepAlive=yes -o UserKnownHostsFile=/dev/null -o ControlPath=/home/nutanix/.ssh/controlmasters/tmp5pz9sR -o PreferredAuthentications=publickey  nutanix@192.168.88.34 source /etc/profile; /home/nutanix/cluster/bin/cvm_shutdown -h now: 30 secs elapsed
2023-08-26 00:36:36,175Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:36:36,176Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down
2023-08-26 00:36:49,301Z INFO zookeeper_session.py:625 ZK session establishment complete, sessionId=0x28a2f4015f2007f, negotiated timeout=20 secs
2023-08-26 00:37:36,415Z INFO change_cvm_display_name:261 Waiting for CVM to shut down
2023-08-26 00:37:36,416Z INFO change_cvm_display_name:196 Confirming if the CVM has been shut down
2023-08-26 00:37:36,579Z INFO change_cvm_display_name:263 CVM was shut down succesfully
2023-08-26 00:37:36,579Z INFO change_cvm_display_name:67 Running cmd: virsh domrename NTNX-350f3275-A-CVM NTNX-D-CVM on host
2023-08-26 00:37:51,687Z INFO change_cvm_display_name:67 Running cmd: virsh start NTNX-D-CVM on host
2023-08-26 00:38:09,616Z INFO change_cvm_display_name:67 Running cmd: virsh autostart NTNX-D-CVM on host
2023-08-26 00:38:24,793Z INFO change_cvm_display_name:284 Attempting to create a backup of the NTNX-CVM.xml file on host
2023-08-26 00:38:24,903Z INFO change_cvm_display_name:103 Creating new CVM XML config file
2023-08-26 00:38:24,903Z INFO change_cvm_display_name:105 Running cmd: virsh dumpxml NTNX-D-CVM > NTNX-CVM.xml on host
2023-08-26 00:38:25,057Z INFO change_cvm_display_name:111 Successful in creating the XML file for the CVM.
2023-08-26 00:38:25,057Z INFO change_cvm_display_name:297 CVM rename successful
```

Untuk mengganti hostname pada AHV Host/Hypervisor IP kita bisa menggunakan perintah berikut:

```bash
change_ahv_hostname --host_ip=<host-IP-address> --host_name=<new-host-name>
```

Jika kita eksekusi hasilnya seperti berikut:

```bash
nutanix@NTNX-ba60e5b2-A-CVM:192.168.88.32:~$ change_ahv_hostname --host_ip=192.168.88.22 --host_name=NTNX-AHV-B
2023-08-25 23:34:20,658Z INFO ahv_host_agent.py:230 Setting response time out None for host agent
2023-08-25 23:34:21,881Z INFO ahv_host_agent.py:741 Event listener thread started
2023-08-25 23:34:25,759Z INFO change_ahv_hostname:69 Host name is successfully updated

nutanix@NTNX-ba60e5b2-A-CVM:192.168.88.32:~$ change_ahv_hostname --host_ip=192.168.88.23 --host_name=NTNX-AHV-C
2023-08-25 23:34:35,959Z INFO ahv_host_agent.py:230 Setting response time out None for host agent
2023-08-25 23:34:37,161Z INFO ahv_host_agent.py:741 Event listener thread started
2023-08-25 23:34:40,890Z INFO change_ahv_hostname:69 Host name is successfully updated

nutanix@NTNX-ba60e5b2-A-CVM:192.168.88.32:~$ change_ahv_hostname --host_ip=192.168.88.24 --host_name=NTNX-AHV-D
2023-08-25 23:34:48,477Z INFO ahv_host_agent.py:230 Setting response time out None for host agent
2023-08-25 23:34:49,685Z INFO ahv_host_agent.py:741 Event listener thread started
2023-08-25 23:34:53,467Z INFO change_ahv_hostname:69 Host name is successfully updated
```

Setelah berhasil semuanya, kita bisa lihat vm name pada menu `VM -> tables` hasilnya seperti berikut:

![vm-list-host](imgs/05-prism-element/01d-vm-list-name.png)

## Setup Prism Element

Kemudian kita setup untuk Prism Element seperti:

1. Setup Cluste name
2. Setup Prism Element Virtual IP
3. Setup Prism Element iSCSI Data Services IP
4. Setup Prism Element FQDN
5. Setup DNS
6. Setup NTP

Untuk mengganti ClusterName kita bisa menggunakan command berikut:

```bash
ncli cluster edit-info new-name=<NewPCName>
```

Jika dijalankan maka hasilnya seperti berikut:

```bash
nutanix@NTNX-CVM-C:192.168.88.33:~$ ncli cluster edit-info new-name=DevOpsWithDimasMaryanto

    Cluster Id                : 000603c7-8584-365d-7469-0cc47a4138d2::8388249818958477522
    Cluster Uuid              : 000603c7-8584-365d-7469-0cc47a4138d2
    Cluster Name              : DevOpsWithDimasMaryanto
    Cluster Version           : 6.5.2
    Cluster Full Version      : el7.3-release-fraser-6.5.2-stable-f2ce4db7d67f495ebfd6208bef9ab0afec9c74af
    Node Count                : 3
    Block Count               : 3
    Shadow Clones Status      : Enabled
    Has Self Encrypting Disk  : no
    Cluster Masquerading I... :
    Cluster Masquerading PORT :
    Is registered to PC       : false
    Rebuild Reservation       : Disabled
    Encryption In Transit     : Disabled
    Is LTS                    : true
    External Data Services... :
    Support Verbosity Level   : BASIC_COREDUMP
    Lock Down Status          : Disabled
    Password Remote Login ... : Enabled
    Timezone                  : UTC
    On-Disk Dedup             : Disabled
    NCC Version               : ncc-4.6.2.1
    Common Criteria Mode      : Disabled
    Degraded Node Monitoring  : Enabled
```

Jika kita check hasilnya di menu `Settings -> Cluster Detail` seperti berikut:

![cluster-name-changed](imgs/05-prism-element/01e-changed-cluster-name.png)

Kemudian untuk setting Virtual IP, iSCSI Data Services IP bisa kita langsung edit seperti berikut:

![config-cluster-detail](imgs/05-prism-element/01f-cluster-detail-config.png)

Untuk memastikan cluster kita bisa connect ke internet, pastikan kita menambahkan dns google seperti `8.8.8.8, 8.8.4.4` di menu `Setting -> Name Servers` seperti berikut: 

![config-name-servers](imgs/05-prism-element/01g-config-name-servers.png)

Untuk memastikan sync timezone pada cluster, kita harus menambahkan NTP pada menu `Setting -> NTP Server` seperti berikut:

![config-ntp-server](imgs/05-prism-element/01h-config-ntp-server.png)