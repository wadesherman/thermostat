import paho.mqtt.client as mqtt
import os
import threading
from time import sleep
from dotenv import load_dotenv

load_dotenv(override=True)

epic = True

// registers to be shared across threads
register = {
  "current_temp": 0,
  "current_humidity: : 0,
  "state": 'off',
  "hvac_state": 'heat', // heat, fan, cool
  "set_temp": 0,
}

registerLock = Lock() 

// this should be in the Display "contract"
def display_loop():
  display = Display()
  // do some setup. 

  while epic:
    registerLock.aquire() 
    // update display
    registerLock.release()
    sleep(60) //

def on_message(client, userdata, message):
  // interpret state or set_temp message and update registers    
  // payload = str(message.payload.decode("utf-8"))
  // topic = str(message.topic.decode("utf-8"))
  if(settemp):
    lock
    update temp
    unlock
  
  if(state):
    Thermostat.run(payload)

def on_connect(client, userdata, flags, rc):
    mqttc.subscribe(os.getenv("STATE_TOPIC"))
    mqttc.subscribe(os.getenv("SET_TEMP_TOPIC"))

mqttc = mqtt.Client("Thermostat") //should add uuid for uniqueness
mqttc.on_connect=on_connect
mqttc.on_message=on_message
mqttc.connect(os.getenv("MQ_BROKER"))
mqttc.loop_start()


if __name__ == "__main__":

  // the display runs in its own thread
  display_thread = threading.Thread(targets=Display.loop)
  display_thread.start()
  
  // in do MQTT, sensor sampling in this thread
  while epic:
    
    registerLock.aquire()
    // sample temperature every 30 seconds.
    registerLock.release()
    sleep(30)
