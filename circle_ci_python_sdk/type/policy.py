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


class RequiredPolicy(TypedDict):
    pass

class OptionalPolicy(TypedDict, total=False):
    content: str

    created_at: datetime

    created_by: str

    name: str

class Policy(RequiredPolicy, OptionalPolicy):
    pass