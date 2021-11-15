from typing import Union

from ssl import SSLContext
from gmqtt.mqtt.constants import MQTTv50

from fastapi_mqtt.config import MQTTConfig


class TestMQTTSettings(MQTTConfig):

    # Service name in docker-compose
    host: str = "mosquitto"
    port: int = 1883
    ssl: Union[bool, SSLContext] = False
    keepalive:  int = 60
    username: str = None
    password: str = None
    version: int = MQTTv50

    reconnect_retries: int = None
    reconnect_delay: int = None

    will_message_topic = "/WILL"
    will_message_payload = "MQTT Connection is dead!"
    will_delay_interval = 2
