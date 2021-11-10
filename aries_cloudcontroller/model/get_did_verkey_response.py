# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class GetDIDVerkeyResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetDIDVerkeyResponse - a model defined in OpenAPI
        verkey: Full verification key [Optional].
    """

    verkey: Optional[str] = None

    def __init__(
        self,
        *,
        verkey: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            verkey=verkey,
            **kwargs,
        )

    @validator("verkey")
    def verkey_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = (
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"
        )
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of verkey does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


GetDIDVerkeyResponse.update_forward_refs()