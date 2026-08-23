<!--
Colors:
FFFFFF - Pure white
e01e37 - Bold crimson-red 
-->
## Overview
![Status](https://img.shields.io/badge/Status-L1-e01e37?style=flat-square)
![CERN-OHL-W License](https://img.shields.io/badge/License-CERN--OHL--W-FFFFFF?style=flat-square&logoColor=black)
![Power Electronics](https://img.shields.io/badge/Domain-Power_Electronics-e01e37?style=flat-square&logoColor=FFFFFF)
![Isolated DC/DC](https://img.shields.io/badge/Topology-Isolated_DC%2FDC-FFFFFF?style=flat-square&logoColor=e01e37)
![LLC Resonant Converter](https://img.shields.io/badge/Converter-LLC_Resonant-e01e37?style=flat-square&logoColor=e01e37)

<!--
> [!important]
> This repository was done for the `FSAE` elective `(AUTO1931)` at RMIT between 20 July and 13 Nov, 2026.
-->

A `600 V` to `12 V`, `300 W` isolated `LLC` converter for the FSAE low-voltage system. It is intended to be packaged with a `LV battery` for line 
buffering and standby mode while the tractive battery is disconnected.

This low voltage grounded auxiliary power unit `(LVG-APU)` enables drive-less features in future vehicle iterations, 
potentially reducing LV battery mass and improving packaging.

### High-level System Topology

```
Traction battery (600 V)
         ↓
LVG-APU Interface (Undecided Connector) 
-----------------------------------------------------------------
Isolated LLC resonant half-bridge DC/DC (~300 W target) (LLV-HS, LLV-LV)
         ↓
LV battery buffer (12 V) (Energy Buffer) (Undecided Capacity) ← Charger (External Supply) (12 V)
-----------------------------------------------------------------
LVG-APU Interface (Undecided Connector) 
         ↓
LV vehicle systems (12 V) (~200 W estimate)
```

> [!important] 
> The charger is included in the high-level topology as the LV battery is intended to be packaged inside the APU.

## Implementation

The design will be implemented as two independent boards, which are then mechanically and electrically 
connected via the `high-frequency transformer`. This reflects the natural system boundaries between the high and low voltage sides while also improving the ability to perform sub-circuit testing.

### High-level APU Topology

```
Interface (Undecided Connector) 
LLC-HV - Tractive battery input (400-600V domain) (Unknown EMI)
-----------------------------------------------------------------
EMI filter (Common-mode chokes) (Shunt Capacitors)
         ↓
Half Bridge Mosfets <- Half bridge Driver IC <- LLC Controller <- Optocoupler
         ↓
Resonant Tank Circuit
-----------------------------------------------------------------
High Frequency Transformer (Primary) (400-600 HF AC)

=============================================
Ferrite Core (Magnetic & Structural Coupling)
=============================================

LLC-LV - High Frequency transformer (Secondary) (12V AC) (Unknown Ripple)
-----------------------------------------------------------------
Synchronous Rectifier -> Status MCU (STM32) <- Optocoupler
         ↓
Integrated battery (12 V) (Undecided Capacity) <- Isolated Charger
-----------------------------------------------------------------
LV-Interface (Undecided Connector) (12V Domain) (Unknown EMI)
```

## Documentation
All internal documentation can be found within this repo's [issues](https://github.com/rmit-wgbowley/LV-Isolated-Buck/issues).

### Tags
```
LX -> Documentation and project structure
L0 -> Review and analysis of reference designs
L1 -> System level design, topology and interfaces
L2 -> Detailed design & prototyping
L3 -> Testing & Validation of prototype
DS -> De-scoped Feature, De-scoped Analysis
AC -> Architectural Change
```
