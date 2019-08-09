#!/usr/bin/env python
#####################################
# Installation module for entire set of Sysinternals Utilities
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Sysinternals"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update the entire Sysinternals Utilities"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://download.sysinternals.com/files/SysinternalsSuite.zip"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sysinternals"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="curl,unzip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="curl,unzip"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},unzip -j -o SysinternalsSuite.zip,rm SysinternalsSuite.zip,updatedb,mkdir -p /usr/share/windows-resources/binaries/sysinternals/,rm Eula.txt,chmod +x *.exe,cp -r * /usr/share/windows-resources/binaries/sysinternals/"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="sysinternals"

