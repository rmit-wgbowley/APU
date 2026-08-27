"""
Filename: orchestrator.py

Description:
    Orchestrates FEMM to produce flux linkage
    curves with respect to current using
    a magnetostatic approach.
    
    *(Work in progress)*
"""


from pathlib import Path
import femm
import matplotlib.pyplot as plt

# --------------------------

# Primary Currents
primary_name = "Primary"
primary_range = [0, 0.500]
primary_steps = 10

# Secondary Currents
secondary_name = "Secondary"
secondary_range = [0, 25]
secondary_steps = 50

# --------------------------

# Loads the system path & file location
ROOT_DIR = Path(__file__).resolve().parents[0]
file_location = str(ROOT_DIR / '00_resources/transformer.FEM')

# Loads the FEMM model into pyfemm
femm.openfemm(0)
femm.opendocument(file_location)

# Primary excitation
primary_size = (primary_range[1] - primary_range[0]) / primary_steps

primary_flux_linkage = []
primary_current = []
for step in range(0, primary_steps + 1):
    current = primary_size * step
    print(f"Step {step}/{primary_steps}: Setting primary current to {current:.2f} A")

    femm.mi_setcurrent('Primary', current)
    femm.mi_setcurrent('Secondary', 0)

    femm.mi_analyze(1)
    femm.mi_loadsolution()

    flux_linkage = femm.mo_getcircuitproperties('Primary')[2]

    primary_flux_linkage.append(flux_linkage)
    primary_current.append(current)

# Secondary excitation
secondary_size = (secondary_range[1] - secondary_range[0]) / secondary_steps

secondary_flux_linkage = []
secondary_current = []
for step in range(0, secondary_steps + 1):
    current = secondary_size * step
    print(f"Step {step}/{secondary_steps}: Setting secondary current to {current:.2f} A")

    femm.mi_setcurrent('Primary', 0)
    femm.mi_setcurrent('Secondary', current)

    femm.mi_analyze(1)
    femm.mi_loadsolution()

    flux_linkage = femm.mo_getcircuitproperties('Secondary')[2]

    secondary_flux_linkage.append(flux_linkage)
    secondary_current.append(current)


# Clean up and close
femm.closefemm()

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
