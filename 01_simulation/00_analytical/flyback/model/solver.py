"""
Filename: solver.py

Description:
    Analytical Solver for lumped-parameter 
    model flyback converter
"""


from picounits import DynamicLoader, strip_quantity as validate
from picounits import voltage, capacitance, time, frequency, resistance, inductance, nullset



class ModelSolver:
    """
    Lumped-parameter solver for flyback converter problem.
    Computes voltage, current over time throughout the system
    """
    def __init__(self, parameters: DynamicLoader) -> None:
        """ Initializes the solver class """
        self._extract_validate(parameters)

    def _extract_validate(self, parameters: DynamicLoader) -> None:
        """ Extracts qualities from attribute tree and validates units """
        # Numerics
        self.time_step = validate(parameters.numerics.time_step, time)
        self.msg_frequency = validate(parameters.numerics.msg_frequency, frequency)

        # Input Source & Capacitor
        self.battery_voltage = validate(parameters.input.source.battery_voltage, voltage)
        self.input_capacitance = validate(parameters.input.capacitor.capacitance, capacitance)
        self.input_capacitor_resistance = validate(parameters.input.capacitor.resistance, resistance)

        # Switch & Transformer
        self.switch_resistance = validate(parameters.switch.switch_resistance, resistance)
        self.switching_frequency = validate(parameters.switch.switching_frequency, frequency)
        self.duty_cycle = validate(parameters.switch.duty_cycle, nullset)

        self.primary_inductance = validate(parameters.transformer.primary_inductance, inductance)
        self.secondary_inductance = validate(parameters.transformer.secondary_inductance, inductance)
        self.coupling_coefficient = validate(parameters.transformer.coupling_coefficient, nullset)

        # Load Diode, resistor & capacitor
        self.forward_voltage_drop = validate(parameters.load.diode.forward_voltage_drop, voltage)
        self.load_resistance = validate(parameters.load.resistor.resistance, resistance)
        self.load_capacitance = validate(parameters.load.capacitor.capacitance, capacitance)
        self.load_capacitor_resistance = validate(parameters.load.capacitor.resistance, resistance)
