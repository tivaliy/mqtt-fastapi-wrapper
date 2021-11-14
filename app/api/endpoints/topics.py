import uuid
from datetime import datetime

from fastapi import APIRouter, Body, HTTPException

from app.mqtt.client import fast_mqtt


router = APIRouter()

# fake topic list
topic_list = ['foo', 'bar']


@router.get("/")
def read_topics():
    # stub topic list response
    topic_list_response = [
        {
            "id": uuid.uuid4(),
            "name": name,
            "created_at": datetime.now()
        }
        for name in topic_list
    ]
    return topic_list_response


@router.post("/{topic_name}")
def publish_to_topics(
        topic_name: str,
        qos: int = 0,
        message: str = Body(..., embed=True)
):

    if topic_name not in topic_list:
        raise HTTPException(status_code=404, detail=f"Topic not found")

    fast_mqtt.publish(f"/{topic_name}", message, qos=qos)

    # 200 Ok with empty body
    return {}
