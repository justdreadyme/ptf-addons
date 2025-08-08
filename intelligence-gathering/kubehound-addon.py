#!/usr/bin/env python
#####################################
# Installation module for KubeHound
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="DataDog"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update KubeHound - Tool for building Kubernetes attack paths"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/DataDog/KubeHound"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="kubehound"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},git checkout $(git describe --tags --abbrev=0),make build,sudo ln -sf {INSTALL_LOCATION}/bin/build/kubehound /usr/local/bin/kubehound"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"