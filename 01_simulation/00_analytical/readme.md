### Overview

This folder contains analytical models to explore design variables at medium fidelity but extremely fast.

### First Harmonic Approximation (FHA)

This analytical model is written in `Python` and uses `picounits` for parameter loading and unit validation. It models the resonant circuit two-port model described in application note `AN2450` by ST,
and also in a `2024 RMIT` paper, though they use different models. The ST FHA model was used in this implementation.

<div align="center"><img src="../../05_media/01_simulation/00_analytical_models/fha_example.png" alt="FHA_Example" style="max-width: 600px">
<p><em>Figure 1: First Harmonic Approximation output showing transfer gain (linear) vs frequency (log).</em></p></div>

> Model: [first_harmonic_approximation](first_harmonic_approximation/)  
> Parameters: [parameters.uiv](first_harmonic_approximation/parameters.uiv)

---

### Transfer Gain vs Input Voltage

This analytical model is written in `Python` and uses `picounits` for parameter loading and unit validation. It models the 
transfer gain vs input voltage using the equations described in application note `AN2450` by ST.

<div align="center"><img src="../../05_media/01_simulation/00_analytical_models/transfer_vs_input_voltage.png" alt="Transfer gain vs input voltage" style="max-width: 600px">
<p><em>Figure 2: Analytical model showing transfer gain (linear) vs input voltage (linear).</em></p></div>

> Model: [transfer_gain](transfer_gain/)  
> Parameters: [parameters.uiv](transfer_gain/parameters.uiv)

---

### Winding Loading

This analytical model is written in `Python` and uses `picounits` for parameter loading and unit validation. It calculates primary and secondary
wire diameters across a range of current densities at a target power level, helping to inform winding design for the LLC converter.

> [!IMPORTANT]
>
> Wire diameters shown are bulk equivalents. Litz wire or multi-strand conductors are required in practice due to skin.

<div align="center"><img src="../../05_media/01_simulation/00_analytical_models/winding_loading.png" alt="Winding loading analysis" style="max-width: 600px">
<p><em>Figure 3: Primary and secondary wire diameter vs current density at a fixed target power.</em></p></div>

> Model: [winding_load](winding_load/)  
> Parameters: [parameters.uiv](winding_load/parameters.uiv)

---