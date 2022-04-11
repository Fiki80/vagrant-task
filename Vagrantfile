# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  config.vm.box = "generic/centos8"
  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "ansible/provision.yml"
    ansible.vault_password_file = "ansible/vault_pass"
  end

  config.vm.synced_folder ".", "/vagrant", create: true

end
