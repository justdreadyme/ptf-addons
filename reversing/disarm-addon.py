#!/usr/bin/env python
#####################################
# Installation module for DisARM
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jonathan Levin"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DisARM - Disassembler and Binary Analyzer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://newosxbook.com/tools/disarm.tar"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="disarm"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: For most (Kali) Linux systems, use ./binaries/disarm.linux.x86_64
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar -xvf disarm.tar"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"