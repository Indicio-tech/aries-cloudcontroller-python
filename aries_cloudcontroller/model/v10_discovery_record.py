# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.disclose import Disclose
from aries_cloudcontroller.model.query import Query


class V10DiscoveryRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10DiscoveryRecord - a model defined in OpenAPI
        connection_id: Connection identifier [Optional].
        created_at: Time of record creation [Optional].
        disclose: Disclose message [Optional].
        discovery_exchange_id: Credential exchange identifier [Optional].
        query_msg: Query message [Optional].
        state: Current record state [Optional].
        thread_id: Thread identifier [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        updated_at: Time of last record update [Optional].
    """

    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    disclose: Optional[Disclose] = None
    discovery_exchange_id: Optional[str] = None
    query_msg: Optional[Query] = None
    state: Optional[str] = None
    thread_id: Optional[str] = None
    trace: Optional[bool] = None
    updated_at: Optional[str] = None

    def __init__(
        self,
        *,
        connection_id: Optional[str] = None,
        created_at: Optional[str] = None,
        disclose: Optional[Disclose] = None,
        discovery_exchange_id: Optional[str] = None,
        query_msg: Optional[Query] = None,
        state: Optional[str] = None,
        thread_id: Optional[str] = None,
        trace: Optional[bool] = None,
        updated_at: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            connection_id=connection_id,
            created_at=created_at,
            disclose=disclose,
            discovery_exchange_id=discovery_exchange_id,
            query_msg=query_msg,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
            **kwargs,
        )

    @validator("created_at")
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created_at does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of updated_at does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


V10DiscoveryRecord.update_forward_refs()