#!/usr/bin/env python
#####################################
# Installation module for Wifite
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Pentester Academy"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Airodump-ng WiFi Scan Visualizer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/pentesteracademy/airodump-scan-visualizer"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="airodump-scan-visualizer"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},updatedb,mkdir -p /var/www/html/Airodump/,cp -r * /var/www/html/Airodump/"

LAUNCHER="airodump-scan-visualizer"
