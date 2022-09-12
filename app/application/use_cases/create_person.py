from app.application.repository.person_repository import PersonRepository
from app.config.settings import settings
from app.domain.entity.person import Person
from app.dto.create_person_input_dto import CreatePersonInputDto
from app.infrastructure.messaging.kafka_message_bus import KafkaMessageBus
from loguru import logger


class CreatePerson:

    def __init__(self, repository: PersonRepository, message_bus=None):
        self.repository = repository
        self.message_bus = KafkaMessageBus() if not message_bus else message_bus

    async def execute(self, create_person_input_dto: CreatePersonInputDto) -> Person:
        logger.info("Use case - create person")
        person = Person(**create_person_input_dto.dict())

        logger.info("Use rules on domain")
        person.validate_rules()
        person_created = self.repository.save(person)

        await self.message_bus.send_message(settings.KAFKA_TOPIC, person.dict())

        return person_created



