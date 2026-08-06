<!--
Colors:
FFFFFF - Pure white
e01e37 - Bold crimson-red 
-->
## Overview
![CERN-OHL-W License](https://img.shields.io/badge/License-CERN--OHL--W-FFFFFF?style=flat-square&logoColor=black)
![Electrics](https://img.shields.io/badge/Domain-Electrics-e01e37?style=flat-square&logoColor=black)
![Buck Converter](https://img.shields.io/badge/System-Buck_Converter-FFFFFF?style=flat-square)

<!--
> [!important]
> This repository was done for the `FSAE` elective `(AUTO1931)` at RMIT between 20 July and 13 Nov, 2026.

-->

> [!WARNING]
> **Design Phase**: This repository contains a work-in-progress design. 

A `FSAE` vehicle has two main power levels, the `HV` power bus from the tractive battery and the `LV` power bus from a packaged lithium battery. For `r27`, it is intended to decrease the size of the `LV` battery by using a buck converter to step-down the `HV` bus to power the `LV` bus while the tractive battery is connected and as such the `LV` battery becomes a current buffer instead of being the main source during operation.

## Documentation

All internal documentation can be found within this repo's [issues](https://github.com/rmit-wgbowley/LV-Isolated-Buck/issues).

### Tags
```
LX -> Documentation and project structure
L0 -> Review and analysis of reference designs
L1 -> System level design, topology and interfaces
L2 -> Detailed design, prototyping & testing
DS -> Descoped Feature, Descoped Analysis 
```
