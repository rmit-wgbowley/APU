"""
Filename: ref_approximate.py

Description:
    Calculations based on the 
    reference current draw table.
    
    NOTE:
    Calculates both continuous and peak
    power requirements from the reference
    current draw table.
"""

from __future__ import annotations
from dataclasses import dataclass

from picounits import Q, VOLTAGE, CURRENT, POWER, expects

# Parameters
NOMINAL_VOLTAGE = 12 * VOLTAGE
devices: list[Device] = []


@dataclass(slots=True, frozen=True)
class Device:
    """ Stores the values for a specific device """
    name: str
    continuous_current: Q
    peak_current: Q

    def __post_init__(self) -> None:
        """ Appends self to the device set """
        devices.append(self)

    @property
    @expects(POWER)
    def peak_power(self) -> Q:
        """ Calculates the peak usage """
        return self.peak_current * NOMINAL_VOLTAGE

    @property
    @expects(POWER)
    def continuous_power(self) -> Q:
        """ Calculates the continuous usage """
        return self.continuous_current * NOMINAL_VOLTAGE

    @property
    def _name(self):
        """ Returns name as attributes """
        return f"<{self.name}(P_continuous={self.continuous_power}, P_peak={self.peak_power})"

    def __repr__(self) -> str: return self._name
    def __str__(self) -> str: return self._name


# Devices within the low voltage system - Peak Current
Device("Power Distribution Module", 0.15 * CURRENT, 2 * CURRENT)
Device("Electronics Control Unit", 0.2 * CURRENT, 2 * CURRENT)
Device("High Voltage Battery Boards", 0.15 * CURRENT, 2 * CURRENT)
Device("Dash LEDS", 0.2 * CURRENT, 2 * CURRENT)
Device("Wheel - (Unknown)", 0.3 * CURRENT, 2 * CURRENT)
Device("Accumulator Management System", 0.3 * CURRENT, 2 * CURRENT)
Device("Shutdown Circuit", 0.6 * CURRENT, 10 * CURRENT)
Device("Brake light", 0.5 * CURRENT, 2 * CURRENT)
Device("Tractive System Active Light", 1.2 * CURRENT, 2 * CURRENT)

# Supporting systems
Device("Pump 1 - (Unknown)", 1.3 * CURRENT, 10 * CURRENT)
Device("Pump 2 - (Unknown)", 4.6 * CURRENT, 10 * CURRENT)
Device("Fan 1 - (Unknown)", 3.2 * CURRENT, 10 * CURRENT)
Device("Fan 2 - (Unknown)", 3.2 * CURRENT, 10 * CURRENT)


# Displays the results table
sum_peak_currents = 0 * CURRENT
sum_continuous_current = 0 * CURRENT
for item in devices:
    sum_peak_currents += item.peak_current
    sum_continuous_current += item.continuous_current
    print(item)
    print("-" * 80)

# Calculates the power usage
continuous_power = sum_continuous_current * NOMINAL_VOLTAGE
peak_power = sum_peak_currents * NOMINAL_VOLTAGE

print(f"Continuous Current: {sum_continuous_current:.3f}, Power: {continuous_power:.3f}")
print(f"Peak Current: {sum_peak_currents:.3f}, Power: {peak_power:.3f}")
print(f"1.5x Continuous Current: {continuous_power*1.5:.3f}")
