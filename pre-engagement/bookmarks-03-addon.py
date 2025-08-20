#!/usr/bin/env python
#####################################
# Installation module for Bookmarks 03 ~ HackTricks
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="HackTricks-wiki"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Bookmarks 03 ~ HackTricks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
# NOTE: The download size of the repository is humongous, around 24GB, use carefully and only when needed locally
REPOSITORY_LOCATION="https://github.com/HackTricks-wiki/hacktricks"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="bookmarks-03"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,docker.io"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER
# NOTE:  PTF messes up the regular "git clone" command, so after emptying the folder, we redo the "git clone" command
# START: sudo docker run -d --rm --platform linux/amd64 -p 3337:3000 --name hacktricks -v $(pwd)/hacktricks:/app ghcr.io/hacktricks-wiki/hacktricks-cloud/translator-image bash -c "mkdir -p ~/.ssh && ssh-keyscan -H github.com >> ~/.ssh/known_hosts && cd /app && git config --global --add safe.directory /app && git checkout master && git pull && MDBOOK_PREPROCESSOR__HACKTRICKS__ENV=dev mdbook serve --hostname 0.0.0.0"
# NOTE:  In case the container does not start properly, drop the "-d" parameter and check the messages. Sometimes, a "git config pull.rebase true" is needed to update properly:
# START: sudo docker run --rm --platform linux/amd64 -p 3337:3000 --name hacktricks -v $(pwd)/hacktricks:/app ghcr.io/hacktricks-wiki/hacktricks-cloud/translator-image bash -c "mkdir -p ~/.ssh && ssh-keyscan -H github.com >> ~/.ssh/known_hosts && cd /app && git config --global --add safe.directory /app && git config pull.rebase true && git checkout $LANG && git pull && MDBOOK_PREPROCESSOR__HACKTRICKS__ENV=dev mdbook serve --hostname 0.0.0.0"
# STOP:  sudo docker stop hacktricks
AFTER_COMMANDS="cd {INSTALL_LOCATION},sudo rm -rf {INSTALL_LOCATION}/*,git clone https://github.com/HackTricks-wiki/hacktricks ,chown -R kali\:kali {INSTALL_LOCATION},chmod -R 0755 {INSTALL_LOCATION},echo '#!/bin/bash' > launcher,echo 'cd' '{INSTALL_LOCATION}' >> launcher,echo 'sudo docker run -d --rm --platform linux/amd64 -p 3337:3000 --name hacktricks -v {INSTALL_LOCATION}/hacktricks:/app ghcr.io/hacktricks-wiki/hacktricks-cloud/translator-image bash -c "mkdir -p ~/.ssh && ssh-keyscan -H github.com >> ~/.ssh/known_hosts && 'cd' '/app' && git config --global --add safe.directory /app && git checkout master && git pull && MDBOOK_PREPROCESSOR__HACKTRICKS__ENV=dev mdbook serve --hostname 0.0.0.0" && xdg-open http://localhost:3337' >> launcher,chmod +x {INSTALL_LOCATION}/launcher,sudo ln -sf {INSTALL_LOCATION}/launcher /usr/local/bin/hacktricks"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""