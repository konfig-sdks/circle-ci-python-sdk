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


class RequiredScheduleGetByIdResponseActor(TypedDict):
    # The unique ID of the user.
    id: str

    # The login information for the user on the VCS.
    login: str

    # The name of the user.
    name: str

class OptionalScheduleGetByIdResponseActor(TypedDict, total=False):
    pass

class ScheduleGetByIdResponseActor(RequiredScheduleGetByIdResponseActor, OptionalScheduleGetByIdResponseActor):
    pass