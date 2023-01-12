from abc import ABC, abstractmethod

from app.domain.entity.person import Person


class PersonRepository(ABC):
    @abstractmethod
    async def get(self, person_id) -> Person:
        raise NotImplementedError()

    @abstractmethod
    async def save(self, person: Person) -> Person:
        raise NotImplementedError()
