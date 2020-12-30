#!/usr/bin/env python
#####################################
# Installation module for Gitrob
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update Gitrob" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/michenriksen/gitrob/releases/download/v2.0.0-beta/gitrob_linux_amd64_2.0.0-beta.zip" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gitrob"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="unzip" 

# DEPENDS FOR FEDORA INSTALLS
FEDORA="unzip"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},unzip gitrob*.zip,rm gitrob*.zip"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="gitrob"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

