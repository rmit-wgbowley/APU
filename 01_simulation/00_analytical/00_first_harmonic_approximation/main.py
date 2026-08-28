"""
Filename: main.py

Description:
    A Resonant Half Bridge Converter analytical 
    first harmonic approximation for quality factor
    and transfer gain against normalized frequency
"""

from pathlib import Path
from picounits import Parser
from picounits import FREQUENCY

from matplotlib import pyplot as plt
from model.solver import ModelSolver

# Loads unit system, material library & parameters
ROOT_DIR = Path(__file__).resolve().parents[0]

# Materials & Parameter files
parameters_path = ROOT_DIR / "parameters.uiv"
parameters = Parser.open(parameters_path, ROOT_DIR / "../derived.ut")

# Loads in the Solver and prints derived values
solver = ModelSolver(parameters)
solver.info()


# Calculates the number of samples
frequency_step = parameters.numerics.frequency_step
frequency_sample_space = parameters.numerics.frequency_sample

num_samples = int(frequency_sample_space/frequency_step)
print(f"Sample Space: {frequency_sample_space}, Samples: {num_samples}")


# Calculates the gain characteristic vs normalized frequency
normalized_results = []
gain_results = []

for index in range(0, num_samples):
    normalized_frequency = (frequency_step * index) / (solver.res_freq * FREQUENCY)
    gain = solver.gain_characteristic(normalized_frequency)

    # Appends the resulting normalized frequency and gain, removed units
    normalized_results.append(normalized_frequency.stripped)
    gain_results.append(gain)


# Plots the normalized frequency vs characteristic gain
plt.figure(figsize=(10, 6))
plt.semilogx(normalized_results, gain_results, linewidth=2, color='black')
plt.xlabel('Normalized Frequency (f/f₀)', fontsize=12)
plt.ylabel('Transfer Gain (M)', fontsize=12)
plt.title(
    f'Transfer Gain at L_r = {solver.ind_ratio:.3f} (Lr/Lm), Qe = {solver.quality_factor:.3f}',
    fontsize=14
)
plt.grid(True, alpha=0.3)

# Add gain range as lines
gain_min, gain_max = solver.gain_range()
plt.axhline(y=gain_min, color='blue', linestyle='--', label=f'Gain min = {gain_min:.3f}')
plt.axhline(y=gain_max, color='blue', linestyle='--', label=f'Gain max = {gain_max:.3f}')

# Add frequency lines
peak_idx = gain_results.index(max(gain_results))

f_at_gain_min = None
f_at_gain_max = None


for i in range(peak_idx, len(gain_results)):
    gain = gain_results[i]

    if f_at_gain_max is None and gain <= gain_max:
        # Adds the closes point before max gain
        f_at_gain_max = normalized_results[i]

    if f_at_gain_min is None and gain <= gain_min:
        # Adds the close point before min gain
        f_at_gain_min = normalized_results[i]

    if f_at_gain_min and f_at_gain_max:
        # Breaks the loop if both are true
        break


plt.axvline(f_at_gain_min, color='red', linestyle=':', label=f'Fn, max = ~{f_at_gain_min:.3f}')
plt.axvline(f_at_gain_max, color='red', linestyle=':', label=f'Fn, min = ~{f_at_gain_max:.3f}')

plt.legend()
plt.show()
