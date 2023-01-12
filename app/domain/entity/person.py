from typing import Optional

from app.exception.person_state_unauthorized_exception import (
    PersonStateUnauthorizedException,
)
from app.shared.models import EntityModel


class Person(EntityModel):
    id: Optional[int]
    name: str
    address: str
    state: str

    def validate_rules(self):
        if self.state.upper() == "MG":
            raise PersonStateUnauthorizedException()

        return True
