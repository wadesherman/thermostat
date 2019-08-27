import paho.mqtt.client as mqtt
import os
import threading
from time import sleep
from dotenv import load_dotenv

from display import *
from thermostat import *
from store import Values
from sensor import *

load_dotenv(override=True)

epic = True

# registers to be shared across threads
values = Values()
values.initialize("current_temperature")
values.initialize("current_humidity")
values.initialize("state", "off")
values.initialize("hvac_state", "heat")
values.initialize("set_temp")


def on_message(client, userdata, message):
    # interpret state or set_temp message and update registers
    payload = str(message.payload.decode("utf-8"))
    topic = str(message.topic.decode("utf-8"))
    print(topic + ": " + payload)
    # if(settemp):
    #   lock
    #   update temp
    #   unlock
    #
    # if(state):
    #   Thermostat.run(payload)


def on_connect(client, userdata, flags, rc):
    mqttc.subscribe(os.getenv("STATE_TOPIC"))
    mqttc.subscribe(os.getenv("HVAC_STATE_TOPIC"))
    mqttc.subscribe(os.getenv("SET_TEMP_TOPIC"))


if __name__ == "__main__":

    # MQTT takes care of its own non-blocking thread
    mqttc = mqtt.Client("Thermostat")  # should add uuid for uniqueness
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect(os.getenv("MQ_BROKER"))
    mqttc.loop_start()

    # Put the display on its own thread
    display = Display(TestDisplayAdapter())
    display_thread = threading.Thread(target=display.loop)
    display_thread.start()

    # Put the thermostat on its own thread
    thermostat = Thermostat(TestIOAdapter())
    thermostat_thread = threading.Thread(target=thermostat.loop)
    thermostat_thread.start()

    # register the Display and Thermostat with the Values store to receive
    # updates when values are updated.
    values.add_observer(display)
    values.add_observer(thermostat)

    # Polling the temp/humidity sensor can happen right here
    sensor = Sensor(TestSensorAdapter())
    # sensor = Sensor(Si7021Adapter())
    # sensor = Sensor(DHTAdapter("DHT22",23))
    while epic:
        values.write("current_temperature", sensor.get_temperature())
        values.write("current_humidity", sensor.get_humidity())
        sleep(5)
