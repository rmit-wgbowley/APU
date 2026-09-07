"""
Filename: orchestrator.py

Description:
    Orchestrates FEMM to produce flux curves
    with respect to current using a magnetostatic 
    approach for a transformer.
    
    It also uses the core area to derive the
    b-field within the core.
"""

from pathlib import Path
from picounits import Parser, MAGNETIC_FLUX, AREA

from femm import femm as pyFEMM
from matplotlib import pyplot as plt


# Loads the system path & file location
ROOT_DIR = Path(__file__).resolve().parents[0]
file_location = str(ROOT_DIR / '00_resources/transformer.FEM')

# Loads the parameter file
parameters = Parser.open(ROOT_DIR / "parameters.uiv")

# Loads the FEMM model into pyFEMM
pyFEMM.openfemm(0)
pyFEMM.opendocument(file_location)

# Transformer core area
# (Work In Progress)


# Primary excitation
primary_range = parameters.primary.current[1] - parameters.primary.current[0]
primary_size = primary_range / parameters.primary.steps

steps = parameters.primary.steps.stripped

primary_flux = []
primary_current = []
for step in range(0, steps + 1):
    current = primary_size * step
    print(f"Step {step}/{steps}: Primary current = {current:.2f}")

    pyFEMM.mi_setcurrent(parameters.primary.name, current.stripped)
    pyFEMM.mi_setcurrent(parameters.secondary.name, 0)

    pyFEMM.mi_analyze(1)
    pyFEMM.mi_loadsolution()

    flux_linkage = pyFEMM.mo_getcircuitproperties('Primary')[2]
    flux = flux_linkage / parameters.primary.turns * MAGNETIC_FLUX

    primary_flux.append(flux)
    primary_current.append(current)


# Secondary excitation
secondary_range = parameters.secondary.current[1] - parameters.secondary.current[0]
secondary_size = secondary_range / parameters.secondary.steps

steps = parameters.secondary.steps.stripped

secondary_flux = []
secondary_current = []
for step in range(0, steps + 1):
    current = secondary_size * step
    print(f"Step {step}/{steps}: Secondary current = {current:.2f}")

    pyFEMM.mi_setcurrent(parameters.primary.name, 0)
    pyFEMM.mi_setcurrent(parameters.secondary.name, current.stripped)

    pyFEMM.mi_analyze(1)
    pyFEMM.mi_loadsolution()

    flux_linkage = pyFEMM.mo_getcircuitproperties('Secondary')[2]
    flux = flux_linkage / parameters.secondary.turns * MAGNETIC_FLUX

    secondary_flux.append(flux)
    secondary_current.append(current)


# Clean up and close
pyFEMM.closefemm()

core_area = 1
# Calculates the b-field from the solution
primary_b_field = [flux / core_area for flux in primary_flux]
secondary_b_field = [flux / core_area for flux in secondary_flux]

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
