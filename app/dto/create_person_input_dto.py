from app.shared.models import EntityModel


class CreatePersonInputDto(EntityModel):
    name: str
    address: str
    state: str
