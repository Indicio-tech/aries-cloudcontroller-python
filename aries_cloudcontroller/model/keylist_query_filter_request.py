# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class KeylistQueryFilterRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistQueryFilterRequest - a model defined in OpenAPI
        filter: Filter for keylist query [Optional].
    """

    filter: Optional[Dict[str, Any]] = None

    def __init__(
        self,
        *,
        filter: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(
            filter=filter,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


KeylistQueryFilterRequest.update_forward_refs()