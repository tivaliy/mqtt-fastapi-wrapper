from fastapi import APIRouter

from .endpoints import subscriptions, topics

api_router = APIRouter()
api_router.include_router(topics.router, prefix="/topics", tags=["topics"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])  # noqa
