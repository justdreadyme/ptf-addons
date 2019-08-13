#!/usr/bin/env python
#####################################
# Installation module for JSP File Browser ~ JSP Web Shell
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Tobi von Loesch"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update JSP File Browser - JSP Web Shell"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.vonloesch.de/files/browser.zip"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="jsp-filebrowser"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="unzip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="unzip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},updatedb,unzip browser.zip,rm browser.zip"

# LAUNCHER
LAUNCHER=""
