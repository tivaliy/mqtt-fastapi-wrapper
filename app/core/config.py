from functools import lru_cache
from typing import Dict, Type

from app.core.settings.test import TestAppSettings
from app.core.settings.base import BaseAppSettings, AppEnvTypes


environments: Dict[AppEnvTypes, Type[BaseAppSettings]] = {
    # TODO: Implement settings for Dev and Prod
    # AppEnvTypes.dev: DevAppSettings
    # AppEnvTypes.prod: ProdAppSettings
    AppEnvTypes.test: TestAppSettings
}


@lru_cache
def get_app_settings():
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
