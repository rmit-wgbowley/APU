<!--
Colors:
FFFFFF - Pure white
e01e37 - Bold crimson-red 
-->
## Overview
![CERN-OHL-W License](https://img.shields.io/badge/License-CERN--OHL--W-FFFFFF?style=flat-square&logoColor=black)
![Electrics](https://img.shields.io/badge/Domain-Electrics-e01e37?style=flat-square&logoColor=black)
![Buck Converter](https://img.shields.io/badge/System-Buck_Converter-FFFFFF?style=flat-square)

> [!important]
> This repository was done for the `FSAE` elective `(AUTO1931)` at RMIT between 20 July and 13 Nov, 2026.

A `FSAE` vehicle has two main power levels, the `HV` power bus from the tractive battery and the `LV` power bus from a packaged lithium battery. For `r27`, it is intended to decrease the size of the `LV` battery by using a buck converter to step-down the `HV` bus to power the `LV` bus while the tractive battery is connected and as such the `LV` battery becomes a current buffer instead of being the main source during operation.

### Repository Structure

```
├── README.md
├── LICENSE - CERN-OHL-W License
├───00_docs
│   └───00_references
├───01_electrical
│   ├───00_references
│   ├───01_datasheets
│   ├───02_detailed_design
│   └───03_kicad
├───02_mechanical
│   ├───00_references
│   ├───01_datasheets
│   └───02_cad
├───03_integration
└───04_media
    ├───01_electrical
    ├───02_mechanical
    └───03_integration
```

--- 

> [!WARNING]
> **Design Phase**: This repository contains a work-in-progress design. 

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

## License & Attribution

This project is a modified version of the [DCDC](https://github.com/Rootthecause/DCDC) project.

**Original Work**
- **Author**: Rootthecause / Liv
- **Original Repository**: [https://github.com/Rootthecause/DCDC](https://github.com/Rootthecause/DCDC)
- **Original License**: CERN Open Hardware license Version 2 - Weakly Reciprocal (CERN-OHL-W)

**Planned Modifications by RMIT MotorSports**
This project is currently in the design phase. We plan to:
- Convert the output from 24V to 12V to suit the r27 LV system requirements
- Conduct and document EMI testing to ensure compliance with relevant standards
- Implementation specifics relating to the r27 LV system 

The full text of the CERN-OHL-W license is included in this repository as `LICENSE`.
