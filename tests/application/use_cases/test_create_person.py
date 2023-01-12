
import pytest
from app.application.use_cases.create_person import CreatePerson
from app.application.use_cases.schemas.create_person_input_dto import CreatePersonInputDto
from app.domain.entity.person import Person
from app.exception.person_state_unauthorized_exception import PersonStateUnauthorizedException


class TestCreatePerson:

    @pytest.mark.asyncio
    async def test_when_create_person_ok(self, mock_person_repository, mock_message_bus):
        create_person_input_dto = CreatePersonInputDto(
            name="Person test",
            address="Address for person test",
            state="SP"
        )

        uc_create_person = CreatePerson(mock_person_repository, mock_message_bus)
        person_created = await uc_create_person.execute(create_person_input_dto)
        assert isinstance(person_created, Person)
        assert person_created.id == 1


    @pytest.mark.asyncio
    async def test_when_create_person_state_unauthorized_exception(self, mock_person_repository, mock_message_bus):

        with pytest.raises(PersonStateUnauthorizedException) as ex:
            create_person_input_dto = CreatePersonInputDto(
                name="Kevin Space",
                address="5 Avenue",
                state="MG"
            )

            uc_create_person = CreatePerson(mock_person_repository, mock_message_bus)
            await uc_create_person.execute(create_person_input_dto)
            assert str(ex.value) == "State unauthorized"
