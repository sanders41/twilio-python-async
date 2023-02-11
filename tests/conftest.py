import os
from unittest.mock import patch

import httpx
import pytest

from twilio_async.client import AsyncClient


@pytest.fixture
async def async_client():
    async with AsyncClient("test", "test") as client:
        yield client


@pytest.fixture(autouse=True)
def clear_environment_variables():
    with patch.dict(
        os.environ,
        {
            "TWILIO_ACCOUNT_SID": "",
            "TWILIO_AUTH_TOKEN": "",
            "TWILIO_MESSAGING_SERVICE_SID": "",
        },
        clear=True,
    ):
        yield


@pytest.fixture
def mock_message_response_data():
    return {
        "body": "test",
        "num_segments": 0,
        "direction": "test",
        "date_updated": "Sat, 11 Feb 2023 02:25:05 +0000",
        "uri": "test",
        "account_sid": "test",
        "num_media": 0,
        "to": "test",
        "date_created": "Sat, 11 Feb 2023 02:25:05 +0000",
        "status": "test",
        "sid": "test",
        "date_sent": "Sat, 11 Feb 2023 02:25:05 +0000",
        "api_version": "test",
        "subresource_uris": {"media": "test"},
    }
