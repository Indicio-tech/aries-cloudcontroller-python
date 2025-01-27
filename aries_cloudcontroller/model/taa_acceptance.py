# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class TAAAcceptance(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TAAAcceptance - a model defined in OpenAPI
        mechanism: The mechanism of this TAAAcceptance [Optional].
        time: The time of this TAAAcceptance [Optional].
    """

    mechanism: Optional[str] = None
    time: Optional[int] = None

    def __init__(
        self,
        *,
        mechanism: Optional[str] = None,
        time: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            mechanism=mechanism,
            time=time,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


TAAAcceptance.update_forward_refs()
