# PenTesters Framework (PTF) Add-ons
Add-on modules for the [PenTesters Framework (PTF)](https://github.com/trustedsec/ptf).

## Module Naming Convention
Add-on modules follow the naming convention:

**tool_name**-**addon**.py

This has been done so PTF will not overwrite any custom modules once they get added as a default module and during automatic updates of PTF.

## Alternative Module Configuration
For certain default PTF modules, the supplied installation and configuration instructions (the **AFTER_COMMANDS**) do not (yet) work properly. One example of this is **modules/vulnerability-analysis/owtf.py**. As a result, for this module an alternative module installation and configuration has been added to this repository.