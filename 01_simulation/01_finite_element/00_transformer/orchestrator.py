"""
Filename: orchestrator.py

Description:
    Orchestrates FEMM to compute magnetic flux
    linkage with respect to current within the
    primary and secondary winding using a 
    magnetostatic approximation.
"""

from pathlib import Path
from femm import femm as pyFEMM
from picounits import Q, expects, strip_quantity

from picounits import CURRENT, MAGNETIC_FLUX


def connect_femm(path: Path) -> None:
    """ Connect FEMM for usage """
    pyFEMM.openfemm(0)
    pyFEMM.opendocument(str(path))


def disconnect_femm() -> None:
    """ Disconnect FEMM """
    pyFEMM.closefemm()


@expects(MAGNETIC_FLUX)
def compute_magnetic_flux(primary: Q, secondary: Q) -> tuple[Q, Q]:
    """ Computes the magnetic flux using FEMM """
    # Validates and strips dimensions
    primary = strip_quantity(primary, CURRENT)
    secondary = strip_quantity(secondary, CURRENT)

    # Updates primary and secondary windings
    pyFEMM.mi_setcurrent("Primary", primary)
    pyFEMM.mi_setcurrent("Secondary", secondary)

    # Analyzes and loads the solution
    pyFEMM.mi_analyse(1)
    pyFEMM.mi_loadsolution()

    # Calculates the flux_linkage of primary and secondary
    primary_linkage = pyFEMM.mo_getcircuitproperties('Primary')[2]
    secondary_linkage = pyFEMM.mo_getcircuitproperties('Secondary')[2]

    return primary_linkage * MAGNETIC_FLUX, secondary_linkage * MAGNETIC_FLUX
