#!/usr/bin/env python
#####################################
# Installation module for MSBuildShell
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Cn33liz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update MSBuildShell - Powershell Host running within MSBuild.exe"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Cn33liz/MSBuildShell"

# X64 LOCATION
X64_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="msbuildshell"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
# To compile on Windows (32bit): C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild.exe C:\Scripts\MSBuildShell.csproj
# To compile on Windows (64bit): C:\Windows\Microsoft.NET\Framework64\v4.0.30319\msbuild.exe C:\Scripts\MSBuildShell.csproj
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"