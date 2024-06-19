# Ansible Dev Setup

## Installing latest ansible (v10) on Debian (bookworm)

```bash
./install-debian.sh
```

## SSH Authentication

ssh authentication is preferred since it will not require a password and somehow is still more secure.

Create an ssh key pair, if needed, and add the public key to ~/.ssh/authorized_keys.

_Remember to chmod 600 ~/.ssh/authorized_keys._

Include the path to the private key in the inventory for localhost below.

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
