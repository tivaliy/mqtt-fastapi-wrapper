import uuid

from fastapi import APIRouter, HTTPException

from app import schemas
from app.mqtt.client import fast_mqtt

from .topics import FAKE_TOPICS_LIST


router = APIRouter()


@router.post("/", response_model=schemas.TopicSubscription)
def subscribe_to_topic(subscription_in: schemas.TopicSubscriptionCreate):
    """
    Subscribes to a particular topic.
    """

    if subscription_in.topic not in FAKE_TOPICS_LIST:
        raise HTTPException(status_code=404, detail=f"Topic not found")

    fast_mqtt.client.subscribe(
        f"{subscription_in.topic}",
        qos=subscription_in.qos
    )

    # Potentially, here should be values from db, but let's fake it now
    topic_subscription = schemas.TopicSubscription(
        id_=str(uuid.uuid4()),
        **subscription_in.dict()
    )

    return topic_subscription
