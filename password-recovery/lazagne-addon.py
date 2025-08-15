#!/usr/bin/env python
#####################################
# Installation module for LaZagne
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="AlessandroZ"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update LaZagne - Credentials recovery on a local computer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/AlessandroZ/LaZagne"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="lazagne"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,pyinstaller"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,pyinstaller"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: To compile the Windows EXE binary on Kali via Wine and Pyinstaller:
#   cd {INSTALL_LOCATION}
#   wine /home/kali/.wine/drive_c/Python312/python.exe -m pip install -U pyinstaller
#   wine /home/kali/.wine/drive_c/Python312/Scripts/pyinstaller.exe --additional-hooks-dir=. -F --onefile Windows/laZagne.py
AFTER_COMMANDS="cd {INSTALL_LOCATION},wget https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.7/LaZagne.exe"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"