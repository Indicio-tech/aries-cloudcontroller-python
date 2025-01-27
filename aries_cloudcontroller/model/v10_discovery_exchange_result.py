# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v10_discovery_record import V10DiscoveryRecord


class V10DiscoveryExchangeResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10DiscoveryExchangeResult - a model defined in OpenAPI
        results: Discover Features v1.0 exchange record [Optional].
    """

    results: Optional[V10DiscoveryRecord] = None

    def __init__(
        self,
        *,
        results: Optional[V10DiscoveryRecord] = None,
        **kwargs,
    ):
        super().__init__(
            results=results,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V10DiscoveryExchangeResult.update_forward_refs()
