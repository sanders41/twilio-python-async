import os
from unittest.mock import patch

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
        "to": "+19018675309",
        "date_created": "Sat, 11 Feb 2023 02:25:05 +0000",
        "status": "test",
        "sid": "test",
        "date_sent": "Sat, 11 Feb 2023 02:25:05 +0000",
        "api_version": "test",
        "subresource_uris": {"media": "test"},
    }


@pytest.fixture
def mock_message_log_data():
    return {
        "first_page_uri": "/2010-04-01/Accounts/fakeaccountsid/Messages.json?PageSize=2&Page=0",
        "end": 1,
        "previous_page_uri": None,
        "messages": [
            {
                "body": "Test",
                "num_segments": "1",
                "direction": "outbound-api",
                "from": "+185558675309",
                "date_updated": "Sun, 12 Feb 2023 01:52:48 +0000",
                "price": "-0.00790",
                "error_message": None,
                "uri": "/2010-04-01/Accounts/fakeaccountsid/Messages/faketoken.json",
                "account_sid": "fakeaccountsid",
                "num_media": "0",
                "to": "+19198675309",
                "date_created": "Sun, 12 Feb 2023 01:52:47 +0000",
                "status": "delivered",
                "sid": "fakemessagesid",
                "date_sent": "Sun, 12 Feb 2023 01:52:47 +0000",
                "messaging_service_sid": "fakemessageservicesid",
                "error_code": None,
                "price_unit": "USD",
                "api_version": "2010-04-01",
                "subresource_uris": {
                    "media": "/2010-04-01/Accounts/fakeaccountsid/Messages/faketoken/Media.json",
                    "feedback": "/2010-04-01/Accounts/fakeaccountsid/Messages/faketoken/Feedback.json",
                },
            },
            {
                "body": "Bye",
                "num_segments": "1",
                "direction": "outbound-api",
                "from": "+18558675309",
                "date_updated": "Sat, 11 Feb 2023 14:18:27 +0000",
                "price": "-0.00790",
                "error_message": None,
                "uri": "/2010-04-01/Accounts/fakeaccountsid/Messages/faketoken.json",
                "account_sid": "fakeaccountsid",
                "num_media": "0",
                "to": "+19198675309",
                "date_created": "Sat, 11 Feb 2023 14:18:26 +0000",
                "status": "delivered",
                "sid": "faketoken",
                "date_sent": "Sat, 11 Feb 2023 14:18:26 +0000",
                "messaging_service_sid": "fakemessagingservicesid",
                "error_code": None,
                "price_unit": "USD",
                "api_version": "2010-04-01",
                "subresource_uris": {
                    "media": "/2010-04-01/Accounts/fakeaccountsid/Messages/faketoken/Media.json",
                    "feedback": "/2010-04-01/Accounts/fakeaccountsid/Messages/faketoken/Feedback.json",
                },
            },
        ],
        "uri": "/2010-04-01/Accounts/fakeaccountsid/Messages.json?PageSize=2&Page=0",
        "page_size": 2,
        "start": 0,
        "next_page_uri": "/2010-04-01/Accounts/fakeaccountsid/Messages.json?PageSize=2&Page=1&PageToken=PAfaketoken",
        "page": 0,
    }
