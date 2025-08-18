#!/usr/bin/env python
#####################################
# Installation module for IPATool
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="majd"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update IPATool - Command-line tool that allows searching and downloading app packages (IPA files) from the iOS App Store"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/majd/ipatool"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ipatool"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: You need to use the App Store once with the Apple ID on any iOS device before you can use it with ipatool
AFTER_COMMANDS="cd {INSTALL_LOCATION},go build -o ipatool,chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},chmod +x {INSTALL_LOCATION}/ipatool,sudo ln -sf {INSTALL_LOCATION}/ipatool /usr/local/bin/ipatool"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE

BYPASS_UPDATE="YES"
