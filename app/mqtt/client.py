import logging

from fastapi_mqtt.fastmqtt import FastMQTT

from .config import get_mqtt_config


logger = logging.getLogger(__name__)

fast_mqtt = FastMQTT(
    config=get_mqtt_config()
)


@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    logger.info(f"Connected: {client}, {flags}, {rc}, {properties}")


@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    logger.info(f"Received message: {topic}, {payload.decode()}, {qos}, {properties}")  # noqa


@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    logger.info(f"Disconnected: client - {client}")


@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    logger.info(f"Subscribed: {client}, {mid}, {qos}, {properties}")
