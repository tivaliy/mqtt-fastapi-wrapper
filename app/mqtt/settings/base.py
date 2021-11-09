from enum import Enum

from pydantic import BaseSettings


class MQTTEnvTypes(Enum):
    prod: str = 'prod'
    dev: str = 'dev'
    test: str = 'test'


class BaseMQTTSettings(BaseSettings):
    mqtt_env: MQTTEnvTypes = MQTTEnvTypes.test

    class Config:
        env_file = '.env'
        case_sensitive = True
        env_file_encoding = 'utf-8'
