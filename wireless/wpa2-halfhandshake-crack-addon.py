#!/usr/bin/env python
#####################################
# Installation module for WPA2 HalfHandshake Crack
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dylan Ayrey (dxa4481)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update WPA2 HalfHandshake Crack - Rogue AP for handshakes without an AP"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dxa4481/WPA2-HalfHandshake-Crack"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wpa2-halfhandshake"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},virtualenv venv,/bin/bash -c 'source {INSTALL_LOCATION}/venv/bin/activate && curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && python2.7 get-pip.py && python2.7 -m pip install setuptools && python2.7 -m pip install pypcapfile && python2.7 -m pip install pbkdf2_ctypes && python2.7 setup.py install && deactivate',chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#!/bin/bash' > launcher,echo cd {INSTALL_LOCATION} >> launcher,echo source {INSTALL_LOCATION}/venv/bin/activate \&\& python2.7 halfHandshake.py \"\$\@\" \&\& deactivate >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/halfHandshake"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
# cd {INSTALL_LOCATION}, sudo python2 halfHandshake.py
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
