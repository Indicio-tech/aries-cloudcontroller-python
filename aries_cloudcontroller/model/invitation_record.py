# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.invitation_message import InvitationMessage


class InvitationRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InvitationRecord - a model defined in OpenAPI
        created_at: Time of record creation [Optional].
        invi_msg_id: Invitation message identifier [Optional].
        invitation: Out of band invitation message [Optional].
        invitation_id: Invitation record identifier [Optional].
        invitation_url: Invitation message URL [Optional].
        state: Out of band message exchange state [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        updated_at: Time of last record update [Optional].
    """

    created_at: Optional[str] = None
    invi_msg_id: Optional[str] = None
    invitation: Optional[InvitationMessage] = None
    invitation_id: Optional[str] = None
    invitation_url: Optional[str] = None
    state: Optional[str] = None
    trace: Optional[bool] = None
    updated_at: Optional[str] = None

    def __init__(
        self,
        *,
        created_at: Optional[str] = None,
        invi_msg_id: Optional[str] = None,
        invitation: Optional[InvitationMessage] = None,
        invitation_id: Optional[str] = None,
        invitation_url: Optional[str] = None,
        state: Optional[str] = None,
        trace: Optional[bool] = None,
        updated_at: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            created_at=created_at,
            invi_msg_id=invi_msg_id,
            invitation=invitation,
            invitation_id=invitation_id,
            invitation_url=invitation_url,
            state=state,
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


InvitationRecord.update_forward_refs()