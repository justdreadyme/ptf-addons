#!/usr/bin/env python
#####################################
# Installation module for GCPBucketBrute
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="RhinoSecurityLabs"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update GCPBucketBrute - Enumerate Google Storage buckets"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/RhinoSecurityLabs/GCPBucketBrute"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gcpbucketbrute"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python3-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python3-pip"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},virtualenv venv,/bin/bash -c 'source {INSTALL_LOCATION}/venv/bin/activate && chmod +x *.py && pip3 install -r requirements.txt && deactivate',chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#!/bin/bash' > launcher,echo 'cd' '{INSTALL_LOCATION}' >> launcher,echo source {INSTALL_LOCATION}/venv/bin/activate \&\& python gcpbucketbrute.py \"\$\@\" \&\& deactivate >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/gcpbucketbrute"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="gcpbucketbrute"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

