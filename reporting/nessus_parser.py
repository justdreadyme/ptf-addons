#!/usr/bin/env python
#####################################
# Installation module for Nessus Parser
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Larry Spohn (Spoonman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Nessus Parser - a Nessus results parsing tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/interference-security/nessus_parser.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="nessus_parser"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="perl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="perl,perl-CPAN"

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cpan install XML::TreePP Data::Dumper Math::Round Excel::Writer::XLSX Data::Table Excel::Writer::XLSX::Chart Getopt::Std"

# create a launcher
LAUNCHER="nessus_parser"
