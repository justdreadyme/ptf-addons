#!/usr/bin/env python
#####################################
# Installation module for osint-framework
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="lockFALE"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update osint-framework - OSINT Framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/lockfale/osint-framework"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="osint-framework"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,npm"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,npm"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},updatedb,npm install"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="osint-framework"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

