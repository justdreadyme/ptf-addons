#!/usr/bin/env python
#####################################
# Installation module for various (OP) Packers
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Miscellaneous"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update various (OP) packers (AV evasion): CEXE, Kkrunchy, PEScrambler"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://raw.githubusercontent.com/Veil-Framework/Veil-Evasion/master/tools/pescrambler/PEScrambler.exe"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="packers"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="curl,upx-ucl,unzip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="curl,upx-ucl,unzip"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},timeout 300 curl -k -L -f "http://www.farbrausch.de/~fg/kkrunchy/kkrunchy_023a2.zip" > kkrunchy.zip,timeout 300 curl -k -L -f "https://web.archive.org/web/20160313071633/http://www.eskimo.com/~scottlu/win/cexe.exe" > cexe.exe,updatedb,unzip -q -o kkrunchy.zip,rm kkrunchy.zip,chmod +x *.exe,mkdir -p /usr/share/windows-resources/binaries/packers/,cp *.exe /usr/share/windows-resources/binaries/packers/"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
