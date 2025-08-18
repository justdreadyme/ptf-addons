#!/usr/bin/env python
#####################################
# Installation module for DefenderCheck
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="matterpreter"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DefenderCheck - Identifies the bytes that Microsoft Defender flags on"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/matterpreter/DefenderCheck"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="defendercheck"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: Compile with Visual Studio (disable Real-time Protection in Defender before compiling)
# NOTE: Check the file offset reported by DefenderCheck, with Kali: hexdump -C <file> -s <offset_in_hex>
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"