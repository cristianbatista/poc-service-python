from app.shared.models import EntityModel


class PersonCreateRequest(EntityModel):
    name: str
    address: str
    state: str
