# Vagrant-task

This repository contains code to build a simple webserver using Vagrant and Ansible. Vagrant will set up virtual machine based on Centos 8 linux. Ansible will take care of provision and configuration of all the tools listed below.

Following components will be installed in the target VM:

* Centos8
* Nginx
* Grafana
* Prometheus

## Prerequisities

Vagrant has to be installed on the host machine. In case of running VM on local machine, VirtualBox has to be present.

## Build

After cloning this repository simply issue:
'vagrant up'

Vault password can be found in ansible/vault_pass file.
