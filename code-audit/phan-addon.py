#!/usr/bin/env python
#####################################
# Installation module for Phan
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="phan"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Phan - Phan is a static code analyzer for PHP"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/phan/phan/releases/latest/download/phan.phar"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="phan"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,php-ast"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,php-ast"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# NOTE: Create a ".phan/config.php" file, see also: https://github.com/phan/phan/wiki/Getting-Started#creating-a-config-file
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"