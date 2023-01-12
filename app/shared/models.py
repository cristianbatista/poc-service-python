from datetime import datetime

from pydantic import BaseConfig, BaseModel

from .serializers import to_camel


class EntityModel(BaseModel):
    """Base class for all models."""

    class Config(BaseConfig):
        alias_generator = to_camel
        allow_population_by_field_name = True
        json_encoders = {datetime: lambda dt: dt.strftime("%Y-%m-%dT%H:%M:%SZ")}
