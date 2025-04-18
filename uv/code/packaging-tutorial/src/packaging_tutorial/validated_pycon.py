from collections.abc import Generator, Iterable
from datetime import UTC, datetime, timedelta
from functools import lru_cache
from typing import Any, Self

import httpx
import pydantic

try:
    from rich import print
except ImportError:
    pass


class Session(pydantic.BaseModel):
    room: str | None = None
    rooms: list[str] | None = None
    start: datetime | None = None
    end: datetime | None = None
    duration: timedelta | None = None
    kind: str | None = None
    section: str | None = None
    conf_key: int | None = None
    list_render: bool | None = None
    license: str | None = None
    tags: str | None = None
    released: bool | None = None
    contact: list[str] | None = None
    name: str | None = None
    description: str | None = None
    authors: list[str] | None = None
    speakers: list[dict[str, int | str]] | None = None
    conf_url: str | None = None
    cancelled: bool | None = None
    
    @classmethod
    def from_record(cls, record: dict[str, Any]) -> Self:
        return cls(
            room=record.get("room"),
            rooms=record.get("rooms"),
            start=(datetime.fromisoformat(t) if (t := record.get("start")) else None),
            end=(datetime.fromisoformat(t) if (t := record.get("end")) else None),
            duration=(timedelta(minutes=dt) if (dt := record.get("duration")) else None),
            kind=record.get("kind"),
            section=record.get("section"),
            conf_key=record.get("conf_key"),
            list_render=record.get("list_render"),
            license=record.get("license"),
            tags=record.get("tags"),
            released=record.get("released"),
            contact=record.get("contact"),
            name=record.get("name"),
            description=record.get("description"),
            authors=record.get("authors"),
            speakers=record.get("speakers"),
            conf_url=record.get("conf_url"),
            cancelled=record.get("cancelled"),
        )


HTTP_CLIENT = httpx.Client()


@lru_cache()
def get_programme() -> dict:
    response = HTTP_CLIENT.get("https://us.pycon.org/2025/schedule/conference.json")
    response.raise_for_status()
    return response.json()


def get_sessions() -> Generator[Session, None, None]:
    programme = get_programme()
    return (Session.from_record(record) for record in programme["schedule"])


def get_future_sessions(sessions: Iterable[Session], now: datetime | None = None) -> Generator[Session, None, None]:
    if now is None:
        now = datetime.now(tz=UTC)
    return (session for session in sessions if session.start and session.start > now)


def get_immediate_sessions(sessions: Iterable[Session], now: datetime | None = None) -> Generator[Session, None, None]:
    sessions = list(get_future_sessions(sessions, now=now))
    start_time = min(session.start for session in sessions if session.start)
    return (session for session in sessions if session.start == start_time)


def main() -> None:
    sessions = get_sessions()

    print("Next sessions:")
    print("==============\n")
    for session in get_immediate_sessions(sessions):
        print(session.name, session.start )


if __name__ == "__main__":
    main()
    