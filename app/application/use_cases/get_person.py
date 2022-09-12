from app.application.repository.person_repository import PersonRepository
from app.exception.person_not_found_exception import PersonNotFoundException
from loguru import logger


class GetPerson:

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def execute(self, id: int):
        logger.info("Use case - get person")
        person = self.repository.get(id)

        if person is None:
            raise PersonNotFoundException()

        return person



