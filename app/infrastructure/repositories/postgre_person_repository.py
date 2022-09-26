from typing import List

from loguru import logger

from app.application.repository.person_repository import PersonRepository
from app.domain.entity.person import Person
from app.infrastructure.database.postgre import SessionLocal
from app.infrastructure.models import PersonModel


class PostgrePersonRepository(PersonRepository):
    def __init__(self, session_local_db: SessionLocal = None):
        self.session_db = SessionLocal() if not session_local_db else session_local_db

    async def get(self, person_id) -> Person:
        logger.info("Get person - repository")
        person = (
            self.session_db.query(PersonModel)
            .filter(PersonModel.id == person_id)
            .first()
        )

        return self._row_to_entity(person)

    async def list(self) -> List[Person]:
        logger.info("List person - repository")
        records = (
            self.session_db.query(PersonModel)
            .order_by(PersonModel.id)
            .limit(10)
            .offset(0)
            .all()
        )

        x = [self._row_to_entity(item) for item in records]
        return x

    async def save(self, person: Person) -> Person:
        logger.info("Save person - repository")
        person_model = PersonModel(**person.dict())
        self.session_db.add(person_model)
        self.session_db.commit()
        self.session_db.refresh(person_model)
        return self._row_to_entity(person_model)

    @staticmethod
    def _row_to_entity(person_model: PersonModel):
        if person_model is not None:
            return Person(
                id=person_model.id,
                name=person_model.name,
                address=person_model.address,
                state=person_model.state,
            )
        return None
