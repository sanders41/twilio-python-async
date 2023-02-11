from datetime import datetime, timezone
from typing import Union

from pydantic import BaseModel, Field, validator


class SubresouceUris(BaseModel):
    media: str


class Message(BaseModel):
    body: str
    num_segments: int
    direction: str
    from_: Union[str, None] = Field(None, alias="field")
    date_updated: datetime
    price: Union[float, None] = None
    error_message: Union[str, None] = None
    uri: str
    account_sid: str
    num_media: int
    to: str
    date_created: datetime
    status: str
    sid: str
    date_sent: Union[datetime, None] = None
    error_code: Union[int, None] = None
    price_unit: Union[str, None] = None
    api_version: str
    subresource_uris: SubresouceUris
    messaging_service_sid: Union[str, None] = None

    @validator("date_updated", pre=True)
    def parse_date_updated(cls, v: str) -> datetime:
        return _to_datetime(v)

    @validator("date_created", pre=True)
    def parse_date_created(cls, v: str) -> datetime:
        return _to_datetime(v)

    @validator("date_sent", pre=True)
    def parse_date_sent(cls, v: Union[str, None]) -> Union[datetime, None]:
        if not v:
            return None

        return _to_datetime(v)


def _to_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %z")
