# Kubernetes

There 2 method for installation Nutanix Kubernetes Platform:

1. Online Installation (you may experience some failures `error: coz maximum pull request from docker.io`)
    - Required stable & high speed internet access
    - Recommended using Bastion VM to provision NKP Kommander HOST

2. Offline Installation (Recommended)
    - DNS Server ([bind/bind9](https://www.isc.org/bind/), DNS Server on windows, DNS on Network appliance)
    - Private Registry ([Nexus OSS](https://www.sonatype.com/products/sonatype-nexus-oss-download), [distribution](https://distribution.github.io/distribution/), [harbor](https://goharbor.io/), etc...)
    - Recommended using Bastion VM to provision NKP Komander HOST
    - [Download bundle](https://portal.nutanix.com/page/downloads?product=nkp) image, tools, nkp-cli from nutainx portal.

So this article we will goes through step by step for *Enablement Nutanix Kubernetes Platform (NKP) with Offline Mode / Airgap*