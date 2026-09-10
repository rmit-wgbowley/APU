"""
Filename: main.py

Description:
    Computes the magnetic flux with respect to
    currents within the primary and secondary
    windings using magnetostatic FEMM.
    
    Uses those flux curves to compute the b-field
    with respect to those primary and secondary
    currents also.
"""

from math import pi
from pathlib import Path
from matplotlib import pyplot as plt

from picounits import Parser, Q, DynamicLoader, resolve_derived, expects
from picounits import LENGTH, CURRENT

from orchestrator import connect_femm, disconnect_femm, compute_magnetic_flux


# Loads unit system & parameters
resolve_derived()

ROOT_DIR = Path(__file__).resolve().parents[0]
parameters = Parser.open(ROOT_DIR / "parameters.uiv")


@expects(LENGTH ** 2)
def core_area(parameter: DynamicLoader) -> Q:
    """ Calculates the cross sectional area of the core. """
    core_center = pi * (parameter.core.inner_dia / 2) ** 2
    return core_center


# Loads the FEMM model and loads Numerical Steps
file_location = str(ROOT_DIR / '00_resources/transformer.FEM')
connect_femm(file_location)

steps = parameters.numerics.steps.stripped

# Primary & secondary excitation range
primary_range = (parameters.primary.current[1] - parameters.primary.current[0]) / steps
secondary_range = (parameters.secondary.current[1] - parameters.secondary.current[0]) / steps

# Primary excitation
primary_flux = []
primary_current = []

for step in range(0, steps + 1):
    current = primary_range * step
    print(f"Step {step}/{steps}: Primary Current = {current:.2f}")

    # Computes the magnetic flux linkage
    linkage, _ = compute_magnetic_flux(current, 0 * CURRENT)
    flux = linkage / parameters.primary.turns

    # Appends the results
    primary_flux.append(flux)
    primary_current.append(current)


# Secondary excitation
secondary_flux = []
secondary_current = []

for step in range(0, steps + 1):
    current = secondary_range * step
    print(f"Step {step}/{steps}: Secondary Current = {current}")

    # Computes the magnetic flux linkage
    _, linkage = compute_magnetic_flux(0 * CURRENT, current)
    flux = linkage / parameters.primary.turns

    # Appends the results
    secondary_flux.append(flux)
    secondary_current.append(current)


# Disconnect FEMM
disconnect_femm()

# Calculates the b-field from the solution
area = core_area(parameters)
primary_b_field = [flux / area for flux in primary_flux]
secondary_b_field = [flux / area for flux in secondary_flux]

# Calculates the inductance of the secondary and primary
primary_inductance = []
secondary_inductance = []

for i in range(1, len(primary_current)):
    linkage = primary_flux[i] * parameters.primary.turns
    primary_inductance.append(linkage / primary_current[i])

for i in range(1, len(secondary_current)):
    linkage = secondary_flux[i] * parameters.primary.turns
    secondary_inductance.append(linkage / secondary_current[i])

# Calculates the average inductance from secant inductance
primary_avg_inductance = primary_inductance[0]
for inductance in primary_inductance[1:]:
    primary_avg_inductance = primary_avg_inductance + inductance
    
primary_avg_inductance = primary_avg_inductance / len(primary_inductance)

secondary_avg_inductance = secondary_inductance[0]
for inductance in secondary_inductance[1:]:
    secondary_avg_inductance = secondary_avg_inductance + inductance

secondary_avg_inductance = secondary_avg_inductance / len(secondary_inductance)

print("\n===== Secant Inductance Results =====")
print(f"Primary   average inductance: {primary_avg_inductance}")
print(f"Secondary average inductance: {secondary_avg_inductance}")

# Create figure with 2x2 subplots
plt.figure(figsize=(12, 10))

# Primary Flux Linkage plot
plt.subplot(2, 2, 1)
plt.plot(primary_current, primary_flux, color='black')
plt.xlabel('Primary Current (A)')
plt.ylabel('Flux (Wb)')
plt.title('Primary Excitation - Flux')
plt.grid(True)

# Secondary Flux Linkage plot
plt.subplot(2, 2, 2)
plt.plot(secondary_current, secondary_flux, color='black')
plt.xlabel('Secondary Current (A)')
plt.ylabel('Flux (Wb)')
plt.title('Secondary Excitation - Flux')
plt.grid(True)

# Primary B-field plot
plt.subplot(2, 2, 3)
plt.plot(primary_current, primary_b_field, color='red')
plt.xlabel('Primary Current (A)')
plt.ylabel('B-field (T)')
plt.title('Primary Excitation - B-field')
plt.grid(True)

# Secondary B-field plot
plt.subplot(2, 2, 4)
plt.plot(secondary_current, secondary_b_field, color='red')
plt.xlabel('Secondary Current (A)')
plt.ylabel('B-field (T)')
plt.title('Secondary Excitation - B-field')
plt.grid(True)

plt.tight_layout()
plt.show()
