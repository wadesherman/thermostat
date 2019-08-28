import os
import threading
from time import sleep
from dotenv import load_dotenv

from display import *
from thermostat import *
from store import Values
from sensor import *
from network import *

load_dotenv(override=True)

epic = True

if __name__ == "__main__":
    values = Values()

    network_interface = MqttAdapter(os.getenv("MQ_BROKER"), values)
    network_interface.start()
    network_interface.loop()

    http_interface = FlaskAdapter()
    http_interface.start()
    http_interface.loop()

    # Put the display on its own thread
    display = Display(TestDisplayAdapter())
    display_thread = threading.Thread(target=display.loop, daemon=True)
    display_thread.start()

    # Put the thermostat on its own thread
    thermostat = Thermostat(TestIOAdapter())
    thermostat_thread = threading.Thread(target=thermostat.loop, daemon=True)
    thermostat_thread.start()

    # register the Display and Thermostat with the Values store to receive
    # updates when values are updated.
    values.add_observer(display)
    values.add_observer(thermostat)
    values.add_observer(network_interface)

    # Polling the temp/humidity sensor can happen right here
    sensor = Sensor(TestSensorAdapter())
    # sensor = Sensor(Si7021Adapter())
    # sensor = Sensor(DHTAdapter("DHT22",23))

    values.write("current_temperature", sensor.get_temperature())
    values.write("set_temperature", 72)
    values.write("state", "off")
    values.write("hvac_state", "heat")

    while epic:
        values.write("current_temperature", sensor.get_temperature())
        values.write("current_humidity", sensor.get_humidity())
        sleep(15)
