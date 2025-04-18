from datetime import datetime, timedelta

import httpx
import pytest

import packaging_tutorial.pycon


@pytest.fixture(autouse=True)
def clear_cached_response() -> None:
    packaging_tutorial.pycon.get_programme.cache_clear()


def test_get_future_sessions() -> None:
    now = datetime.fromisoformat("20250512T12:00Z")
    past_sessions = [
        packaging_tutorial.pycon.Session(start=now - timedelta(hours=2)),
        packaging_tutorial.pycon.Session(start=now - timedelta(hours=1)),
        packaging_tutorial.pycon.Session(start=now - timedelta(hours=22)),
    ]
    future_sessions = [
        packaging_tutorial.pycon.Session(start=now + timedelta(hours=1)),
        packaging_tutorial.pycon.Session(start=now + timedelta(hours=21)),
    ]
    sessions = past_sessions + future_sessions

    assert list(packaging_tutorial.pycon.get_future_sessions(sessions, now=now)) == future_sessions


def test_get_sessions_caches_response(monkeypatch: pytest.MonkeyPatch):
    # Setup mock client
    def handler(request: httpx.Request) -> httpx.Response:
        handler.requests.append(request)
        return httpx.Response(200, json={"some data": 123})
    handler.requests = []

    transport = httpx.MockTransport(handler=handler)
    client = httpx.Client(transport=transport)
    monkeypatch.setattr(packaging_tutorial.pycon, "HTTP_CLIENT", client)

    # Act and assert
    packaging_tutorial.pycon.get_programme()
    packaging_tutorial.pycon.get_programme()
    assert len(handler.requests) == 1
