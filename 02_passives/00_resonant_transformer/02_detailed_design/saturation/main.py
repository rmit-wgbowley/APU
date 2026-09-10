"""
Filename: main.py

Description:
    Calculates the derivative of db/di to get
    the linear region, saturation of a specific
    transformer core described in `data.uiv`
"""


from pathlib import Path
from picounits import Parser, resolve_derived

# Loads unit system & parameters
resolve_derived()

ROOT_DIR = Path(__file__).resolve().parents[0]
parameters = Parser.open(ROOT_DIR / "data.uiv")

current = parameters.data.current
flux_density = parameters.data.flux_density


for index in range(1, len(flux_density)):
    # Calculates the difference between frames
    db = flux_density[index] - flux_density[index - 1]
    di = current[index] - current[index - 1]

    # Calculates the numerical derivative
    db_di = db /di

    # prints the resulting values.
    print(f"dB = {db}, dI = {di}, dB/dI = {db_di}")
