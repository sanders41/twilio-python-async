from __future__ import annotations

import os
from types import TracebackType
from typing import Type

from httpx import AsyncClient as HttpxAsyncClient

from twilio_async.models.message import Message


class AsyncClient:
    """A client for interacting with the Twilio API."""

    def __init__(
        self,
        account_sid: str | None = None,
        token: str | None = None,
        *,
        timeout: int | None = None,
    ) -> None:
        """Class initializer.

        Args:
            account_sid: Account SID. If `None` will attempt to read from the `TWILIO_ACCOUNT_SID`
                envoronment variable.
            token: Authentication token. If `None` will attempt to read from `TWILIO_AUTH_TOKEN`.
            timeout: The amount of time in seconds that the client will wait for a response before
                timing out. Defaults to None.
        """

        self.account_sid = account_sid or os.getenv("TWILIO_ACCOUNT_SID", None)

        if not self.account_sid:
            raise ValueError("No account_sid found")

        self.token = token or os.getenv("TWILIO_AUTH_TOKEN", None)

        if not self.token:
            raise ValueError("No account_sid found")

        self._http_client = HttpxAsyncClient(
            base_url=f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/",
            timeout=timeout,
            auth=(self.account_sid, self.token),
        )

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(
        self,
        et: Type[BaseException] | None,
        ev: Type[BaseException] | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        """Closes the client.

        This only needs to be used if the client was not created with a context manager.
        """
        await self._http_client.aclose()

    async def message_create(
        self,
        body: str,
        to: str,
        *,
        from_: str | None = None,
        messaging_service_sid: str | None = None,
    ) -> Message:
        """Sends a message.

        Args:
            body: Message body.
            to: The phone number to send the message to.
            from_: The phone number to send the message from. Defaults to `None`

        Returns:
            Message response information.

        Examples:
            >>> from twilio_async import AsyncClient
            >>> async with AsyncClient() as client:
            >>>     response = await client.message_create(
            >>>         "My message",
            >>>         "+15018675301",
            >>>     )
        """
        sid = messaging_service_sid or os.getenv("TWILIO_MESSAGING_SERVICE_SID", None)

        if not sid and not from_:
            raise ValueError("A messaging_service_sid or from_ is required")

        payload = {
            "Body": body,
            "To": to,
        }

        if sid:
            payload["MessagingServiceSid"] = sid

        if from_:
            payload["From"] = from_

        response = await self._http_client.post(
            url="Messages.json",
            data=payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        response.raise_for_status()

        return Message(**response.json())
