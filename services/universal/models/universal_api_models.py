from __future__ import annotations

from typing import Any, List, Optional
from pydantic import BaseModel, field_validator


class AuthModel(BaseModel):
    refresh: str
    access: str

    field_validator("refresh", "access")

    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            return ValueError("Пустое поле")
        else:
            return value


class ApprovedParams(BaseModel):
    period: int
    principal: int
    prepayment_amount: int
    interest_rate: float
    effective_rate: float
    monthly_payment: float


def fields_are_not_empty(cls, value):
    if value == "" or value is None:
        return ValueError("Пустое поле")
    else:
        return value


class GetScoringResultModel(BaseModel):
    result: str
    alternative_reason: str
    alternative_sum: Any
    redirect_url: str
    approved_params: ApprovedParams
    additional_approved_params: List
    product: str

    @field_validator("result", "alternative_reason", "alternative_sum")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            return ValueError("Пустое поле")
        else:
            return value
