# Ansible Dev Setup

## Installing latest ansible (v10) on Debian (bookworm)

```bash
./install-debian.sh
```

## Configure Ansible Inventory at /etc/ansible/hosts

example /etc/ansible/hosts file:

```yml
---
all:
  hosts:
    localhost:
      ansible_connection: local
      ansible_user: bennie
      ansible_os_family: Debian
      ansible_ssh_private_key_file: ~/.ssh/id_ed25519
      ansible_python_interpreter: /usr/bin/python3
```

## Running the (main) playbook

```bash
ansible-playbook main.yml -K
```
