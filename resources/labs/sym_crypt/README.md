<!--
SPDX-FileCopyrightText: © 2023 Menacit AB <foss@menacit.se>
SPDX-License-Identifier: CC-BY-SA-4.0
X-Context: Practical cryptography course - Symmetric file encryption lab
-->

# Practical cryptography course - Symmetric file encryption lab

## Scenario description
Backups - can't live with 'em, can't live without 'em, am I right? Everyone has some precious data,
mayhaps it's that huge pile of baby photos that no one will every revisit or a meticulously
organized collection of totally legitimately obtained eurodisco MP3s. It's the same story for most
enterprises, only far more of a snooze fest.  
  
Examplify Inc. learned the importance of backups the hard way and now they are almost overdoing it.
Flash drives and tapes have been scattered all over the office containing highly sensitive backup
data. One of these drives got lost during spring cleaning, causing tons of gastric ulcers within
the security team.  
  
In your resume, you've listed "shell scripting" as a skill, hmm? Time to put that claim to the test
and implement some military-grade encryption in the backup utility.


## Learning objectives
Practical knowledge of symmetric encryption for file storage.


## Lab overview
The lab consist of an example bash script that can be used to backup and restore files called
"backup\_and\_restore.sh". In addition, the included script "generate\_test\_files.sh" can be used
to populate the backup source directory with example files.  
  
In order to complete the lab, the student should add encryption capabilities to the backup/restore
script. All tools required to complete the assignment should be pre-installed on the student's lab
system.


## Tasks
- Modify the backup/restore script to store backups in AES-256 encrypted 7-Zip archives


## Lab report/documentation
Each student should submit a lab report containing **at least** the following information:
- Documentation of changes made in the backup/restore script to implement encryption
- Demonstration of how the implemented changes improve security of the service ("before and after")
  
The lab report should be provided as a plain text file (".txt"), Markdown document or PDF file.
In addition to the report, all lab files that have been changed (scripts, configuration sets, etc.)
should be provided as a ZIP or GZIP archive. **Example backup files should not be included**.
  
Send lab report and archive of changed files in an email to:  
[courses+crypto-sym\_crypt\_lab@%EMAIL_DOMAIN%](mailto:courses+sym_crypt_lab@%EMAIL_DOMAIN%)


## Guidance and resources

### Usage of debug logging
The backup/restore shell script provides a logging function. If the environment variable
"LOG\_LEVEL" is set to "DEBUG", the script will include verbose debug messages in script output.
Usage of the debug logging level is recommended if sensitive information, such as passwords or
keys, needs to be included in log messages for problem analysis/investigation.


### Avoid hard-coding passwords
It is generally consider a bad/unsafe practice to store credentials, such as a passwords and API
keys, as hard-coded values in scripts/application source code. These should instead be provided
through runtime configuration options, such as environment variables or a settings file.


### Links
- [Man page: "tar" command](https://linux.die.net/man/1/tar)
- [Man page: "7z" command](https://linux.die.net/man/1/7z)
- [Environment variable HOWTO guide](https://www.cyberciti.biz/faq/set-environment-variable-linux/)
