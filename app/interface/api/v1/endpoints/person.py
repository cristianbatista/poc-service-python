from fastapi import APIRouter, status
from loguru import logger
from starlette.responses import JSONResponse

from app.application.use_cases.create_person import CreatePerson
from app.application.use_cases.get_person import GetPerson
from app.application.use_cases.schemas.create_person_input_dto import (
    CreatePersonInputDto,
)
from app.domain.entity.person import Person
from app.exception.person_not_found_exception import PersonNotFoundException
from app.infrastructure.messaging.kafka_message_bus import KafkaMessageBus
from app.infrastructure.repositories.postgre_person_repository import (
    PostgrePersonRepository,
)
from app.interface.api.v1.schemas.person_create_request import PersonCreateRequest

router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=Person,
    summary="Create Person",
)
async def create_person(create_person_request: PersonCreateRequest) -> Person:
    logger.info("Received request POST - controller person")
    repository = PostgrePersonRepository()
    message_bus = KafkaMessageBus()
    uc_create_person = CreatePerson(repository, message_bus)
    create_person_input_dto = CreatePersonInputDto(**create_person_request.dict())

    return await uc_create_person.execute(create_person_input_dto)


@router.get("/{id}", response_model=Person, summary="Get Person by Id")
async def get_person(id: int) -> JSONResponse:
    try:
        logger.info("Received request GET - controller person")
        repository = PostgrePersonRepository()
        uc_get_person = GetPerson(repository)
        person = await uc_get_person.execute(id)
        return person
    except PersonNotFoundException as pnfe:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"error": pnfe.message}
        )
