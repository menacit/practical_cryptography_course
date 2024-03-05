---
SPDX-FileCopyrightText: © 2024 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0

title: "Practical cryptography course: Symmetric encryption tools"
author: "Joel Rangsmo <joel@menacit.se>"
footer: "© Course authors (CC BY-SA 4.0)"
description: "Demonstration of symmetrical encryption tools"
keywords:
  - "cryptology"
  - "cryptography"
  - "practical"
  - "encryption"
  - "course"
color: "#ffffff"
class:
  - "invert"
style: |
  section.center {
    text-align: center;
  }

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
## Symmetric encryption tools
### Let there be demos!

![bg right:30%](images/07-chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Fritzchens Fritz (CC0 1.0)" -->
## Simple file encryption
```
$ cat my_secrets.txt 
I didn't shoot the sheriff...

$ ccrypt --encrypt --key "hunter2" my_secrets.txt 
$ file my_secrets.txt.cpt 
my_secrets.txt.cpt: data

$ ccrypt --decrypt --key "hunter2" my_secrets.txt.cpt
$ cat my_secrets.txt 
I didn't shoot the sheriff...
```

![bg right:30%](images/07-abstract_chip.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Loco Steve (CC BY-SA 2.0)" -->
## LUKS
- Standard for encryption at the block layer
- "Full Disk Encryption" on Linux
- Supports multiple "keyslots"
- Typically used via the "cryptsetup" utility

![bg right:30%](images/07-train.jpg)

---
![bg center 70%](images/07-gnome_disks.png)

---
![bg center 70%](images/07-gnome_disks_format.png)

---
![bg center 60%](images/07-gnome_disks_format_options.png)

---
![bg center 60%](images/07-gnome_disks_select_passphrase.png)

---
![bg center 70%](images/07-gnome_unlock_disk.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
## BitLocker
- Introduced in Windows Vista (2007)
- Not available in "Home" editions\*
- Supports encryption of boot and data drives

![bg right:30%](images/07-red_windows.jpg)

---
![bg center 70%](images/07-bitlocker_start.png)

---
![bg center 55%](images/07-bitlocker_configure_external.png)

---
![bg center 55%](images/07-bitlocker_encrypting_external.png)

---
![bg center 45%](images/07-bitlocker_mount_external.png)

---
![bg center 55%](images/07-bitlocker_reconfigure_external.png)

---
![bg center 55%](images/07-bitlocker_overwrite_internal.png)

---
![bg center 55%](images/07-bitlocker_backup_key_internal.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Jonathan Torres (CC BY 4.0)" -->
## VeraCrypt
- Fork of ["TrueCrypt"](https://en.wikipedia.org/wiki/TrueCrypt)
- FOSS and publicly audited
- Cross-platform
- Supports encryption of boot\*, data drives and "virtual devices"

![bg right:30%](images/07-cyborg.jpg)

---
![bg center 55%](images/07-veracrypt_home.png)

---
![bg center 70%](images/07-veracrypt_select_drive_external.png)

---
![bg center 65%](images/07-veracrypt_choose_external_algo.png)

---
![bg center 55%](images/07-veracrypt_benchmark.png)

---
![bg center 70%](images/07-veracrypt_benchmark_result_zoomed.png)

---
![bg center 70%](images/07-veracrypt_benchmark_aesni_zoomed.png)

---
![bg center 70%](images/07-veracrypt_choose_external_password.png)

---
![bg center 70%](images/07-veracrypt_format_external.png)

---
![bg center 70%](images/07-veracrypt_decrypt_external.png)

---
![bg center 55%](images/07-veracrypt_decrypt_loading_external.png)

---
![bg center 65%](images/07-veracrypt_mounted_external.png)

---
![bg center 65%](images/07-veracrypt_create_virtual.png)

---
![bg center 65%](images/07-veracrypt_select_hidden_volume.png)

---
![bg center 65%](images/07-veracrypt_choose_volume_outer_password.png)

---
![bg center 65%](images/07-veracrypt_select_volume_file.png)

---
![bg center 65%](images/07-veracrypt_enter_volume_password.png)

---
![bg center 65%](images/07-veracrypt_outer_content_list.png)

---
![bg center 65%](images/07-veracrypt_outer_secret_content.png)

---
![bg center 65%](images/07-veracrypt_enter_volume_password.png)

---
![bg center 65%](images/07-veracrypt_inner_content_list.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Helsinki Hacklab (CC BY 2.0)" -->
# [XKCD: 538](https://xkcd.com/538/)

![bg right:30%](images/07-led_smile.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% George N (CC BY 2.0)" -->
## KeePassXC
- Offline password/secrets manager
- FOSS and cross-platform
- Compatible with other KeePass variants\*

![bg right:30%](images/07-laser.jpg)

---
![bg center 65%](images/07-keepass_home.png)

---
![bg center 65%](images/07-keepass_create_database.png)

---
![bg center 65%](images/07-keepass_algos_simple.png)

---
![bg center 65%](images/07-keepass_algos_advanced.png)

---
![bg center 65%](images/07-keepass_configure_creds.png)

---
![bg center 65%](images/07-keepass_unlock_password.png)

---
![bg center 65%](images/07-keepass_unlock_yk.png)

---
![bg center 65%](images/07-keepass_list_entries.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
## Up1
- Web-based file hosting service
- FOSS!
- Try it at ["Riseup Share"](https://share.riseup.net/)
- Performs cryptography tasks in the browser ("client-side")

![bg right:30%](images/07-full_moon.jpg)

---
![bg center 65%](images/07-up1_home.png)

---
![bg center 65%](images/07-up1_upload_dialog.png)

---
![bg center 65%](images/07-up1_uploading.png)

---
![bg center 65%](images/07-up1_downloading.png)

---
![bg center 65%](images/07-up1_downloaded_content.png)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% Halfrain (CC BY-SA 2.0)" -->
share.riseup.net/**#6nV4VONZwLr7nhBkd5gML**

![bg right:30%](images/07-full_moon.jpg)

---
<!-- _footer: "%ATTRIBUTION_PREFIX% RoboticSpider (CC BY 4.0)" -->
## Bonus tip! ("fulhack")

![bg right:30%](images/07-sad_robot.jpg)

---
![bg center 60%](images/07-yubikey_manager_home.png)

---
![bg center 60%](images/07-yubikey_manager_configure_otp.png)

---
![bg center 60%](images/07-yubikey_manager_configure_long_slot.png)

---
![bg center 60%](images/07-yubikey_manager_select_static.png)

---
![bg center 60%](images/07-yubikey_manager_program_static.png)

---
![bg center 70%](images/07-yubikey_manager_static_output.png)
