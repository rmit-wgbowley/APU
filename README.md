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


<div align="center">
  <img 
    src="./05_media/00_logo/logo.png" 
    alt="APU Logo" 
    style="width:400px; max-width:100%; display:block;"
  >

  A proposed low-voltage grounded APU for FSAE-A vehicles <br>
  Engineered by [`William Bowley`](https://github.com/wgbowley)
</div>

### Overview

The APU is a proposed power architecture that allows the tractive battery, while connected, to feed the low-voltage grounded (LVG) system via an isolated LLC converter, using the LVG battery as a line buffer. 
The LVG battery also allows for standby mode while the tractive battery is disconnected.

```
Traction battery (600 V) → APU-LLC (12 V) → APU-Battery (12 V) → LVG Systems (12 V)
```

### Objectives

```
- [/] Support a `400-600 V` input range from the tractive battery.
- [/] Support up to `300 W (DC)` peak continuous loads on the APU and `800 W (DC)` peak transient loads.
- [ ] Reach an asymptote temperature under `70°C` with passive cooling.
- [ ] Validate the APU architecture and generate performance curves.
- [ ] Pass the EMC/EMI requirements and pass the 2027 Formula SAE rules inspection.
```

> *(Note). `[ ]` Not started. `[/]` In progress. `[x]` Complete.*

---

### Magnetic Passives

#### Primary Transformer

<div align="center">
  <table>
    <tr>
      <td><img src="./05_media/02_passives/00_primary_transformer/top_right_corner.png" alt="Transformer 1 Side" style="height:375px; width:auto;"></td>
      <td><img src="./05_media/02_passives/01_backup_transformer/cross_section.png" alt="Transformer 1 Cross Section" style="height:375px; width:auto;"></td>
    </tr>
  </table>
</div>

> *(Ordered). Primary Transformer core former and core are on-hand. Litz wire has been ordered.*

The primary transformer used for this design has an `N87` core with a `glass fibre` coil former and snap-on `ABS` insulation rings. 
The turns ratio is `21:1:1`, with `0.125 mm × 64` litz wire used on the primary across 3 layers of 14 turns each. 
The secondary and tertiary windings each have a single layer of 2 turns with `0.125 mm × 420` litz wire.

#### Backup Transformer

<div align="center">
  <table>
    <tr>
      <td><img src="./05_media/02_passives/01_backup_transformer/top_right_corner.png" alt="Transformer 2 Side" style="height:375px; width:auto;"></td>
      <td><img src="./05_media/02_passives/01_backup_transformer/cross_section.png" alt="Transformer 2 Cross Section" style="height:375px; width:auto;"></td>
    </tr>
  </table>
</div>

> *(Ordered). Backup Transformer core former, core, and litz wire have been ordered.*

This backup transformer is in case the primary transformer saturates during operation. 
This transformer uses a `40%` larger `N87` core with a matching `glass fibre` coil former. 
The same turns ratio of `21:1:1` and the same construction method are used.

#### Inductor

> *(Dependency). The resonant inductor is dependent on the implementation of the transformer.*

The inductor forms the series inductance $L_r$, which allows for frequency response tuning. 

See the [`02_passives`](./02_passives/readme.md) for implementation details.

---

### LLC-HVS & LLC-LVS Boards

> *(Dependency). The LLC-HVS and LLC-LVS are dependent on the implementation of the magnetic passives.*

#### Proposed Topology

```
LLC-HVS — Tractive Battery Input (400–600 V Domain) (Unknown EMI)
-----------------------------------------------------------------
EMI Filter (Common-mode chokes) (Shunt Capacitors)
         ↓
Half-Bridge MOSFETs ← Half-Bridge Driver IC ← LLC Controller → LLC-HVS Optocoupler
         ↓
Resonant Tank Circuit (Capacitor & Inductor)
-----------------------------------------------------------------
High-Frequency Transformer (Primary) (400-600 HF AC)

=============================================
Ferrite Core (Magnetic & Structural Coupling)
=============================================

LLC-LVS — High-Frequency Transformer (Secondary) (12 V AC)
-----------------------------------------------------------------
Synchronous Rectifier
        ↓
Status MCU (STM32) ← LLC-HVS Optocoupler 
-----------------------------------------------------------------
```

See the [`03_boards`](./03_boards/readme.md) for implementation details.

---

### APU Battery & External Charging Interface

> *(Dependency). The APU battery is dependent on the implementation of the LLC-HVS and LLC-LVS.*

#### Proposed Topology

```
APU-EBC (Isolated Supply) (Unknown Range) → APU-BI → APU-battery (12 V) (Undecided Capacity)
```

See the [`03_boards`](./03_boards/readme.md) for implementation details.

---

### APU Packaging & Integration

> *(Dependency). The APU packaging is dependent on all of the above.* <br>
> *(Note). This is a very early conceptual integration.*

#### Proposed Integration

The proposed integration is to package the LLC converter above the APU battery, with the converter ultimately sitting next to 
the APU-BI and APU-EBC boards, with a separation plane between the battery. That plane splits the APU into two sections: 
the `electronics box` with EMI shielding and the `battery box` with appropriate containment systems.

---

### Documentation

Each section of the repo is self-documenting. <br>
For internal documentation, credits, and contributors, refer to [`00_docs`](./00_docs/readme.md).

---


