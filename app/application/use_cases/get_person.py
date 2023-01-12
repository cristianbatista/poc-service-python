from loguru import logger

from app.application.repository.person_repository import PersonRepository
from app.exception.person_not_found_exception import PersonNotFoundException


class GetPerson:
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    async def execute(self, id: int):
        logger.info("Use case - get person")
        person = await self.repository.get(id)

        if person is None:
            raise PersonNotFoundException()

        return person
