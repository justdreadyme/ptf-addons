#!/usr/bin/env python
###################################################
# Installation module for Yet Another Nessus Parser
###################################################

# AUTHOR OF MODULE NAME
AUTHOR="Alessandro Di Pinto"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Yet Another Nessus Parser - a Nessus results parsing tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/adipinto/yet-another-nessus-parser"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="yanp"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="python"

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION}, updatedb && sed -i 's/if len(pluginid) != 5 or not pluginid.isdigit():/if (len(pluginid) != 5 and len (pluginid) != 6) or not pluginid.isdigit():/' {INSTALL_LOCATION}yanp.py"

# create a launcher
LAUNCHER="yanp"
