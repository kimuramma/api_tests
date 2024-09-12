from pydantic import BaseModel, field_validator


class AuthModel(BaseModel):
    refresh: str
    access: str
