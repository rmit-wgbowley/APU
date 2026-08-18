"""
Filename: winding_load.py

Description:
    A transformer load analytical
    model for power output, current
    density and wire diameter.
    
    NOTE:
    This is just a quick analytical tool
    for understanding rather than specifically
    for implementation.
    
    NOTE:
    Bulk material in place of litz wire as 
    simplification
"""

from math import pi
from pathlib import Path
from picounits import Parser
from matplotlib import pyplot as plt

# Loads unit system, material library & parameters
ROOT_DIR = Path(__file__).resolve().parents[0]

# Materials & Parameter files
parameters_path = ROOT_DIR / "parameters.uiv"
parameters = Parser.open(parameters_path, ROOT_DIR / "../metric.ut")

# Target design point
target_power = parameters.design.target.power
target_current = target_power / parameters.load.nominal_voltage

current_density_axis = []
primary_wire_diameter_axis = []
secondary_wire_diameter_axis = []


# Calculate wire diameter across current density range at target power
current_density = parameters.transformer.range.min_current_density
while current_density <= parameters.transformer.range.max_current_density:
    # Calculates the wire diameter based on target current & current density
    inner_term = 4 * target_current / (pi * current_density)
    secondary_wire_diameter = inner_term ** 0.5
    primary_wire_diameter = secondary_wire_diameter / parameters.transformer.turns

    # Saves parameters as raw values (kA/m^2, mm, mm)
    current_density_axis.append(current_density.stripped * 10 ** -3)
    primary_wire_diameter_axis.append(primary_wire_diameter.stripped * 10 ** 3)
    secondary_wire_diameter_axis.append(secondary_wire_diameter.stripped * 10 ** 3)

    # Updates current density for next iteration
    current_density += parameters.numerics.current_density


# Plots the primary and secondary wire diameters against current density
fig, ax = plt.subplots()
ax.plot(current_density_axis, secondary_wire_diameter_axis,linewidth=2, color='black', label='Secondary')
ax.plot(current_density_axis, primary_wire_diameter_axis, linewidth=2, color='red', label='Primary')

ax.set_xlabel('Current Density k(A/m²)')
ax.set_ylabel('Wire Diameter (mm)')
ax.set_title(f'Wire Diameter vs Current Density at {target_power.stripped} (W)')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)
plt.show()
