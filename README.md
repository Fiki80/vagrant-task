# Vagrant-task

This repository contains code to build a simple webserver using Vagrant and Ansible. Vagrant will set up virtual machine based on Centos8 linux and runs Virtualbox as default provider. This virtual machine serves as a demonstration of running Python application on server, it's monitoring and providing graphical view of collected metrics.

Provided Ansible roles will take care of deployment and configuration of all the tools listed below.

Following components will be installed in the target VM:

* Centos8
* NGINX
* Grafana
* Prometheus
* Python3 application


## Architectural overview

Python web application, Grafana and Prometheus are running behind Nginx server configured as reverse proxy. Access locations to Grafana and web application are described in the paragraphs below.

## Requirements

- [Vagrant](https://www.vagrantup.com)
- [VirtualBox](https://www.virtualbox.org)
- [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html)

## Usage

### Initial setup:
1. Install required dependencies.
2. Use included Bash script 'pass_gen' to generate login credentials for Grafana web interface.
```
./pass_gen -u USER -p PASSWORD
```

3. To provision and start VM, issue:
```
vagrant up
```

### Grafana web interface
Grafana web interface can be accessed via: 
```
http://localhost:8080/grafana
```

Pre-configured dashboard displaying web app's metrics:
```
http://localhost:8080/grafana/dashboard
```

### Web application
Python application displaying page visit counter is accessible via:
```
http://localhost:8080/app
```


### Destroying VM
To destroy created virtual machine issue command:
```
vagrant destroy
```
