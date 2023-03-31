<!--
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course - Password cracking lab
-->

# Practical cryptography course - Password cracking lab

## Scenario description
This is not your average corporate pentest - this time it's personal.  
  
After many long hours of crawling and scanning, you've finally hit the jackpot. Laying around on a
forgotten and dusty file share was a full system backup of the all important bastion host. "Why is
this host so damn important?" you may ask - well, it's used by administrators to manage the
Super Sensitive Production Database. A shell on that server would surely mean game-over.  
  
You peruse through the backup data and find "etc/shadow", a file used to store passwords for the
system's users. When scrolling through the list your heart suddenly stops for a second and the PTSD
hits. With a shattered voice, the cat in your lap hears a silent whisper:
"It can't be - it can't possible be. Oscar, freaking Oscar."  
  
A quick search on LinkedIn confirms your worst suspicion. Oscar, your childhood tormentor, has
started working as a developer at Xample Industries - the very same company you're auditing. The
stressful feeling is steadily replaced by a huger for revenge. You've been given the chance to
both impress the customer by hacking their crown jewel and in a subtle way get back at Oscar.  
  
What are you waiting for? Let's get cracking.


## Learning objectives
Practical knowledge of tools and techniques used for password recovery/cracking.


## Lab overview
The lab consist of a file called "shadow.bak" that contains salted and hashed passwords. The
password recovery tool "John The Ripper" (AKA "JtR" or simply John) should be used to extract
cleartext versions of the stored passwords. The utility has been packaged as a container image and
may be executed by running the wrapper script "john.sh", which has been included in the lab files.
  
In order to aid the password cracking process, the student should obtain and use a copy of the
popular "RockYou" dictionary/wordlist, which contains a large amount of leaked password.  
  
All tools required to complete the assignment should be pre-installed on the student's lab system. 


## Tasks

### Mandatory ("G")
- Obtain a copy of the "RockYou" password list (MD5 hash: 9076652d8ae75ce713e23ab09e10d9ee)
- Determine which hash types are used to store passwords in the file "shadow.bak"
- Use JtR ("john.sh") and the password list to crack Oscar's password
- Crack Bob's password by extending/permutating the password list (ends with =2022= or =2023=)


### Meritorious ("VG")
Use the "rules" functionality in "John The Ripper" _or_ create a custom script to extend/permutate
the "RockYou" wordlist for cracking the "root" user's password, based on the following information:
- System security requirements specify that the password must be at least 12 characters long
- Typically begins with a digit
- Typically ends with a dot (".") or the plus ("+") character


## Lab report/documentation
Each student should submit a lab report containing **at least** the following information ("G"):
- Documentation of which hash types were stored in the "shadow" file
- Description of which programs/commands/arguments were used to crack the password hashes
  
Optionally, describe three techniques/tricks that could be used to minimize the number of attempts
and increase likelihood of successful password recovery in 1000 characters or more ("VG").  
  
The lab report should be provided as a plain text file (".txt"), Markdown document or PDF file.

## Guidance and resources

### Documentation mismatch for JtR
JtR is an old tool which is available in several different versions. The configuration and
command-line syntax can be very different between these versions/forks, which may cause confusion
when researching the tool and how it should be utilized.  
  
The JtR version included in the lab container image is called "Jumbo". Make sure to include this
term when searching for information.

### Argument separation in JtR CLI
JtR supports many different command-line options. Options that support/require positional arguments
(such as "--config" which requires that the user specify a file) typically use the "equal"
character (or in rare cases the colon character) to separate these.

This means that an option such as "--wordlist" must be specified as "--wordlist=path/to/file" and
not "--wordlist path/to/file".

### Simple permutation of wordlists
JtR Jumbo supports a feature called "mask" to generate passwords on the fly based on a user
specified pattern, such as "three letters followed by a number". This feature can be combined with
the "wordlist" mode to easily create new permutations/versions of passwords stored in a password
list. When used in unison, it is typically called "stacked mask" or "hybrid stacked mask".

### File paths and the "john.sh" wrapper 
For ease of use, the JtR Jumbo version has been packaged in a container image in this lab. It can
be trivially executed by running the "john.sh" wrapper script, which basically just runs the
container image using Docker.  
  
In order to expose the lab files and a user obtained password list, the lab directory
("resources/labs/pwd\_crack") is bind-mounted ("exposed") into the container at the path "/data".
The lab directory is the only shared path between the lab system and the container.
  
The shared path "/data" is configured as the container's working directory, so as long as the
student specify relative search paths when running "john.sh" it should work as expected. In other
words, execution of a command such as "./john.sh --wordlist=foo.txt hashes.txt" will work, but not
"./john.sh --wordlist=/vagrant/pwd\_crack/foo.txt hashes.txt".


### Links
- [Official documentation for JtR Jumbo](https://github.com/openwall/john/tree/bleeding-jumbo/doc)
- [Documentation for rules feature](https://github.com/openwall/john/blob/bleeding-jumbo/doc/RULES)
- [Miloserdov - JtR "stacked/hybrid mask" feature](https://miloserdov.org/?p=5031#331)
- [shadow(5) - Linux manual page](https://www.man7.org/linux/man-pages/man5/shadow.5.html)
