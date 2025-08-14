#!/usr/bin/env python
#####################################
# Installation module for Drozer
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="ReversecLabs"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Drozer - The leading security assessment framework for Android"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ReversecLabs/drozer"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="drozer"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: Also requires the Drozer Agent, see "modules/mobile-analysis/drozer-agent-addon"
AFTER_COMMANDS="cd {INSTALL_LOCATION},virtualenv venv,/bin/bash -c 'source {INSTALL_LOCATION}/venv/bin/activate && pip install . && deactivate',chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#\!/bin/bash' > launcher,echo 'cd' '{INSTALL_LOCATION}' >> launcher,echo source {INSTALL_LOCATION}/venv/bin/activate \&\& {INSTALL_LOCATION}/venv/bin/drozer \\\"\\\$\\\@\\\" \&\& deactivate >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/drozer"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"