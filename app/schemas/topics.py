from typing import Optional

from pydantic import BaseModel


class TopicBase(BaseModel):
    name: Optional[str] = None


class Topic(TopicBase):
    id_: Optional[str] = None
