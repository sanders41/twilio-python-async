import os
from unittest.mock import patch

import httpx
import pytest

from twilio_async.client import AsyncClient


async def test_client_no_account_sid():
    with pytest.raises(ValueError):
        async with AsyncClient(token="test"):
            ...


async def test_client_no_token():
    with pytest.raises(ValueError):
        async with AsyncClient(account_sid="test"):
            ...


async def test_client():
    async with AsyncClient("account_sid", "token") as client:
        assert client.account_sid == "account_sid"
        assert client.token == "token"


@patch.dict(
    os.environ,
    {"TWILIO_ACCOUNT_SID": "account_sid", "TWILIO_AUTH_TOKEN": "token"},
    clear=True,
)
async def test_client_environment_variables():
    async with AsyncClient() as client:
        assert client.account_sid == "account_sid"
        assert client.token == "token"


async def test_message_create_no_messaging_service_id():
    with pytest.raises(ValueError):
        async with AsyncClient("test", "test") as client:
            await client.message_create("test", "+13368675309")


async def test_message_create_from(mock_message_response_data, monkeypatch):
    async def mock_return(*args, **kwargs):
        return httpx.Response(
            status_code=200,
            json=mock_message_response_data,
            request=httpx.Request(url=kwargs["url"], method="post"),
        )

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_return)
    async with AsyncClient("account_sid", "token") as client:
        response = await client.message_create("test", "+13368675309", from_="+13369035768")

    assert response.body == mock_message_response_data["body"]


@patch.dict(
    os.environ,
    {"TWILIO_MESSAGING_SERVICE_SID": "messaging_id"},
    clear=True,
)
async def test_message_create_env_var(mock_message_response_data, monkeypatch):
    async def mock_return(*args, **kwargs):
        return httpx.Response(
            status_code=200,
            json=mock_message_response_data,
            request=httpx.Request(url=kwargs["url"], method="post"),
        )

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_return)
    async with AsyncClient("account_sid", "token") as client:
        response = await client.message_create("test", "+13368675309")

    assert response.body == mock_message_response_data["body"]
