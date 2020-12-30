#!/usr/bin/env python
###################################################
# Installation module for Yet Another Nessus Parser
###################################################

# AUTHOR OF MODULE NAME
AUTHOR="InfosecMatter"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Yet Another Nessus Parser - a Nessus CSV results parsing tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/InfosecMatter/Scripts.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="yanp"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},rm firebird-bruteforce.sh,rm portsweep.ps1"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="yanp"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""