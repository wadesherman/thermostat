import logging
from .Display import Display
from display.adapters.TestDisplayAdapter import TestDisplayAdapter

try:
    from display.adapters.InkyPhatAdapter import InkyPhatAdapter
except ImportError:
    logging.debug("no InkyPhat")
