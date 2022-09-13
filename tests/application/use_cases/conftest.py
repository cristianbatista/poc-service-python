import asyncio

import pytest
import asynctest

from app.application.messaging.message_bus import MessageBus
from app.application.repository.person_repository import PersonRepository
from app.domain.entity.person import Person


def mock_dto_create_person_success() -> Person:
    person_return = Person(
        id=1,
        name="Person test",
        address="Address for person test",
        state="SP"
    )

    return person_return


@pytest.fixture
def mock_person_repository():
    mock_person_repository = asynctest.Mock(spec=PersonRepository)
    mock_person_repository.save.return_value = asyncio.Future()
    mock_person_repository.save.return_value.set_result(mock_dto_create_person_success())
    return mock_person_repository


@pytest.fixture
def mock_message_bus():
    mock_message_bus = asynctest.Mock(spec=MessageBus)
    mock_message_bus.send_message.return_value = asyncio.Future()
    mock_message_bus.send_message.return_value.set_result(None)
    return mock_message_bus
