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

from circle_ci_python_sdk.type.webhook_get_by_id_response_events import WebhookGetByIdResponseEvents
from circle_ci_python_sdk.type.webhook_get_by_id_response_scope import WebhookGetByIdResponseScope

RequiredWebhookGetByIdResponse = TypedDict("RequiredWebhookGetByIdResponse", {
    # URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)
    "url": str,

    # Whether to enforce TLS certificate verification when delivering the webhook
    "verify-tls": bool,

    # The unique ID of the webhook
    "id": str,

    # Masked value of the secret used to build an HMAC hash of the payload and passed as a header in the webhook request
    "signing-secret": str,

    # The date and time the webhook was last updated.
    "updated-at": datetime,

    # Name of the webhook
    "name": str,

    # The date and time the webhook was created.
    "created-at": datetime,

    "scope": WebhookGetByIdResponseScope,

    "events": WebhookGetByIdResponseEvents,
    })

OptionalWebhookGetByIdResponse = TypedDict("OptionalWebhookGetByIdResponse", {
    }, total=False)

class WebhookGetByIdResponse(RequiredWebhookGetByIdResponse, OptionalWebhookGetByIdResponse):
    pass
