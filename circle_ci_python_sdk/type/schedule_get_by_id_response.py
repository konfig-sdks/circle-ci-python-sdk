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

from circle_ci_python_sdk.type.schedule_get_by_id_response_actor import ScheduleGetByIdResponseActor
from circle_ci_python_sdk.type.schedule_get_by_id_response_parameters import ScheduleGetByIdResponseParameters

RequiredScheduleGetByIdResponse = TypedDict("RequiredScheduleGetByIdResponse", {
    # Description of the schedule.
    "description": typing.Optional[str],

    "parameters": ScheduleGetByIdResponseParameters,

    # The unique ID of the schedule.
    "id": str,

    # Timetable that specifies when a schedule triggers.
    "timetable": typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],

    # The date and time the pipeline was last updated.
    "updated-at": datetime,

    # Name of the schedule.
    "name": str,

    # The date and time the pipeline was created.
    "created-at": datetime,

    # The project-slug for the schedule
    "project-slug": str,

    "actor": ScheduleGetByIdResponseActor,
    })

OptionalScheduleGetByIdResponse = TypedDict("OptionalScheduleGetByIdResponse", {
    }, total=False)

class ScheduleGetByIdResponse(RequiredScheduleGetByIdResponse, OptionalScheduleGetByIdResponse):
    pass
