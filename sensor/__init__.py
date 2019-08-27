import logging
from .Sensor import Sensor
from sensor.adapters.TestSensorAdapter import TestSensorAdapter

try:
    from sensor.adapters.Si7021Adapter import Si7021Adapter
except ImportError:
    logging.debug("Si7021 module not available")

try:
    from sensor.adapters.DHTAdapter import DHTAdapter
except ImportError:
    logging.debug("DHT Module not available")
