import logging

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """
    Test Application settings class.
    """

    debug: bool = True

    logging_level: int = logging.DEBUG

    # Service name in docker-compose
    host: str = "mosquitto"

    will_message_topic = "/WILL"
    will_message_payload = "MQTT Connection is dead!"
    will_delay_interval = 2
