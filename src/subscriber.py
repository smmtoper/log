#subscriber
import time
#pip install paho-mqtt
import paho.mqtt.client as mqtt_client
import random
import requests

from logger_wrapper import get_logger

logger = get_logger("subscriber")

broker="broker.emqx.io"

def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.debug(f"received message = {data}")
    if len(data) == 0:
        logger.warning(f"received empty data")

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
client.on_message=on_message

logger.info(f"Connecting to broker {broker}")
client.connect(broker)
client.loop_start()
logger.info("Subcribing")
client.subscribe("lab/leds/state")
time.sleep(1800)
logger.info("Disconnecting")
client.disconnect()
client.loop_stop()