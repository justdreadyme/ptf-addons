#!/usr/bin/env python
#####################################
# Installation module for AADInternals
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gerenios"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update AADInternals - PowerShell module for administering Azure AD and Office 365"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Gerenios/AADInternals"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="aadinternals"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,powershell"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,powershell"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: Not installed via PTF, but with "pswh" commands. Downloaded as a reference.
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"