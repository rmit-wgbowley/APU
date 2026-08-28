"""
Filename: orchestrator.py

Description:
    Orchestrates FEMM to produce flux linkage
    curves with respect to current using a 
    magnetostatic approach for a transformer.
"""

from pathlib import Path
from picounits import Parser, CURRENT

from femm import femm as pyFEMM
from matplotlib import pyplot as plt


# Loads the system path & file location
ROOT_DIR = Path(__file__).resolve().parents[0]
file_location = str(ROOT_DIR / '00_resources/transformer.FEM')

# Loads the parameter file
parameters_path = ROOT_DIR / "parameters.uiv"
parameters = Parser.open(parameters_path)

# Loads the FEMM model into pyFEMM
pyFEMM.openfemm(0)
pyFEMM.opendocument(file_location)


# Primary excitation
primary_range = parameters.primary.current[1] - parameters.primary.current[0]
primary_size = primary_range.stripped / parameters.primary.steps.stripped

steps = parameters.primary.steps.stripped

primary_flux_linkage = []
primary_current = []
for step in range(0, steps + 1):
    current = primary_size * step
    print(f"Step {step}/{steps}: Setting primary current to {current * CURRENT:.2f}")

    pyFEMM.mi_setcurrent(parameters.primary.name, current)
    pyFEMM.mi_setcurrent(parameters.secondary.name, 0)

    pyFEMM.mi_analyze(1)
    pyFEMM.mi_loadsolution()

    flux_linkage = pyFEMM.mo_getcircuitproperties('Primary')[2]

    primary_flux_linkage.append(flux_linkage)
    primary_current.append(current)


# Secondary excitation
secondary_range = parameters.secondary.current[1] - parameters.secondary.current[0]
secondary_size = secondary_range.stripped / parameters.secondary.steps.stripped

steps = parameters.secondary.steps.stripped

secondary_flux_linkage = []
secondary_current = []
for step in range(0, steps + 1):
    current = secondary_size * step
    print(f"Step {step}/{steps}: Setting secondary current to {current * CURRENT:.2f} A")

    pyFEMM.mi_setcurrent(parameters.primary.name, 0)
    pyFEMM.mi_setcurrent(parameters.secondary.name, current)

    pyFEMM.mi_analyze(1)
    pyFEMM.mi_loadsolution()

    flux_linkage = pyFEMM.mo_getcircuitproperties('Secondary')[2]

    secondary_flux_linkage.append(flux_linkage)
    secondary_current.append(current)


# Clean up and close
pyFEMM.closefemm()
plt.figure(figsize=(12, 5))

# Primary plot
plt.subplot(1, 2, 1)
plt.plot(primary_current, primary_flux_linkage, color='black')
plt.xlabel('Primary Current (A)')
plt.ylabel('Flux Linkage (Wb-Turns)')
plt.title('Primary Excitation')
plt.grid(True)

# Secondary plot
plt.subplot(1, 2, 2)
plt.plot(secondary_current, secondary_flux_linkage, color='black')
plt.xlabel('Secondary Current (A)')
plt.ylabel('Flux Linkage (Wb-Turns)')
plt.title('Secondary Excitation')
plt.grid(True)

plt.tight_layout()
plt.show()
