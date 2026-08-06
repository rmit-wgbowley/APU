<!--
Colors:
FFFFFF - Pure white
e01e37 - Bold crimson-red 
-->
## Overview
![CERN-OHL-W License](https://img.shields.io/badge/License-CERN--OHL--W-FFFFFF?style=flat-square&logoColor=black)
![Power Electronics](https://img.shields.io/badge/Domain-Power_Electronics-e01e37?style=flat-square&logoColor=FFFFFF)
![Isolated DC/DC](https://img.shields.io/badge/Topology-Isolated_DC%2FDC-FFFFFF?style=flat-square&logoColor=e01e37)
![LLC Resonant Converter](https://img.shields.io/badge/Converter-LLC_Resonant-e01e37?style=flat-square&logoColor=e01e37)


<!--
> [!important]
> This repository was done for the `FSAE` elective `(AUTO1931)` at RMIT between 20 July and 13 Nov, 2026.

-->

> [!WARNING]
> **L0-L1 Phase**: This repository contains a work-in-progress design. 

A `FSAE` vehicle has two main power levels, the `HV` power bus from the tractive battery and the `LV` power bus from a packaged lithium battery. For `r27`, it is intended to 
decrease the capacity of the `LV` battery by using an isolated LLC resonant half-bridge DC/DC to step-down the `HV` bus to power the `LV` bus while the tractive battery is 
connected and as such the `LV` battery becomes a energy buffer instead of being the main source during operation. This potentially allows for reductions in LV battery mass, 
improved packaging and a power architecture similar to modern automotive EV systems.

### High level system topology

```
Traction battery (600 V)
         ↓
Isolated LLC resonant half-bridge DC/DC (~300 W target)
         ↓
LV battery buffer (12 V) (Energy Buffer) (Undecided Capacity)
         ↓
LV vehicle systems (12 V) (~200 W estimate)
```

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
