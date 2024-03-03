<!--
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course
-->

# Practical cryptography course - Labs

## Setup

### Automated setup
In order to get started with the course labs, the following software components must be installed
on the user's host/physical computer:

- [HashiCorp Vagrant](https://developer.hashicorp.com/vagrant/downloads)
- [Virtualbox](https://www.virtualbox.org/)

Connect YubiKey via USB, open a command prompt in ["resources/labs"](%RESOURCES_ARCHIVE%) and run:

```
$ vagrant up
$ vagrant ssh -- ykman info
```

If successful, information such as the model and serial of the YubiKey should be outputted.


## Manual setup
Users who, for whatever reason, can't/prefer not to use Vagrant and/or VirtualBox may opt for
manual setup of the lab system. This can be done on a physical or virtual machine, provided that:

- It runs Ubuntu 22.04 LTS or a compatible derivative
- Supports attaching/forwarding USB devices

For manual setup, install [Ansible](https://www.ansible.com/) and run the Ansible playbook
"resources/labs/setup\_lab\_system.yml" against the target system.


## Common issues

### Enabling virtualisation support
Virtualisation software like VirtualBox relies on hardware features included in most processors.
These features are typically enabled by default, but some computer manufacturers require that they
are explicitly enabled.  
  
If the student is experiencing issues creating virtual machines, review "step one" and "step two"
in [Microsoft's virtualisation support documentation](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-11-pcs-c5578302-6e43-4b4b-a449-8ced115f58e1).


### "Incompatible character encodings"
Vagrant doesn't handle file system paths well with non-ASCII character/mixed character encoding.  
Users who encounter error messages such as "join: incompatible character encodings: CP850 and..."
have two options: create a new user account/file system path containing only ASCII characters (A-Z)
or reconfigure the Vagrant path settings, as documented below.  
  
On Windows, start a command prompt **as administrator** (right click "Run as administrator") and
execute the following commands:

```
$ md "C:\vagrant_data"
$ setx VAGRANT_HOME "C:/vagrant_data"
$ setx GEM_HOME "C:/vagrant_data"
$ takeown /a /r /f "C:\vagrant_data"
$ "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setproperty machinefolder "C:\vagrant_data"
```

Copy the "resources" directory into "C:\\vagrant\_data" and re-execute "vagrant up".


### USB forwarding on Linux
Linux users who encounter problems accessing their YubiKey inside a VirtualBox may not have the
appropriate privileges configured. A requirement to utilize the "USB forwarding" functionality
is to be a member of the "vboxusers" group - if this is not the case, execute the command below
and reboot the host system:

```
$ sudo usermod -a -G vboxusers "${USER}"
```
