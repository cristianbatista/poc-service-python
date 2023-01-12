from typing import Any, Optional

from app.shared.models import EntityModel


class ApiError(EntityModel):
    developer_message: Optional[str] = None
    user_message: Optional[str] = None


class RequestValidationApiError(ApiError):
    errors: Any
