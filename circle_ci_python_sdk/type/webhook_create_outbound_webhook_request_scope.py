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


class RequiredWebhookCreateOutboundWebhookRequestScope(TypedDict):
    # ID of the scope being used (at the moment, only project ID is supported)
    id: str

    # Type of the scope being used
    type: str

class OptionalWebhookCreateOutboundWebhookRequestScope(TypedDict, total=False):
    pass

class WebhookCreateOutboundWebhookRequestScope(RequiredWebhookCreateOutboundWebhookRequestScope, OptionalWebhookCreateOutboundWebhookRequestScope):
    pass
