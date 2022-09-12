from abc import abstractmethod, ABC

from app.domain.entity.person import Person


class PersonRepository(ABC):

    @abstractmethod
    def get(self, person_id):
        raise NotImplementedError()

    @abstractmethod
    def save(self, person: Person):
        raise NotImplementedError()
