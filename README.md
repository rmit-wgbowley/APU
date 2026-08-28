<!--
Colors:
FFFFFF - Pure white
e01e37 - Bold crimson-red 
-->

<p align="center">
  <em> (An appropriate header logo/image is under development) </em>
  <!-- <img src="" alt="" style="width:100%; max-width:100%; display:block;"> -->
  <br>
  <br>
  <em>
    A proposed low-voltage grounded APU for FSAE-A vehicles 
    <br>
    Engineered by 
    <a href="https://github.com/wgbowley">William Bowley</a>
  </em>
</p>

### Overview

![Status](https://img.shields.io/badge/Status-L1-e01e37?style=flat-square)
![CERN-OHL-W License](https://img.shields.io/badge/License-CERN--OHL--W-FFFFFF?style=flat-square&logoColor=black)
![Power Electronics](https://img.shields.io/badge/Domain-Power_Electronics-e01e37?style=flat-square&logoColor=FFFFFF)
![LLC Resonant](https://img.shields.io/badge/Topology-LLC_Resonant%2FDC-FFFFFF?style=flat-square&logoColor=e01e37)


> [!important]
> This repository was done for the `FSAE` elective `(AUTO1931)` at RMIT between 20 July and 13 Nov, 2026.

A proposed architecture to feed the low-voltage grounded `(LVG)` system using the tractive battery's `400–600 V` domain via an LLC 
converter to step down the voltage to `12 V`, which feeds an LVG battery. The proposed implementation would be a `12 V`, `25 A` 
isolated `LLC` converter with the LVG battery allowing for standby mode, absorbing line noise from the converter, and handling high load transients.

This low-voltage grounded auxiliary power unit `(LVG-APU)` enables drive-less features in future vehicle iterations while potentially 
reducing LVG battery mass and improving packaging. The component-level packaging also allows for long-term usage and reduces validation
per iteration via the ability to black-box the solution.

#### High-level System Topology

```
Traction battery (600 V)
         ↓
LVG-APU Interface (Undecided Connector) (Unknown EMI / Ripple)
-----------------------------------------------------------------
Isolated LLC resonant half-bridge DC/DC (~300 W target) (LLV-HS, LLV-LV)
         ↓
LV battery buffer (12 V) (Energy Buffer) (Undecided Capacity) ← Charger (Isolated Supply) (Unknown Range)
-----------------------------------------------------------------
LVG-APU Interface (Undecided Connector) (Unknown EMI / Ripple)
         ↓
LV vehicle systems (12 V) (~200 W estimate)
```

---

### Implementation

The design will be implemented as two independent boards, which are then mechanically and electrically connected via the transformer. 
This reflects the natural system boundaries between the high and low voltage sides while also improving the ability to perform sub-circuit testing.

#### APU Topology

```
Interface (Undecided Connector) 
LLC-HVS - Tractive battery input (400-600V domain) (Unknown EMI)
-----------------------------------------------------------------
EMI filter (Common-mode chokes) (Shunt Capacitors)
         ↓
Half Bridge Mosfets <- Half bridge Driver IC <- LLC Controller <- Optocoupler
         ↓
Resonant Tank Circuit (Capacitor & External Inductor)
-----------------------------------------------------------------
High Frequency Transformer (Primary) (400-600 HF AC)

=============================================
Ferrite Core (Magnetic & Structural Coupling)
=============================================

LLC-LVS - High Frequency transformer (Secondary) (12V AC) (Unknown Ripple)
-----------------------------------------------------------------
Synchronous Rectifier -> Status MCU (STM32) <- Optocoupler
         ↓
Integrated battery (12 V) (Undecided Capacity) <- Isolated Charger
-----------------------------------------------------------------
LV-Interface (Undecided Connector) (12V Domain) (Unknown EMI)
```

---

### Documentation
All internal documentation can be found within this repo's [issues](https://github.com/rmit-wgbowley/LV-Isolated-Buck/issues).

#### Tags
```
Project Progress:
----------------------------------------------------
LX -> Documentation and project structure
L0 -> Review and analysis of reference designs
L1 -> System level design, topology and interfaces
L2 -> Detailed design & prototyping
L3 -> Testing & Validation of prototype
----------------------------------------------------

Miscellaneous:
----------------------------------------------------
DS -> De-scoped Feature, De-scoped Analysis
AC -> Architectural Change
----------------------------------------------------
```

---


