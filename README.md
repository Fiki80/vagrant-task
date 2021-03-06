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

Python web application, Grafana and Prometheus are running behind Nginx server configured as reverse proxy. Using Prometheus client library for Python, web application generates and exposes metrics to be scraped by Prometheus. Grafana is configured to source data from Prometheus and displays application's CPU utilization, RAM utilization and custom page visit counter. 
Python application also generates artificial CPU stress (around 50% usage on one CPU core) to emulate real application.

## Requirements

- [Vagrant](https://www.vagrantup.com)
- [VirtualBox](https://www.virtualbox.org)
- [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html)

## Usage

### Initial setup:
1. Install required dependencies.
2. Clone this repository
3. Use included Bash script 'pass_gen' to generate login credentials for Grafana web interface.
```
./pass_gen -u USER -p PASSWORD
```

4. To provision and start VM, cd inside the cloned repository and issue:
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

## Links
- https://github.com/prometheus/client_python
