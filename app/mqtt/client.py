from fastapi_mqtt.fastmqtt import FastMQTT
from loguru import logger

from app.core.config import get_app_settings

settings = get_app_settings()

# Let's pass the whole settings attributes
fast_mqtt = FastMQTT(config=settings)


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
