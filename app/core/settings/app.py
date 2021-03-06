import logging
import sys
from typing import Any, Dict, List, Tuple

from fastapi_mqtt.config import MQTTConfig
from loguru import logger

from app.core.logging import InterceptHandler
from app.core.settings.base import BaseAppSettings


# TODO: Re-think in favor of using nested env for MQTTConfig, see link
#  https://github.com/samuelcolvin/pydantic/pull/3159
class AppSettings(BaseAppSettings, MQTTConfig):
    """
    Base Application settings class.
    """

    debug: bool = False
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    api_v1_prefix: str = "/api/v1"
    openapi_prefix: str = ""
    openapi_url: str = f"{api_v1_prefix}/openapi.json"
    title: str = "FastAPI+MQTT example application"
    app_version: str = "0.0.1"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    # ====================== MQTT client settings =========================
    # Use default/base settings for MQTT client defined in MQTTConfig class
    # host: str = "localhost"
    # port: int = 1883

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """
        FastAPI related arguments.
        """
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.app_version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]  # noqa

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])  # noqa
