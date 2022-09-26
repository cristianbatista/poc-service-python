from typing import Optional

from app.shared.models import EntityModel


class ListMetadataResponse(EntityModel):
    prev: Optional[str] = None
    next: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    total: Optional[int] = None
