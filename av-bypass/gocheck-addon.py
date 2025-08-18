#!/usr/bin/env python
#####################################
# Installation module for Gocheck
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="gatariee"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Gocheck - AV evasion, implementation of DefenderCheck in Golang"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/gatariee/gocheck"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gocheck"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},wget https://github.com/gatariee/gocheck/releases/download/v1.5.0/gocheck32.exe ,wget https://github.com/gatariee/gocheck/releases/download/v1.5.0/gocheck64.exe"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"