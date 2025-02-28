<!--
SPDX-FileCopyrightText: © 2025 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course
-->

# Practical cryptography course - Labs


## Setup
The course labs have been tested on Ubuntu 24.04 LTS. The documentation below describes three
methods for setting up a student's lab environment:

1. "Native setup": Recommended for students running Ubuntu 24.04 LTS on a physical/virtual machine
2. "Non-native setup": Recommend for students running Windows/MacOS on their physical machine
3. "Manual setup": Available for students running other Linux distributions/operating systems


### Alt. 1: Native setup
The "native setup" method can be used on a physical or virtual machine, provided that it:

- Runs Ubuntu 24.04 LTS or a compatible derivative
- Supports attaching/forwarding USB devices (required for non-graded exercises)

To automate the installation/configuration of tools required to complete the course labs, install
[Ansible](https://www.ansible.com/) and run the Ansible playbook
["resources/labs/setup\_lab\_system.yml"](%RESOURCES_ARCHIVE%) on the target system:

```
$ sudo apt update && sudo apt install ansible --no-install-recommends 
$ ansible-playbook -v -c local resources/labs/setup_lab_system.yml 
```


### Alt. 2: Non-native setup
Students running operating systems other than Ubuntu 24.04 LTS or that desire to have an isolated
environment for course labs may utilize the "non-native setup" method, in which all tools required
to complete the exercises are automatically setup in a virtual machine.  
  
The following software components must be installed on the user's host/physical computer:

- [HashiCorp Vagrant](https://developer.hashicorp.com/vagrant/downloads)
- [Virtualbox](https://www.virtualbox.org/) or other compatible Vagrant provider

Once the dependencies described above have been installed/configured, open a command line prompt,
navigate to the ["resources/labs"](%RESOURCES_ARCHIVE%) directory and run the following commands:

```
$ vagrant up
$ vagrant ssh
```

To validate automatic forwarding of YubiKeys into the virtual machine (VirtualBox only), connect 
a YubiKey 5 to a USB port, open a command line prompt, navigate to the
["resources/labs"](%RESOURCES_ARCHIVE%) directory and executed the following commands:

```
$ vagrant up
$ vagrant ssh -- ykman info
```

If successful, information such as the model and serial of the YubiKey should be outputted.
Users of Vagrant providers other than VirtualBox may need to configure USB forwarding manually.


### Alt. 3: Manual setup
Students who are using alternative operating systems/Linux distributions and don't wish setup their
lab environment in a virtual machine may utilize the "manual setup" method.  

For guidance regarding required utilities and their configuration, review the tasks in
["resources/labs/setup\_lab\_system.yml"](%RESOURCES_ARCHIVE%) and adapt them to the target
environment.


## Common issues


### Problems starting Vagrant VM
The most common issue type student experience is problems accessing their VM when executing the
command "vagrant up". This typically occurs when the command is not executed in the correct
directory. Before issuing any Vagrant commands, ensure that the current working directory is the
course "labs" folder:

```
$ cd /my/path/to/practical_cryptography_course/resources/labs
```


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


### "Permission denied" when using Gitbash
On a Windows system, Vagrant commands should not be executed in a "Gitbash" shell as it has known
compatibility issues, especially related to SSH authentication to the guest VM. If possible,
utilize a PowerShell prompt or the ["Windows Terminal" app](https://aka.ms/terminal) instead.


### USB forwarding on Linux
Linux users who encounter problems accessing their YubiKey inside a VirtualBox may not have the
appropriate privileges configured. A requirement to utilize the "USB forwarding" functionality
is to be a member of the "vboxusers" group - if this is not the case, execute the commands below
on the host/physical system:

```
$ sudo usermod -a -G vboxusers "${USER}"
$ sudo reboot
```
