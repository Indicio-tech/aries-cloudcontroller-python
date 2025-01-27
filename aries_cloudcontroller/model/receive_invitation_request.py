# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class ReceiveInvitationRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ReceiveInvitationRequest - a model defined in OpenAPI
        id: Message identifier [Optional].
        type: Message type [Optional].
        did: DID for connection invitation [Optional].
        image_url: Optional image URL for connection invitation [Optional].
        label: Optional label for connection invitation [Optional].
        recipient_keys: List of recipient keys [Optional].
        routing_keys: List of routing keys [Optional].
        service_endpoint: Service endpoint at which to reach this agent [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    did: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    label: Optional[str] = None
    recipient_keys: Optional[List[str]] = Field(None, alias="recipientKeys")
    routing_keys: Optional[List[str]] = Field(None, alias="routingKeys")
    service_endpoint: Optional[str] = Field(None, alias="serviceEndpoint")

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        did: Optional[str] = None,
        image_url: Optional[str] = None,
        label: Optional[str] = None,
        recipient_keys: Optional[List[str]] = None,
        routing_keys: Optional[List[str]] = None,
        service_endpoint: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            did=did,
            image_url=image_url,
            label=label,
            recipient_keys=recipient_keys,
            routing_keys=routing_keys,
            service_endpoint=service_endpoint,
            **kwargs,
        )

    @validator("did")
    def did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of did does not match regex pattern ('{pattern}')")
        return value

    class Config:
        allow_population_by_field_name = True


ReceiveInvitationRequest.update_forward_refs()
