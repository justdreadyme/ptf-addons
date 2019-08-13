#!/usr/bin/env python
#####################################
# Installation module for Wifiphisher
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Wifiphisher"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update wifiphisher - Rogue AP Framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wifiphisher/wifiphisher"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wifiphisher"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},updatedb,python setup.py install"

LAUNCHER=""
