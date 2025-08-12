#!/usr/bin/env python
##################################################
# Installation module for Security Headers Checker
##################################################

# AUTHOR OF MODULE NAME
AUTHOR="Koen Buyens"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update security headers checker"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/koenbuyens/securityheaders.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="securityheadersfull"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python3,python3-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="python3,python3-pip"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

#COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},virtualenv venv,/bin/bash -c 'source {INSTALL_LOCATION}/venv/bin/activate && pip3 install -r requirements.txt && pip3 install setuptools && deactivate',sed -i 's/loader.find_module(module_name).load_module(module_name)/loader.find_spec(module_name).loader.load_module(module_name)/' securityheaders/checkers/cors/__init__.py,sed -i 's/loader.find_module(module_name).load_module(module_name)/loader.find_spec(module_name).loader.load_module(module_name)/' securityheaders/checkers/__init__.py,sed -i 's/loader.find_module(module_name).load_module(module_name)/loader.find_spec(module_name).loader.load_module(module_name)/' securityheaders/checkers/checkerfactory.py,chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#!/bin/bash' > launcher,echo 'cd' '{INSTALL_LOCATION}' >> launcher,echo source {INSTALL_LOCATION}/venv/bin/activate \&\& python securityheaders.py \"\$\@\" \&\& deactivate >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/securityheadersfull"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
# cd {INSTALL_LOCATION},python3 securityheaders.py
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
