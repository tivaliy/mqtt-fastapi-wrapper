import uuid
from typing import List

from fastapi import APIRouter, Body, HTTPException

from app import schemas
from app.mqtt.client import fast_mqtt


router = APIRouter()

# fake topic list
FAKE_TOPICS_LIST = ("/foo", "/bar")


@router.get("/", response_model=List[schemas.Topic])
def read_topics():
    """
    Get list of available topics.
    """
    # stub topic list response
    topic_list_response = [
        schemas.Topic(
            id_=str(uuid.uuid4()),
            name=name
        )
        for name in FAKE_TOPICS_LIST
    ]
    return topic_list_response


@router.post("/{topic_name}")
def publish_to_topics(
        topic_name: str,
        qos: int = 0,
        message: str = Body(..., embed=True)
):
    """
    Publish to a particular ``topic_name``.
    """

    if topic_name not in FAKE_TOPICS_LIST:
        raise HTTPException(status_code=404, detail=f"Topic not found")

    fast_mqtt.publish(f"{topic_name}", message, qos=qos)

    # 200 Ok with empty body
    return {}
