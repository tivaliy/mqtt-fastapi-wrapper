from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import get_app_settings
from app.mqtt.client import fast_mqtt


def create_application() -> FastAPI:
    """
    Creates and initializes FastAPI application.
    """

    settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.include_router(api_router, prefix=settings.api_v1_prefix)

    # Init mqtt client
    fast_mqtt.init_app(application)

    return application


app = create_application()
