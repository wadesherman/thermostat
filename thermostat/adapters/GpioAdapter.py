from ..ThermostatAdapterInterface import ThermostatAdapterInterface

from gpiozero import OutputDevice


class GpioAdapter(ThermostatAdapterInterface):
    heat_relay = OutputDevice(1, initial_value=False)
    cool_relay = OutputDevice(2, initial_value=False)
    fan_relay = OutputDevice(3, initial_value=False)
