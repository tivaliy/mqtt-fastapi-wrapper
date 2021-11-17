from fastapi import APIRouter

from app.api.api_v1.endpoints import subscriptions, topics

api_router = APIRouter()
api_router.include_router(topics.router, prefix="/topics", tags=["topics"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])  # noqa
