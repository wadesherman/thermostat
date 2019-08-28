from ..ProtocolInterface import ProtocolInterface
from store import ObserverInterface
import paho.mqtt.client as mqtt
import json


class MqttAdapter(ProtocolInterface, ObserverInterface):

    def __init__(self, broker, values):
        self.values = values
        self.broker = broker
        self.mqttc = mqtt.Client("Thermostat")  # should add uuid for uniqueness
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message

    def start(self):
        self.mqttc.connect(self.broker)

    def loop(self):
        self.mqttc.loop_start()

    def notify(self, m):
        self.mqttc.publish("foo/bar/baz", json.dumps(m))

    def on_message(self, client, userdata, message):
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

    def on_connect(self, client, userdata, flags, rc):
        self.mqttc.subscribe("foo/bar/baz")
        # self.mqttc.subscribe(os.getenv("STATE_TOPIC"))
        # self.mqttc.subscribe(os.getenv("HVAC_STATE_TOPIC"))
        # self.mqttc.subscribe(os.getenv("SET_TEMP_TOPIC"))
