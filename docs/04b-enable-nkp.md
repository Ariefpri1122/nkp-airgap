# Nutanix Kubernetes Platform (NKP)

Since middle of 2023, Nutanix discontinue development for Nutanix Kubernetes Engine (NKE) then 2024 will end of support for it. So the next up is we need move to Nutanix Kubernetes Platform (NKP).

To enable NKP is not strigh forward as Nutanix Kubernetes Engine which just one click there is several requirement you should meet, so what the requirement to enable NKP:

- AOS version, atleast `6.8.1`
    - tested `6.10` at Nutanix CE & Enterpise
- Prism Central, atleast `2024.2` or newer
    - tested `2024.1` at Nutanix Enterprise
    - tested `2024.2` at Nutanix CE & Enterprise

There 2 method for installation Nutanix Kubernetes Platform:

1. Online Installation (may failed expiriances)
    - Required stable & high speed internet access
    - Recommended using Bastion VM to provision NKP Kommander HOST

2. Offline Installation (Recommended)
    - DNS Server ([bind/bind9](https://www.isc.org/bind/), DNS Server on windows)
    - Private Registry ([Nexus OSS](https://www.sonatype.com/products/sonatype-nexus-oss-download), [distribution](https://distribution.github.io/distribution/), [harbor](https://goharbor.io/), etc...)
    - Recommended using Bastion VM to provision NKP Komander HOST
    - [Download bundle](https://portal.nutanix.com/page/downloads?product=nkp) image, tools, nkp-cli from nutainx portal.

    So this article we will goes through step by step for *Enablement Nutanix Kubernetes Platform (NKP)*