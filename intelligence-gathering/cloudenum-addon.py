#!/usr/bin/env python
#####################################
# Installation module for cloudenum
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="initstring"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update cloudenum - Multi-cloud OSINT"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/initstring/cloud_enum"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="cloudenum"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,pip3"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,pip3"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},updatedb,pip3 install -r ./requirements.txt"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="cloudenum"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

