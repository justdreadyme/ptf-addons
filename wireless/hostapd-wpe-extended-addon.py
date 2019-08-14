#!/usr/bin/env python
#####################################
# Installation module for hostapd-wpe-extended
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Matthias Larisch (NerdyProjects)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update hostapd-wpe-extended - Rogue AP for WPA-Enterprise"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/NerdyProjects/hostapd-wpe-extended"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hostapd-wpe-extended"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
