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

from circle_ci_python_sdk.type.webhook_create_outbound_webhook_response_events import WebhookCreateOutboundWebhookResponseEvents
from circle_ci_python_sdk.type.webhook_create_outbound_webhook_response_scope import WebhookCreateOutboundWebhookResponseScope

RequiredWebhookCreateOutboundWebhookResponse = TypedDict("RequiredWebhookCreateOutboundWebhookResponse", {
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

    "scope": WebhookCreateOutboundWebhookResponseScope,

    "events": WebhookCreateOutboundWebhookResponseEvents,
    })

OptionalWebhookCreateOutboundWebhookResponse = TypedDict("OptionalWebhookCreateOutboundWebhookResponse", {
    }, total=False)

class WebhookCreateOutboundWebhookResponse(RequiredWebhookCreateOutboundWebhookResponse, OptionalWebhookCreateOutboundWebhookResponse):
    pass
