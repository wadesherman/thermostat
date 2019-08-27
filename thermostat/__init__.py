import logging

from .Thermostat import Thermostat
from thermostat.adapters.TestIOAdapter import TestIOAdapter

try:
    from thermostat.adapters.GpioAdapter import GpioAdapter
except ImportError:
    logging.debug("gpio not available")
