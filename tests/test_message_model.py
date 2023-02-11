from datetime import datetime, timezone

import pytest

from twilio_async.models.message import MessageResponse, SubresouceUris


@pytest.mark.parametrize(
    "date_sent, expected_date_sent",
    [
        (None, None),
        ("Sat, 11 Feb 2023 02:25:05 +0000", datetime(2023, 2, 11, 2, 25, 5, tzinfo=timezone.utc)),
    ],
)
def test_date_parse(date_sent, expected_date_sent):
    str_date = "Sat, 11 Feb 2023 02:25:05 +0000"
    expected_date = datetime(2023, 2, 11, 2, 25, 5, tzinfo=timezone.utc)
    result = MessageResponse(
        body="test",
        num_segments=0,
        direction="test",
        date_updated=str_date,
        uri="test",
        account_sid="test",
        num_media=0,
        to="test",
        date_created=str_date,
        status="test",
        sid="test",
        date_sent=date_sent,
        api_version="test",
        subresource_uris=SubresouceUris(media="test"),
    )

    assert result.date_updated == expected_date
    assert result.date_created == expected_date
    assert result.date_sent == expected_date_sent
