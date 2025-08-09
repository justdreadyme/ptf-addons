#!/usr/bin/env python
#####################################
# Installation module for DeTTECT
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Rabobank CDC"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DeTTECT - Detect Tactics, Techniques & Combat Threats"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/rabobank-cdc/DeTTECT"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dettect"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},virtualenv venv,/bin/bash -c 'source {INSTALL_LOCATION}/venv/bin/activate && pip3 install -r requirements.txt && deactivate',chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#!/bin/bash' > launcher,echo cd {INSTALL_LOCATION} >> launcher,echo source {INSTALL_LOCATION}/venv/bin/activate \&\& python3 dettect.py \"\$\@\" \&\& deactivate >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/dettect"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
# Use the generated layer files on the following URL: https://mitre-attack.github.io/attack-navigator/#comment_underline=false&metadata_underline=false
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"