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


class RequiredContextCreateNewContextResponse(TypedDict):
    # The unique ID of the context.
    id: str

    # The user defined name of the context.
    name: str

    # The date and time the context was created.
    created_at: datetime

class OptionalContextCreateNewContextResponse(TypedDict, total=False):
    pass

class ContextCreateNewContextResponse(RequiredContextCreateNewContextResponse, OptionalContextCreateNewContextResponse):
    pass
