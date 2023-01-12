from typing import List

from app.domain.entity.person import Person
from app.shared.list_metadada_response import ListMetadataResponse
from app.shared.models import EntityModel


class PersonListResponse(EntityModel):
    meta: ListMetadataResponse
    data: List[Person]
