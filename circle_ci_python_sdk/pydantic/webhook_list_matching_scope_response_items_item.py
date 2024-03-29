# coding: utf-8

"""
    CircleCI API

    This describes the resources that make up the CircleCI API v2.

    The version of the OpenAPI document: v2
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from circle_ci_python_sdk.pydantic.webhook_list_matching_scope_response_items_item_events import WebhookListMatchingScopeResponseItemsItemEvents
from circle_ci_python_sdk.pydantic.webhook_list_matching_scope_response_items_item_scope import WebhookListMatchingScopeResponseItemsItemScope

class WebhookListMatchingScopeResponseItemsItem(BaseModel):
    # URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)
    url: str = Field(alias='url')

    # Whether to enforce TLS certificate verification when delivering the webhook
    verify-tls_: bool = Field(alias='verify-tls')

    # The unique ID of the webhook
    id: str = Field(alias='id')

    # Masked value of the secret used to build an HMAC hash of the payload and passed as a header in the webhook request
    signing-secret_: str = Field(alias='signing-secret')

    # The date and time the webhook was last updated.
    updated-at_: datetime = Field(alias='updated-at')

    # Name of the webhook
    name: str = Field(alias='name')

    # The date and time the webhook was created.
    created-at_: datetime = Field(alias='created-at')

    scope: WebhookListMatchingScopeResponseItemsItemScope = Field(alias='scope')

    events: WebhookListMatchingScopeResponseItemsItemEvents = Field(alias='events')
    class Config:
        arbitrary_types_allowed = True
