import pytest
import asynctest
import asyncio

from unittest.mock import Mock
from app.application.repository.person_repository import PersonRepository
from app.infrastructure.messaging.kafka_message_bus import KafkaMessageBus
from app.application.use_cases.create_person import CreatePerson
from app.domain.entity.person import Person
from app.dto.create_person_input_dto import CreatePersonInputDto


def person() -> Person:
    person_return = Person(
        id=1,
        name="Person test",
        address="Address for person test",
        state="SP"
    )

    return person_return


@pytest.fixture
def mock_person_repository():
    mock_person_repository = Mock(spec=PersonRepository)
    mock_person_repository.save.return_value = person()
    return mock_person_repository


@pytest.fixture
def mock_message_bus():
    mock_message_bus = asynctest.Mock(KafkaMessageBus())
    mock_message_bus.send_message.return_value = asyncio.Future()
    mock_message_bus.send_message.return_value.set_result(None)
    return mock_message_bus


@pytest.mark.asyncio
async def test_when_create_person_ok(mock_person_repository):
    create_person_input_dto = CreatePersonInputDto(
        name="Person test",
        address="Address for person test",
        state="SP"
    )

    uc_create_person = CreatePerson(mock_person_repository)
    person_created = await uc_create_person.execute(create_person_input_dto)
    assert isinstance(person_created, Person)
