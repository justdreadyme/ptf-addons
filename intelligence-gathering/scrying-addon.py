#!/usr/bin/env python
#####################################
# Installation module for Scrying
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="NCC Group"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update scrying - Tool for collecting RDP, web and VNC screenshots all in one place"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/nccgroup/scrying/releases/download/v0.9.2/scrying_0.9.2_amd64.deb"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="scrying"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},dpkg -i scrying*.deb,wget https://github.com/openssl/openssl/releases/download/OpenSSL_1_1_1w/openssl-1.1.1w.tar.gz,tar -zxvf openssl-1.1.1w.tar.gz,cd openssl-1.1.1w,./config,make,make test,sudo cp libssl.so.1.1 libcrypto.so.1.1 /usr/lib/i386-linux-gnu/,sudo cp libssl.so.1.1 libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/,cd {{INSTALL_LOCATION}},rm -rf openssl-1.1.1w/"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE

BYPASS_UPDATE="YES"
