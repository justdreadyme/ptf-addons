#!/usr/bin/env python
#####################################
# Installation module for Chimera
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="tokyoneon"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Chimera - PowerShell obfuscation script designed to bypass AMSI and commercial antivirus solutions"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/tokyoneon/Chimera"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="chimera"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,sed,xxd,libc-bin,curl,jq,perl,gawk,grep,coreutils"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,sed,xxd,libc-bin,curl,jq,perl,gawk,grep,coreutils"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: Bulk update of the hard-coded IP addresses in the "shells" folder: sed -i 's/192.168.56.101/<YOUR-IP-ADDRESS>/g' shells/*.ps1
AFTER_COMMANDS="cd {INSTALL_LOCATION},chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},chmod +x chimera.sh,sudo ln -sf {INSTALL_LOCATION}/chimera.sh /usr/local/bin/chimera"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"