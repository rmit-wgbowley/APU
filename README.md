<!--
Colors:
FFFFFF - Pure white
e01e37 - Bold crimson-red 

Hello,
I think this is/was (for future tense) a very fun
project and I believe it's a good demonstration of my
engineering skills outside of me just making a linear
motor for example or some complex PCB at home. 

I enjoyed working with others for once, and being able
to have my own architecturally defined piece in the 
car is pretty damn cool.

- William Bowley, 2026-08-17

P.S: 
Thanks for downloading the APU repository `▽`ʃ♡ — but please be safe with high-voltage boards :)

-->

<p align="center">
  <img src="05_media/00_logo/logo.png" alt="APU Logo" style="width:400px; max-width:100%; display:block;">
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

<!-- > This repository was done for the `FSAE` elective `(AUTO1931)` at RMIT between 20 July and 13 Nov, 2026. -->

The APU is a proposed low-voltage grounded (LVG) system that allows the tractive battery, while connected, to feed the LVG system via an 
isolated LLC converter, effectively using the LVG battery as a line buffer. This has the secondary benefit of allowing standby mode while 
the tractive battery is disconnected.

#### High-level Topology

```
Traction battery (600 V) → APU-LLC Converter (12 V) → APU-Battery (12 V) → LVG Systems (12 V)
```

#### Objectives

```
- Support a 600 V to 400 V input range from the tractive battery.
- Support up to 300 W continuous loads on the APU and 800 W peaks.
- Reach an asymptote temperature under 70°C with passive cooling.
- Validate the APU architecture and generate performance curves.
- Pass the EMC/EMI requirements and pass the 2027 Formula SAE rules inspection.
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


