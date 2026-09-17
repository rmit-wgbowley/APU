"""
Filename: wire_cross_section.py

Description:
    Calculates the wire cross section for different 
    RMS currents up to a specific current.
"""

from math import pi, sqrt

from picounits import resolve_derived
from picounits import CURRENT, LENGTH

# Loads the unit system
resolve_derived()

# System Constants
current_density = 4 * (CURRENT / LENGTH ** 2)

# System Parameters
current_step = 1 * CURRENT
current_range = [0, 30] * CURRENT

steps = (current_range[1] - current_range[0]) / current_step

# Computes the cross section over a range of currents
for index in range(1, int(steps) + 1):
    current = current_range[0] + index * current_step

    # Computes the cross section at a specific current
    area = current / current_density
    diameter = sqrt(4 * area / pi)

    print(f"Section: {area:.3f} | Diam: {diameter:.3f} @ {current:.3f}")
