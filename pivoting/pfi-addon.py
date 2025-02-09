#!/usr/bin/env python
#####################################
# Installation module for pfi
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Stephen A. Ridley (s7ephen)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update pfi ~ Port Forwarding Interceptor"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/s7ephen/pfi"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pfi"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python,python-tk"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python,python-tk"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# CREATE LAUNCHER
# cd {INSTALL_LOCATION},sudo python2 pfi.py
LAUNCHER=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

