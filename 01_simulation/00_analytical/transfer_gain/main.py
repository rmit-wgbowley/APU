"""
Filename: main.py

Description:
    A resonant Half Bridge Converter
    analytical model for transfer gain
    range over changing input voltage.
"""

from pathlib import Path
from picounits import Parser

from matplotlib import pyplot as plt

# Loads unit system, material library & parameters
ROOT_DIR = Path(__file__).resolve().parents[0]

# Materials & Parameter files
parameters_path = ROOT_DIR / "parameters.uiv"
parameters = Parser.open(parameters_path, ROOT_DIR / "../derived.ut")


initial = parameters.model.min_voltage
samples = (parameters.model.max_voltage - initial) / parameters.numerics.voltage_step

# Calculates the gain vs input voltage with fixed nominal voltage
input_voltage = []
transfer_gain = []

for index in range(0, int(samples)):
    voltage = initial + index * parameters.numerics.voltage_step
    gain = 2 * parameters.transformer.turns * (parameters.load.nominal_voltage/voltage)

    # Strips and appends voltage/gain results
    input_voltage.append(voltage.stripped)
    transfer_gain.append(gain.stripped)


plt.figure(figsize=(10, 6))
plt.plot(input_voltage, transfer_gain, linewidth=2, color='black')
plt.xlabel('Input voltage (V)', fontsize=12)
plt.ylabel('Transfer Gain (M)', fontsize=12)
plt.title(
    f'Transfer Gain vs Input Voltage, Nominal Output: {parameters.load.nominal_voltage:.3f}',
    fontsize=14
)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
