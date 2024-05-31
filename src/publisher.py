#publisher
import time
import paho.mqtt.client as mqtt_client
import random
import requests

from logger_wrapper import get_logger

logger = get_logger("publisher")

broker="broker.emqx.io"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info(f"Connected to broker {broker}")
    else:
        logger.error("Connection failed with code {rc}")

respone = requests.get("http://127.0.0.1:8000/user_id")
if respone.status_code != 200:
    logger.error(f"Error getting user_id. Response code = {respone.status_code}")
    exit()

user_id = respone.json()["user_id"]
logger.info(f"User ID {user_id} successfully received")

client = mqtt_client.Client(
   mqtt_client.CallbackAPIVersion.VERSION1,
   user_id
)

logger.info(f"Connecting to broker {broker}")
client.on_connect = on_connect
print(client.connect(broker))
client.loop_start()
logger.info("Publishing")

for i in range(10):
    state = "on" if random.randint(0, 1) == 0 else "off"
    state = state + "smmtoper"
    logger.debug(f"State is {state}")
    client.publish("lab/leds/state", state)
    time.sleep(2)

logger.info("Disconnecting")
client.disconnect()
client.loop_stop()