# Nutanix Kubernetes Platform (NKP)

Since middle of 2023, Nutanix discontinue development for Nutanix Kubernetes Engine (NKE) then 2024 will end of support for it. So the next up is we need move to Nutanix Kubernetes Platform (NKP).

To enable NKP is not strigh forward as Nutanix Kubernetes Engine which just one click there is several requirement you should meet, so what the requirement to enable NKP:

1. Online Installation
    - Required stable & high speed internet access
    - Recommended using Bastion VM to provision NKP Kommander HOST

2. Offline Installation
    - DNS Server
    - Private Registry (Nexus OSS, opendistribution.io, harbor, etc...)
    - Recommended using Bastion VM to provision NKP Komander HOST
    - Download bundle image, tools, nkp-cli from nutainx portal.