from fastapi_mqtt.fastmqtt import FastMQTT

from .config import get_mqtt_config

fast_mqtt = FastMQTT(
    config=get_mqtt_config()
)


@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    print("Connected: ", client, flags, rc, properties)


@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ", topic, payload.decode(), qos, properties)


@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")


@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)
