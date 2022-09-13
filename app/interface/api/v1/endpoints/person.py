from fastapi import APIRouter, Depends, status
from loguru import logger
from starlette.responses import JSONResponse

from app.application.use_cases.create_person import CreatePerson
from app.application.use_cases.get_person import GetPerson
from app.dto.create_person_input_dto import CreatePersonInputDto
from app.exception.person_not_found_exception import PersonNotFoundException
from app.exception.person_state_unauthorized_exception import (
    PersonStateUnauthorizedException,
)
from app.infrastructure.messaging.kafka_message_bus import KafkaMessageBus
from app.infrastructure.repositories.postgre_person_repository import (
    PostgrePersonRepository,
)

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED, summary="Create Person")
async def create_person(
    create_person_input_dto: CreatePersonInputDto,
    repository: PostgrePersonRepository = Depends(),
    message_bus: KafkaMessageBus = Depends(),
):
    try:
        logger.info("Received request POST - controller person")
        uc_create_person = CreatePerson(repository, message_bus)
        return await uc_create_person.execute(create_person_input_dto)
    except PersonStateUnauthorizedException as psue:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, content={"error": psue.message}
        )


@router.get("/{id}", summary="Create Person")
async def get_person(id: int) -> JSONResponse:
    try:
        logger.info("Received request GET - controller person")
        repository = PostgrePersonRepository()
        uc_get_person = GetPerson(repository)
        person = uc_get_person.execute(id)
        return person
    except PersonNotFoundException as pnfe:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"error": pnfe.message}
        )
