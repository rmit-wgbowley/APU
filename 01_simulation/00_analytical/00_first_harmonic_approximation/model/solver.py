"""
Filename: solver.py

Description:
    A Resonant Half Bridge Converter analytical
    solver for quality factor and transfer gain
    against normalized frequency
"""

from math import pi

from picounits import DynamicLoader, Q, strip_quantity as validate
from picounits import VOLTAGE, CAPACITANCE, FREQUENCY, INDUCTANCE, NULLSET, CURRENT, IMPEDANCE


class ModelSolver:
    """
    Analytical Solver for resonant half bridge converter problem.
    Computes quality factor, transfer gain over normalized frequency.
    """
    def __init__(self, parameters: DynamicLoader) -> None:
        """ Initializes the solver class """
        self._extract_validate(parameters)

        # Derived parameters
        self.ind_ratio = self.series_r_inductance / self.magnetising_inductance
        self.res_freq = 1 / (2 * pi * (self.series_r_inductance * self.series_r_capacitance) ** 0.5)
        self.char_imp = (self.series_r_inductance / self.series_r_capacitance) ** 0.5

        # Calculates the quality factor
        term = 8 * self.turns ** 2 * self.load_nominal_voltage
        denom = pi ** 2 * self.load_max_current

        self.equivalent_load_resistance = term / denom
        self.quality_factor = self.char_imp / self.equivalent_load_resistance

    def gain_characteristic(self, normalized_frequency: Q) -> Q:
        """ Computes the transfer gain characteristic at a normalized frequency """
        normalized_frequency = validate(normalized_frequency, NULLSET)

        if normalized_frequency == 0: 
            # Returns to avoid division by zero
            return 0.0 * NULLSET

        term1 = (1 + self.ind_ratio - self.ind_ratio / normalized_frequency **2 ) ** 2
        term2 = self.quality_factor ** 2 * (normalized_frequency - 1 / normalized_frequency) ** 2

        result = 1 / (term1 + term2) ** 0.5 * NULLSET
        return result * NULLSET

    def gain_range(self) -> tuple[Q, Q]:
        """ Calculates the required gain range based off max and min voltages """
        m_min = 2 * self.turns * self.load_nominal_voltage / self.max_voltage
        m_max = 2 * self.turns * self.load_nominal_voltage / self.min_voltage

        return (m_min, m_max) * NULLSET

    def _extract_validate(self, parameters: DynamicLoader) -> None:
        """ Extracts qualities from attribute tree and validates units """
        # Model
        self.max_voltage = validate(parameters.model.max_voltage, VOLTAGE)
        self.min_voltage = validate(parameters.model.min_voltage, VOLTAGE)

        # Load
        self.load_max_current = validate(parameters.load.max_current, CURRENT)
        self.load_nominal_voltage = validate(parameters.load.nominal_voltage, VOLTAGE)

        # Transformer
        self.turns = validate(parameters.transformer.turns, NULLSET)
        self.magnetising_inductance = validate(parameters.transformer.magnetising, INDUCTANCE)
        self.series_r_inductance = validate(parameters.transformer.series_resonant, INDUCTANCE)

        # Capacitor
        self.series_r_capacitance = validate(parameters.capacitor.series_resonant, CAPACITANCE)

    @property
    def _name(self) -> str:
        """ Returns name as attributes """
        return (
            f"<LLC(Resonance: {self.res_freq * FREQUENCY}, "
            f"Impedance: {self.char_imp * IMPEDANCE}, "
            f"Quality Factor: {self.quality_factor * NULLSET}, "
            f"Inductance Ratio: {self.ind_ratio * NULLSET})>"
        )

    def info(self) -> None:
        """ Prints the system information to terminal """
        print(self._name)

    def __repr__(self) -> str: return self._name
    def __str__(self) -> str: return self._name
