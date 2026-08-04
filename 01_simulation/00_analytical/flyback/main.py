"""
Filename: main.py

Description:
    Analytical lumped-parameter model 
    for a flyback converter
"""

from pathlib import Path
from picounits.extensions.parser import Parser

from model.solver import ModelSolver

# Loads unit system & parameters
BASE_DIR = Path(__file__).parent
if not (BASE_DIR / "parameters.uiv").exists():
    raise FileNotFoundError("parameters.uiv not found in current directory")


parameters = Parser.open(BASE_DIR / "parameters.uiv", BASE_DIR / "metric.ut")
parameters.info("parameters")

# Loads model
solver = ModelSolver(parameters)
