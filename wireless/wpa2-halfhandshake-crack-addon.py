#!/usr/bin/env python
#####################################
# Installation module for WPA2 HalfHandshake Crack
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dylan Ayrey (dxa4481)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update WPA2 HalfHandshake Crack - Rogue AP for handshakes without an AP"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dxa4481/WPA2-HalfHandshake-Crack"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wpa2-halfhandshake"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
# cd {INSTALL_LOCATION}, sudo python2 halfHandshake.py
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
