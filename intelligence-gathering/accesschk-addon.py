#!/usr/bin/env python
#####################################
# Installation module for AccessChk (32/64-bit and legacy version)
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Sysinternals"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update AccessChk (checking of Windows file, folder and service permissions)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://download.sysinternals.com/files/AccessChk.zip"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="accesschk"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="curl,unzip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="curl,unzip"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},unzip -j -o AccessChk.zip,rm AccessChk.zip,updatedb,mv accesschk.exe accesschk32.exe,timeout 300 curl --progress -k -L -f "https://web.archive.org/web/20080530012252/http://live.sysinternals.com/accesschk.exe" > {INSTALL_LOCATION}/accesschk_v5.02.exe,rm Eula.txt,mkdir -p /usr/share/windows-resources/binaries/accesschk/,cp * /usr/share/windows-resources/binaries/accesschk/"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

