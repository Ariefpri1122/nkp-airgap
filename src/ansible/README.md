## Using this Ansible Playbook

Pertama kita clone dulu repository ini, dengan perintah berikut:

```bash
git clone https://github.com/dimMaryanto93/ntnx-ncs-core.git --depth 1 && \
cd ntnx-ncs-core/src/ansible ## masuk ke folder ansible
```

Setelah itu kita perlu install dependency dengan menggunakan perintah berikut:

```bash
ansible-galaxy role install -r requirements.yaml --force && \
ansible-galaxy collection install -r requirements.yaml --force
```