from fastapi import APIRouter

from app.mqtt.client import fast_mqtt


router = APIRouter()


@router.get("/")
def read_topics():
    return {
        "message": "Welcome to MQTT topics list"
    }


@router.post("/{topic_name}")
def publish_to_topics(topic_name: str):

    fast_mqtt.publish(f"/{topic_name}", "Hello from Fastapi")

    return {
        "message": f"Success - published to {topic_name}"
    }
