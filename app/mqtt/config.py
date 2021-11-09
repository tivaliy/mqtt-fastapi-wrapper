from typing import Dict, Type

from .settings.test import TestMQTTSettings
from .settings.base import BaseMQTTSettings, MQTTEnvTypes


environments: Dict[MQTTEnvTypes, Type[BaseMQTTSettings]] = {
    # TODO: Implement settings for Dev and Prod
    # MQTTEnvTypes.dev: DevMQTTSettings
    # MQTTEnvTypes.prod: ProdMQTTSettings
    MQTTEnvTypes.test: TestMQTTSettings
}


def get_mqtt_config():
    mqtt_env = BaseMQTTSettings().mqtt_env
    config = environments[mqtt_env]
    return config()
