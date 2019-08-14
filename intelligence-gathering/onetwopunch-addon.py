#!/usr/bin/env python
#####################################
# Installation module for onetwopunch
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Harold Rodriguez (superkojiman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update onetwopunch - A unicornscan & nmap wrapper"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/superkojiman/onetwopunch"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="onetwopunch"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,nmap,unicornscan"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,nmap,unicornscan"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
# TOOL_DEPEND="modules/vulnerability-analysis/nmap,modules/intelligence-gathering/unicornscan"

