#!/usr/bin/env python
#####################################
# Installation module for git-dumper
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="arthaud"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update git-dumper - Tool to dump a git repository from a website"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/arthaud/git-dumper"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="git-dumper"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# Requires an installed Python3.11 virtual environment (tested and confirmed working):
# ... see also: https://www.kali.org/docs/general-use/using-eol-python-versions/
# ... sudo apt-get install pyenv; pyenv install 3.11; pyenv global 3.11.11; exec /usr/bin/zsh; virtualenv venv --python=/home/kali/.pyenv/versions/3.11.11/bin/python3.11; pyenv global system
# After the above steps, run the commented AFTER_COMMANDS below.
AFTER_COMMANDS="cd {INSTALL_LOCATION},virtualenv venv --python=/home/kali/.pyenv/versions/3.11.11/bin/python3.11,/bin/bash -c 'source {INSTALL_LOCATION}/venv/bin/activate && pip3 install -r requirements.txt && deactivate',chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#\!/bin/bash' > launcher,echo 'cd' '{INSTALL_LOCATION}' >> launcher,echo source {INSTALL_LOCATION}/venv/bin/activate \&\& python3 git_dumper.py \\\"\\\$\\\@\\\" \&\& deactivate >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/git-dumper"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"