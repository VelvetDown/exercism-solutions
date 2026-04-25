"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?
    """

    if (temperature < 800 and 
        neutrons_emitted > 500 and 
        (temperature * neutrons_emitted) < 500_000):
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').
    """

    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif 60 <= efficiency < 80: 
        return 'orange'
    elif 30 <= efficiency < 60:
        return 'red'
    elif efficiency < 30:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    temp = temperature * neutrons_produced_per_second

    if temp < 0.9 * threshold:
        output = 'LOW'
    elif 0.9 * threshold <= temp <= 1.1 * threshold:
        output = 'NORMAL'
    else:
        output = 'DANGER'
    return output
    
    
