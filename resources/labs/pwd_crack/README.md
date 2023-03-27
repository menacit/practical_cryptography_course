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
The lab consist of two files typically found on a Linux system:
- "passwd": Contains list of configured users on the host
- "shadow": Contains salted and hashed passwords for users in the "passwd" file 
  
In order to complete the lab, a wordlist and the password recovery program "John The Ripper"
(AKA "john") should be used to obtain cleartext versions of passwords stored in the "shadow" file.
All tools required to complete the assignment should be pre-installed on the student's lab system. 


## Tasks

### Mandatory ("G")
- Obtain a copy of the "RockYou" password list (any version)
- Use the "unshadow" and "john" utility to crack Oscar's password
- Use the "unshadow" and "john" utility to crack Bob's password (has suffix/ends with 2022 or 2023)


### Meritorious ("VG")
Use the "Rules" functionality in "John The Ripper" or a create custom script to extend the
"RockYou" wordlist for cracking the "root" user's password, based on the following information:
- Minimum twelve characters long
- Typically begins a digit
- Typically ends with the plus character ("+") or a dot (".") 


## Lab report/documentation
Each student should submit a lab report containing **at least** the following information ("G"):
- Description of which programs/commands were used to crack the password hashes
  
Optionally, describe the three techniques/rules that could be used to minimize the number of
attempts and increase likelihood of successful password recovery in 1000 characters or more ("VG)".  
  
The lab report should be provided as a plain text file (".txt"), Markdown document or PDF file.
Upload lab report and archive of changed files to %REPORT_TARGET%.
