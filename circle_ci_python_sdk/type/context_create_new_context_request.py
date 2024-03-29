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


class RequiredContextCreateNewContextRequest(TypedDict):
    # The user defined name of the context.
    name: str

    owner: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class OptionalContextCreateNewContextRequest(TypedDict, total=False):
    pass

class ContextCreateNewContextRequest(RequiredContextCreateNewContextRequest, OptionalContextCreateNewContextRequest):
    pass
