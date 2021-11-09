from fastapi import FastAPI

from app.api.api import api_router
from app.mqtt.client import fast_mqtt


app = FastAPI(debug=True)

fast_mqtt.init_app(app)

app.include_router(api_router)
