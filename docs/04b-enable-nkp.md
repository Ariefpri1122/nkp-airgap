# Nutanix Kubernetes Platform (NKP)

Since middle of 2023, Nutanix discontinue development for Nutanix Kubernetes Engine (NKE) then 2024 will end of support for it. So the next up is we need move to Nutanix Kubernetes Platform (NKP).

To enable NKP is not strigh forward as Nutanix Kubernetes Engine which just one click there is several requirement you should meet, so what the requirement to enable NKP:

- AOS version, atleast `6.8.1`
    - tested `6.10` at Nutanix CE & Enterpise
- Prism Central, atleast `2024.2` or newer
    - tested `2024.1` at Nutanix Enterprise
    - tested `2024.2` at Nutanix CE & Enterprise

There 2 method for installation Nutanix Kubernetes Platform:

1. Online Installation (you may experience some failures `error: coz maximum pull request from docker.io`)
    - Required stable & high speed internet access
    - Recommended using Bastion VM to provision NKP Kommander HOST

2. Offline Installation (Recommended)
    - DNS Server ([bind/bind9](https://www.isc.org/bind/), DNS Server on windows)
    - Private Registry ([Nexus OSS](https://www.sonatype.com/products/sonatype-nexus-oss-download), [distribution](https://distribution.github.io/distribution/), [harbor](https://goharbor.io/), etc...)
    - Recommended using Bastion VM to provision NKP Komander HOST
    - [Download bundle](https://portal.nutanix.com/page/downloads?product=nkp) image, tools, nkp-cli from nutainx portal.

So this article we will goes through step by step for *Enablement Nutanix Kubernetes Platform (NKP) with Offline Mode / Airgap*

## Upgrade Infrastructure

As i mension previously there is several requirement to enable Nutanix Kubernetes Platform from instrastructure prospective is Updated Nutanix Cloud Platform Software (AOS & Prism Central). **If you have done it before you can skip this step**, if not please upgrade Prism Central first with following upgrade path:

Example how if currently the Prism Central has `2022.6.x` please find the way to upgrade to `2024.2` or later, So if you see Upgrade path from nutanix portal roadmap is you need to upgrade to `2023.x` then `2024.2` look like this

![pc-upgrade-path](./imgs/07-nkp/01-pc-upgrade-path.png)

After Prism Central successfully upgrade, then you can upgrade the AOS version. If you currently running `6.5.6.6` then you can upgrade to `6.10`

![pe-aos-upgrade-path](./imgs/07-nkp/01-pe-aos-upgrade-path.png)

Also you need to upgrade AHV version to `AHV-20230302.102001`

![pe-ahv-upgrade](./imgs/07-nkp/01-pe-ahv-upgrade.png)

Please consult to us, if you have any trouble

## Private registry

